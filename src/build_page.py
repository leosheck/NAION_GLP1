import json,re,ast,sys
sys.path.insert(0,'/mnt/project-files/glp1-eye-risks/src')
from data_rows import *
SRC='/mnt/project-files/glp1-eye-risks/src/'
import os
TPL=os.environ.get('TPL',SRC+'template.html');OUT=os.environ.get('OUT','/mnt/project-files/glp1-eye-risks/glp1-eye-risks.html')
t=open(TPL).read()
meta=json.load(open(SRC+'pubmed_metadata.json'))
bb=[l for l in open('/mnt/project-files/namd-injections/namd-injections.html') if 'class="brandbar"' in l][0].strip()
CALC=[dict(l='Time-varying (Danish data)',ref='niazi26',note='Excess confined to 6 to 24 months. The Danish ratios are larger than the pooled average; with the Danish starting rate of 9 the peak is about 1 extra case per 4,200 people per year.',periods=[
   dict(frm=0,to=6,est=1.0,lo=1.0,hi=1.0,ref='niazi26',basis='Published 0.80 (0.32 to 2.05); treated as no excess'),
   dict(frm=6,to=12,est=3.63,lo=2.06,hi=6.40,ref='niazi26',basis='Danish case-control'),
   dict(frm=12,to=24,est=3.52,lo=1.73,hi=7.17,ref='niazi26',basis='Danish case-control, 12 to 18 months; assumed to 24'),
   dict(frm=24,to=None,est=1.0,lo=1.0,hi=1.0,ref='hsu',basis='Assumed no excess; fits cumulative ratio of about 2 at 4 years')]),
 dict(l='Constant, pooled (Liu 1.85)',ref='liu',note='A constant ratio overstates early risk and understates the peak.',periods=[dict(frm=0,to=None,est=1.85,lo=1.20,hi=2.85,ref='liu',basis='Pooled observational studies, diabetes')]),
 dict(l='Constant, US Veterans (Choi 1.35)',ref='choi',note='A constant ratio overstates early risk and understates the peak.',periods=[dict(frm=0,to=None,est=1.35,lo=1.11,hi=1.51,ref='choi',basis='Chart-checked diagnosis codes, 3 years')])]
FORESTS={'naion':NAION,'dr':DR,'glau':GLAU,'amd':AMD,'other':OTHER}
order=[]
def use(k):
    if k not in order: order.append(k)
for m in re.finditer(r'\{\{(\w+)\}\}|data-forest="(\w+)"|id="(pvBody|calcRR)"|data-abs="([^"]+)"',t):
    if m.group(4): [use(o[0]) for o in rate_rows() if o[2]==m.group(4)]
    elif m.group(1): use(m.group(1))
    elif m.group(2): [use(r[0]) for r in FORESTS[m.group(2)]]
    elif m.group(3)=='pvBody': [use(p[0]) for p in PV]
    else: [use(q['ref']) for c in CALC for q in c['periods']]
num={k:i+1 for i,k in enumerate(order)}
def lit(s):
    try: return ast.literal_eval(s) if isinstance(s,str) else s
    except Exception: return s
refs=[];missing=[]
for k in order:
    if k in MANUAL:
        m=MANUAL[k];short={'dmr':'Danesh-Meyer 2026','ema':'EMA 2025','focus':'FOCUS trial'}[k]
        refs.append(dict(n=num[k],key=k,cite=m['cite'],doi=m.get('doi'),url=m.get('url'),pmid=None,short=short,lib=k in LIBRARY));continue
    p=REFKEYS.get(k)
    if not p or p not in meta: missing.append(k);continue
    d=meta[p];au=lit(d.get('authors')) or [];j=lit(d.get('journal')) or {};pd=lit(d.get('publication_date')) or {};ci=lit(d.get('citation')) or {}
    names=[(a.get('last_name','')+' '+a.get('initials','')).strip() for a in au if isinstance(a,dict)]
    names=[n for n in names if n]
    a=', '.join(names[:3])+(', et al' if len(names)>3 else '')
    yr=pd.get('year','') if isinstance(pd,dict) else ''
    vol=ci.get('volume') if isinstance(ci,dict) else None;pg=ci.get('pages') if isinstance(ci,dict) else None
    jt=j.get('iso_abbreviation') or j.get('title','')
    cite=f"{a}. {d['title'].rstrip('.')}. {jt} {yr}"+(f";{vol}" if vol else '')+(f":{pg}" if pg else '')+'.'
    last=au[0].get('last_name','') if au and isinstance(au[0],dict) else ''
    if not last and au and isinstance(au[0],dict): last=au[0].get('collective_name','')
    refs.append(dict(n=num[k],key=k,cite=cite,doi=d.get('doi'),pmid=p,url=None,short=f"{last} {yr}",lib=k in LIBRARY))
if missing: raise SystemExit('missing '+str(missing))
def rows(R):
    out=[]
    for r in R:
        d=dict(ref=num[r[0]],label=r[1],est=r[2],lo=r[3],hi=r[4],measure=r[5],group=r[6],kind=r[7],note=r[8])
        q=RATES.get((r[0],r[1]))
        if q: d.update(rd=q[0],rc=q[1],rx=q[2],rn=q[3])
        out.append(d)
    return out
data=dict(refs=refs,forests={k:rows(v) for k,v in FORESTS.items() if f'data-forest="{k}"' in t},
          absr=[dict(ref=num[o[0]],label=o[1],grp=o[2],rd=o[3],rc=o[4],rx=o[5],rn=o[6],stype=o[7]) for o in rate_rows() if o[2]=='NAION'],
          pv=[],
          calcRR=[dict(l=c['l'],note=c['note'],periods=[dict(**{'from':q['frm'],'to':q['to'],'est':q['est'],'lo':q['lo'],'hi':q['hi'],'basis':q['basis'],'ref':num[q['ref']]}) for q in c['periods']]) for c in CALC])
if not os.environ.get('DOC'): json.dump(data,open(SRC+'data.json','w'),indent=1)
t=re.sub(r'\{\{(\w+)\}\}',lambda m:f'<sup class="r"><a href="#ref{num[m.group(1)]}">{num[m.group(1)]}</a></sup>',t)
t=re.sub(r'</sup><sup class="r">',r'</sup><sup class="r">,',t)
t=t.replace('/*BRANDBAR*/',bb).replace('/*DATA*/',json.dumps(data,separators=(',',':'),ensure_ascii=False)).replace('/*QCOUNT*/','22').replace('/*META*/','300').replace('/*KEEP*/','151')
if os.environ.get('DOC'):
    head,body=t.split('<div class="wrap">',1)
    t='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'+head.strip()+'\n</head>\n<body>\n<div class="wrap">'+body+'\n</body>\n</html>\n'
    json.dump(data,open(os.path.join(os.path.dirname(OUT),'data.json'),'w'),indent=1)
open(OUT,'w').write(t)
print(len(t),len(refs),'refs')
