# Study rows for the GLP-1 eye risk page. Ratios are GLP-1 drug against comparator (above 1 = more events on the GLP-1 drug).
# (key, label, est, lo, hi, measure, group, kind, note)
REFKEYS = {
 'hathaway':'38958939','grauslund':'39696569','simonsen':'40098249','niazi26':'42126975','ueda':'42441962','noh':'41701611',
 'reynolds':'42441967','tesfaye':'41104517','heberer':'41678180','choi':'42060307','chenDM':'41687959','wang25':'40788646',
 'hsu':'40146102','cai25':'39976940','lee26':'42692107','chou':'39491755','ramsey':'40788647','gonzalez':'42660856',
 'abbass25':'40015592','lieberman':'41217382','shahAJO':'42025665','jarrett':'41907810','klonoff':'39080859',
 'hong26':'41655764','alharbi':'41994958','silverii':'39563616','li26':'41587563','natividade':'40810985','liu':'41475544',
 'nogueira':'41498755','chrz':'42166479','abdelaal':'41692115','dhiv':'42060879','khani':'42612051','chenAPJO':'40962119',
 'lampsas':'42201355','anatriello':'42311413','sunNMA':'42768849','vilsboll26':'42049287','robertson':'42556433',
 'katz':'39883468','leeMech':'42335513','kakkar':'42259643','lakhaniBJO':'41807083','procacci':'40133108','lakhaniAJO':'40383360',
 'cheng':'41021211','castellana':'41509894','fisch':'42871459','suresh':'41026313',
 'marso':'27633186','vilsboll18':'29178519','bethel':'33444163','yoshida':'35817678','wang21':'34894326','kapoor23':'37454782',
 'avgerinos':'30058208','tang':'29369494','ortiz':'42612754','buckley':'40637847','wai':'38636788','linDOM24':'39030922',
 'eleft':'38584180','hasselstrom':'37078347','gaborit':'31589290','tauqeer':'39389007','douros':'30150234','barkmeier24':'38735641',
 'caiDR':'41192935','muayadDME':'39644923','shahOph':'41577258','zheng23':'36737746','talebi':'40334190','shenMR':'40830891',
 'igwe':'38031234','alwafi':'41488069','alburakDME':'42242293','yang26':'42380920','kapoor24':'39327045','polsky':'42452840',
 'niazi24':'38490274','muayad24':'39182626','chuang':'38250602','allan25':'39863057','vasu':'39978437','chenDOM26':'42259622',
 'hong25':'41360342','pan26':'42383218','amaral':'39732312','asif':'40509955','hallajIOP':'39237049','linCPT':'41074575','steel':'42872071',
 'shor':'40471562','hallajAMD':'42229850','cai26':'42229813','myers':'41453515','mclaughlin':'40712124','allanOR':'41197713',
 'joo':'41443408','panAJM':'42379510','chang26':'42186202','ahujaAMD':'41129133','alburakAMD':'42242290','sunEye':'42225822',
 'abbass26':'42898637','panOS25':'40206263','mohan':'40875223','lin25':'41456709','ahujaCat':'41130371','huang':'40750822',
 'eissa':'42839092','fan':'37893823','su22':'36136333','ottonelli':'41116973','song':'41776834','phutinart':'41973746','azzam':'39949069',
 'shabto':'39928352',
}
LIBRARY = {'hathaway','heberer','liu','dmr','allanOR','myers','joo','hallajAMD','muayadDME'}
MANUAL = {
 'dmr':{'cite':'Danesh-Meyer HV, Rizzo JF. GLP-1 receptor agonists and non-arteritic anterior ischaemic optic neuropathy: a critical appraisal. Clin Exp Ophthalmol 2026;54:554-64.','doi':'10.1111/ceo.70096'},
 'ema':{'cite':'European Medicines Agency, Pharmacovigilance Risk Assessment Committee. Semaglutide: NAION added as a very rare side effect (meeting highlights, June 2025).','url':'https://www.ema.europa.eu/en/news/meeting-highlights-pharmacovigilance-risk-assessment-committee-prac-2-5-june-2025'},
 'focus':{'cite':'FOCUS trial: semaglutide and diabetic retinopathy, ClinicalTrials.gov NCT03811561. No results published in PubMed as of 28 October 2026.','url':'https://clinicaltrials.gov/study/NCT03811561'},
}

S, M = 'study','meta'
NAION = [
 # diabetes cohorts
 ('hathaway','Semaglutide, diabetes, neuro-ophthalmology referrals',4.28,1.62,11.29,'Hazard ratio','Diabetes, cohort studies',S,'Other diabetes drugs. 17 against 6 events. Referral population, so absolute risks are not general.'),
 ('grauslund','Semaglutide, Denmark national register',2.19,1.54,3.12,'Hazard ratio','Diabetes, cohort studies',S,'0.228 against 0.093 per 1,000 person-years. Median time to NAION 22.2 months.'),
 ('simonsen','Semaglutide against SGLT2 inhibitor, Denmark and Norway',2.81,1.67,4.75,'Hazard ratio','Diabetes, cohort studies',S,'1.41 extra cases per 10,000 person-years.'),
 ('niazi26','Any GLP-1 drug, Danish case-control',2.13,1.43,3.18,'Rate ratio','Diabetes, cohort studies',S,'123 cases. No excess in the first 6 months (0.80); 3.63 at 6 to 12 months; 3.52 at 12 to 18 months.'),
 ('heberer','Semaglutide against SGLT2 inhibitor, US Veterans',2.33,1.53,3.54,'Hazard ratio','Diabetes, cohort studies',S,'123 against 67 per 100,000 person-years. Curves separate from about 6 months.'),
 ('noh','Against DPP-4 inhibitor, UK primary care, 1 year',2.56,1.44,4.86,'Risk ratio','Diabetes, cohort studies',S,'18.5 against 7.2 per 100,000. Higher in the first 6 months, under 50, men, smokers, and with an HbA1c fall of 1% or more.'),
 ('hsu','Semaglutide, global records network, 2 years',2.39,1.37,4.18,'Hazard ratio','Diabetes, cohort studies',S,'1 year 1.94 (0.93 to 4.02), not significant.'),
 ('tesfaye','Against SGLT2 inhibitor, three US insurance databases',1.85,1.51,2.27,'Hazard ratio','Diabetes, cohort studies',S,'482,912 matched pairs. 0.29 extra cases per 1,000 person-years.'),
 ('wang25','Semaglutide or tirzepatide, US records, 2 years',1.76,1.01,3.07,'Hazard ratio','Diabetes, cohort studies',S,'35 (0.04%) against 19 (0.02%) events.'),
 ('ueda','Against SGLT2 inhibitor, Sweden, 5 years',1.69,0.95,3.01,'Risk ratio','Diabetes, cohort studies',S,'0.12% against 0.07%. Restricted to metformin users 1.23 (0.65 to 2.33).'),
 ('klonoff','Semaglutide, US records',1.45,0.51,4.17,'Hazard ratio','Diabetes, cohort studies',S,'Research letter.'),
 ('cai25','Semaglutide against empagliflozin, 14 databases',1.44,0.78,2.68,'Hazard ratio','Diabetes, cohort studies',S,'37 million people with diabetes. 14.5 per 100,000 person-years on semaglutide.'),
 ('cai25','Same data, self-controlled case series',1.32,1.14,1.54,'Rate ratio','Diabetes, cohort studies',S,'Each person compared with themselves, which removes fixed confounders.'),
 ('chenDM','Against other diabetes drugs, global records network',1.38,1.23,1.55,'Hazard ratio','Diabetes, cohort studies',S,'0.21% against 0.17%. Against SGLT2 inhibitors 1.30 (1.11 to 1.52).'),
 ('choi','Against SGLT2 inhibitor, US Veterans, 3 years',1.35,1.11,1.51,'Risk ratio','Diabetes, cohort studies',S,'39.1 against 29.3 per 10,000. Diagnosis code checked against charts: 84.7% correct.'),
 ('lee26','Against SGLT2 or DPP-4 inhibitor, US claims',1.86,0.84,4.09,'Hazard ratio','Diabetes, cohort studies',S,'26 events in total.'),
 ('chou','Semaglutide, diabetes alone, 3 years',1.51,0.71,3.25,'Hazard ratio','Diabetes, cohort studies',S,''),
 ('ramsey','Global records network, 2 years',1.26,0.94,1.70,'Hazard ratio','Diabetes, cohort studies',S,''),
 ('gonzalez','Against DPP-4 inhibitor',1.11,0.96,1.29,'Odds ratio','Diabetes, cohort studies',S,''),
 ('jarrett','Ischaemic optic neuropathy, 5 years',0.98,0.79,1.21,'Hazard ratio','Diabetes, cohort studies',S,'People with diabetes and cardiovascular risk factors.'),
 ('shahAJO','People who already have diabetic retinopathy',0.88,0.54,1.44,'Hazard ratio','Diabetes, cohort studies',S,''),
 ('abbass25','Semaglutide, 5 years',0.70,0.52,0.94,'Risk ratio','Diabetes, cohort studies',S,'Any GLP-1 drug 0.89 (0.74 to 1.07).'),
 ('lieberman','Semaglutide, US military health system',0.36,0.25,0.51,'Odds ratio','Diabetes, cohort studies',S,'An outlier in the protective direction.'),
 # obesity
 ('hathaway','Semaglutide, obesity, referral clinic',7.64,2.21,26.36,'Hazard ratio','Obesity without diabetes',S,'20 against 3 events.'),
 ('chou','Semaglutide, obesity alone, 3 years',0.72,0.24,2.16,'Hazard ratio','Obesity without diabetes',S,''),
 ('lieberman','Semaglutide, obesity',0.10,0.01,1.35,'Odds ratio','Obesity without diabetes',S,''),
 # special comparisons
 ('hong26','Tirzepatide against other GLP-1 drugs',0.45,0.27,0.86,'Hazard ratio','Drug against drug, or special groups',S,'Suggests less NAION on tirzepatide than on semaglutide or similar drugs.'),
 ('alharbi','People with idiopathic intracranial hypertension',0.47,0.24,0.93,'Hazard ratio','Drug against drug, or special groups',S,'Optic atrophy 0.78 (0.64 to 0.94).'),
 # trials
 ('liu','Trials in diabetes',1.76,0.43,7.25,'Risk ratio','Randomised trials, pooled',M,'5 against 1 events.'),
 ('liu','Trials in weight loss',2.18,0.33,14.34,'Risk ratio','Randomised trials, pooled',M,''),
 ('silverii','69 trials',1.53,0.53,4.44,'Odds ratio','Randomised trials, pooled',M,'8 against 4 events. 5.6 against 3.0 per 100,000 person-years.'),
 ('li26','20 trials, ischaemic optic neuropathy',1.50,0.49,4.63,'Odds ratio','Randomised trials, pooled',M,'240,334 person-years.'),
 ('nogueira','8 trials',2.36,0.85,6.53,'Odds ratio','Randomised trials, pooled',M,''),
 ('natividade','78 trials',3.92,1.02,15.02,'Peto odds ratio','Randomised trials, pooled',M,'All eye disorders 1.01 (0.91 to 1.12).'),
 # meta-analyses
 ('liu','Observational studies, diabetes',1.85,1.20,2.85,'Hazard ratio','Meta-analyses of observational studies',M,'26.7 against 18.9 per 100,000 person-years. Weight-loss studies 1.57 (0.69 to 3.59).'),
 ('chrz','5 studies, diabetes',2.17,1.73,2.74,'Hazard ratio','Meta-analyses of observational studies',M,'About 1 extra case per 7,000 people per year.'),
 ('nogueira','Non-randomised studies',1.64,1.15,2.35,'Odds ratio','Meta-analyses of observational studies',M,'Number needed to harm about 2,700.'),
 ('abdelaal','6 studies, adjusted',1.63,0.88,2.39,'Hazard ratio','Meta-analyses of observational studies',M,'Diabetes 1.70 (1.10 to 2.64); obesity 0.47 (0.19 to 1.13).'),
 ('khani','8 studies, semaglutide',1.93,1.22,3.08,'Risk ratio','Meta-analyses of observational studies',M,'Obesity 1.68 (0.72 to 3.91).'),
 ('dhiv','5 studies, semaglutide',2.52,1.56,4.72,'Risk ratio','Meta-analyses of observational studies',M,'Bayesian credible interval.'),
 ('chenAPJO','10 studies, semaglutide',2.62,1.81,3.80,'Hazard ratio','Meta-analyses of observational studies',M,'Significant only after 2 years of use.'),
 ('sunNMA','Network analysis, semaglutide',1.54,1.31,1.82,'Hazard ratio','Meta-analyses of observational studies',M,'Liraglutide 1.25 (1.08 to 1.45).'),
 ('anatriello','28 studies in diabetes',1.01,0.62,1.64,'Risk ratio','Meta-analyses of observational studies',M,''),
]
TIMING = [
 ('niazi26','First 6 months of use',0.80,0.32,2.05,'Rate ratio','Danish case-control',S,''),
 ('niazi26','6 to 12 months',3.63,2.06,6.40,'Rate ratio','Danish case-control',S,''),
 ('niazi26','12 to 18 months',3.52,1.73,7.17,'Rate ratio','Danish case-control',S,''),
 ('hsu','1 year',1.94,0.93,4.02,'Hazard ratio','US records, semaglutide',S,''),
 ('hsu','2 years',2.39,1.37,4.18,'Hazard ratio','US records, semaglutide',S,''),
 ('hsu','3 years',2.44,1.44,4.12,'Hazard ratio','US records, semaglutide',S,''),
 ('hsu','4 years',2.05,1.26,3.34,'Hazard ratio','US records, semaglutide',S,''),
 ('lampsas','1 year',3.36,1.44,7.84,'Hazard ratio','Meta-analysis of 8 cohorts',M,''),
 ('lampsas','2 years',2.37,1.46,3.85,'Hazard ratio','Meta-analysis of 8 cohorts',M,''),
 ('lampsas','3 years',2.37,1.45,3.87,'Hazard ratio','Meta-analysis of 8 cohorts',M,''),
]
DR = [
 ('marso','SUSTAIN-6, semaglutide, retinopathy complications',1.76,1.11,2.78,'Hazard ratio','Randomised trials',S,'50 against 29 events (3.0% against 1.8%). Excess mostly in people with existing retinopathy and a large, fast HbA1c fall.'),
 ('wang21','Semaglutide against placebo, 23 trials',1.24,1.03,1.50,'Risk ratio','Randomised trials',M,'All comparators 1.14 (0.98 to 1.33).'),
 ('yoshida','4 cardiovascular outcome trials',1.23,1.05,1.44,'Odds ratio','Randomised trials',M,'Rapidly worsening retinopathy.'),
 ('kapoor23','93 trials, early retinopathy',1.31,1.01,1.68,'Risk ratio','Randomised trials',M,'Driven by albiglutide.'),
 ('bethel','6 cardiovascular outcome trials',1.10,0.93,1.30,'Odds ratio','Randomised trials',M,'Greater HbA1c fall predicted more retinopathy events (meta-regression).'),
 ('tang','Network analysis of trials',1.19,0.94,1.52,'Odds ratio','Randomised trials',M,''),
 ('natividade','78 trials',1.04,0.92,1.17,'Odds ratio','Randomised trials',M,''),
 ('avgerinos','60 trials, vitreous haemorrhage',1.93,1.09,3.42,'Odds ratio','Randomised trials',M,'No increase in retinopathy, macular oedema or detachment.'),
 ('buckley','Tirzepatide, new proliferative retinopathy, UK',2.15,1.24,3.74,'Odds ratio','Observational, higher risk',S,'1.1% against 0.5%. Mainly in people who already had retinopathy. New retinopathy of any grade was lower, 0.73 (0.62 to 0.86).'),
 ('linDOM24','Existing retinopathy, against SGLT2 inhibitor, Taiwan',1.50,1.01,2.23,'Hazard ratio','Observational, higher risk',S,'Mainly tractional detachment. No difference without baseline retinopathy.'),
 ('hasselstrom','Against DPP-4 inhibitor, Denmark',1.46,1.09,1.96,'Hazard ratio','Observational, higher risk',S,''),
 ('eleft','Insulin users, any retinopathy',1.31,1.26,1.36,'Hazard ratio','Observational, higher risk',S,'Macular oedema 1.01 (0.96 to 1.07).'),
 ('wai','Proliferative disease, against SGLT2 inhibitor, 3 years',1.28,1.10,1.50,'Risk ratio','Observational, higher risk',S,'Macular oedema 1.29 (1.21 to 1.38).'),
 ('gonzalez','Non-sight-threatening retinopathy, against DPP-4 inhibitor',1.12,1.09,1.15,'Odds ratio','Observational, higher risk',S,'Sight-threatening disease 1.09 (1.03 to 1.16).'),
 ('ramsey','New retinopathy, 2 years',1.07,1.03,1.11,'Hazard ratio','Observational, higher risk',S,'In existing retinopathy, vitreous haemorrhage 0.74, neovascular glaucoma 0.78, blindness 0.77.'),
 ('gaborit','AngioSafe, severe retinopathy',1.14,0.80,1.62,'Odds ratio','Observational, no clear effect',S,''),
 ('barkmeier24','Treated sight-threatening retinopathy, against DPP-4 inhibitor',1.07,0.85,1.35,'Hazard ratio','Observational, no clear effect',S,'5-year risk 1.0% on GLP-1 drugs, 0.7% on SGLT2 inhibitors.'),
 ('tauqeer','Vision-threatening retinopathy',1.02,0.92,1.14,'Hazard ratio','Observational, no clear effect',S,''),
 ('douros','UK primary care',1.00,0.85,1.17,'Hazard ratio','Observational, no clear effect',S,'Against insulin 0.67.'),
 ('caiDR','Semaglutide, proliferative disease, against empagliflozin',0.83,0.53,1.30,'Hazard ratio','Observational, no clear effect',S,''),
 ('hong26','Tirzepatide against other GLP-1 drugs',0.79,0.72,0.87,'Hazard ratio','Observational, lower risk',S,''),
 ('muayadDME','New macular oedema, 2 years',0.77,0.70,0.85,'Hazard ratio','Observational, lower risk',S,''),
 ('shahOph','Tirzepatide, proliferative disease',0.71,0.56,0.88,'Risk ratio','Observational, lower risk',S,'Macular oedema 0.62 (0.54 to 0.73).'),
 ('shenMR','Genetic (Mendelian randomisation) study',0.59,0.39,0.89,'Odds ratio','Observational, lower risk',S,''),
 ('zheng23','Sweden',0.42,0.29,0.61,'Hazard ratio','Observational, lower risk',S,''),
 ('talebi','Against never-users',0.31,0.26,0.37,'Hazard ratio','Observational, lower risk',S,'Design prone to immortal-time bias.'),
 ('alburakDME','Macular oedema, against SGLT2 inhibitor',1.50,1.17,1.94,'Hazard ratio','Meta-analyses of observational studies',M,'Against mixed comparators 0.81 (0.52 to 1.26). Very low certainty.'),
 ('yang26','Progression',1.07,0.90,1.28,'Risk ratio','Meta-analyses of observational studies',M,''),
 ('alwafi','23 studies',1.00,0.71,1.43,'Risk ratio','Meta-analyses of observational studies',M,'Trials alone 0.91 (0.73 to 1.14).'),
 ('anatriello','New retinopathy',0.96,0.85,1.08,'Risk ratio','Meta-analyses of observational studies',M,'Progression 0.97 (0.83 to 1.14).'),
 ('igwe','Observational studies',0.87,0.56,1.34,'Risk ratio','Meta-analyses of observational studies',M,''),
 ('kapoor24','Against insulin',0.66,0.48,0.91,'Risk ratio','Meta-analyses of observational studies',M,'Against oral drugs, retinopathy complications 1.39 (1.07 to 1.80).'),
]
GLAU = [
 ('niazi24','Glaucoma, Danish case-control',0.81,0.70,0.94,'Rate ratio','Diabetes',S,'1,737 cases. Beyond 3 years of use 0.71 (0.55 to 0.91).'),
 ('chuang','Open-angle glaucoma, Taiwan',0.71,0.53,0.94,'Hazard ratio','Diabetes',S,''),
 ('allan25','Primary open-angle glaucoma, against insulin',0.58,0.45,0.76,'Hazard ratio','Diabetes',S,'Over 60, 5 years of eye follow-up.'),
 ('muayad24','Primary open-angle glaucoma, against metformin, 2 years',0.50,0.32,0.78,'Risk ratio','Diabetes',S,'Ocular hypertension at 1 year 0.44 (0.31 to 0.62).'),
 ('vasu','Primary open-angle glaucoma, 5 years',0.42,0.32,0.55,'Risk ratio','Obesity without diabetes',S,'Against other weight-loss drugs.'),
 ('vasu','Ocular hypertension, 5 years',0.34,0.25,0.47,'Risk ratio','Obesity without diabetes',S,''),
 ('chenDOM26','Primary open-angle glaucoma, 5 years',0.50,0.32,0.78,'Risk ratio','Obesity without diabetes',S,'Ocular hypertension 0.56 (0.34 to 0.91).'),
 ('pan26','Tirzepatide against other GLP-1 drugs, over 60',0.65,0.44,0.96,'Hazard ratio','Tirzepatide against other GLP-1 drugs',S,''),
 ('hong25','Tirzepatide against other GLP-1 drugs',0.50,0.34,0.74,'Risk ratio','Tirzepatide against other GLP-1 drugs',S,'Ocular hypertension 0.59 (0.40 to 0.88); glaucoma treatment 0.54.'),
 ('anatriello','Glaucoma',0.84,0.71,1.00,'Hazard ratio','Meta-analyses',M,''),
 ('amaral','5 studies',0.78,0.59,1.04,'Hazard ratio','Meta-analyses',M,'0.71 (0.60 to 0.85) without one outlying study.'),
 ('asif','5 studies',0.78,0.60,1.02,'Odds ratio','Meta-analyses',M,''),
]
AMD = [
 ('shor','Ontario, 66 and over, diabetes',2.21,1.65,2.96,'Hazard ratio','Neovascular (wet) AMD',S,'0.2% against 0.1%. The only study with a clear increase.'),
 ('hallajAMD','US records, 2.8 million per group',1.00,0.97,1.04,'Hazard ratio','Neovascular (wet) AMD',S,'Any AMD 0.84 (0.83 to 0.86).'),
 ('cai26','Semaglutide against empagliflozin, 12 databases',0.98,0.54,1.79,'Hazard ratio','Neovascular (wet) AMD',S,'Self-controlled analysis 0.92 (0.67 to 1.26).'),
 ('mclaughlin','Progression to wet AMD',0.73,0.60,0.88,'Risk ratio','Neovascular (wet) AMD',S,''),
 ('allan25','Wet AMD against insulin',0.70,0.58,0.84,'Hazard ratio','Neovascular (wet) AMD',S,''),
 ('myers','Wet AMD, no diabetes',0.63,0.30,1.32,'Hazard ratio','Neovascular (wet) AMD',S,''),
 ('hallajAMD','Any AMD',0.84,0.83,0.86,'Hazard ratio','Dry or any AMD',S,''),
 ('mclaughlin','Dry AMD',0.85,0.80,0.91,'Risk ratio','Dry or any AMD',S,'Progression to advanced dry AMD 0.72 (0.53 to 0.97).'),
 ('panAJM','Any AMD, against metformin',0.83,0.75,0.91,'Hazard ratio','Dry or any AMD',S,'Obesity 0.77 (0.61 to 0.98).'),
 ('chang26','Obesity, over 60, target trial emulation',0.82,0.68,0.98,'Hazard ratio','Dry or any AMD',S,''),
 ('allanOR','Dry AMD, 3 years',0.77,0.66,0.91,'Hazard ratio','Dry or any AMD',S,'No effect on conversion from dry to wet.'),
 ('allan25','Dry AMD against metformin',0.68,0.56,0.84,'Hazard ratio','Dry or any AMD',S,''),
 ('myers','Dry AMD, no diabetes',0.47,0.28,0.78,'Hazard ratio','Dry or any AMD',S,'Negative control outcomes were null.'),
 ('joo','Dry AMD, against insulin',0.45,0.27,0.76,'Hazard ratio','Dry or any AMD',S,'Against metformin and SGLT2 inhibitors the effect disappeared after matching. 35 to 43% of coded AMD was wrong on chart review.'),
 ('chenDOM26','AMD, obesity, over 60',0.33,0.23,0.48,'Risk ratio','Dry or any AMD',S,''),
 ('ahujaAMD','Dry AMD, 5 years',0.16,0.10,0.28,'Risk ratio','Dry or any AMD',S,'Implausibly large effect for a drug of this kind.'),
]
OTHER = [
 ('abbass26','Any retinal vein or artery occlusion, 3 years',0.71,0.59,0.86,'Hazard ratio','Retinal vascular occlusion',S,''),
 ('panOS25','Retinal vein occlusion, against DPP-4 inhibitor',0.73,0.54,0.98,'Hazard ratio','Retinal vascular occlusion',S,'Branch vein occlusion 0.62.'),
 ('shahAJO','Vein occlusion, people with retinopathy',0.70,0.61,0.80,'Hazard ratio','Retinal vascular occlusion',S,'Artery occlusion 0.85 (0.57 to 1.26).'),
 ('mohan','Uveitis, all comparators',0.48,0.46,0.51,'Risk ratio','Uveitis',S,'Against metformin 0.58, against insulin 0.57.'),
 ('mohan','Uveitis, against SGLT2 inhibitor',1.17,1.04,1.32,'Risk ratio','Uveitis',S,'Reverses direction against this comparator.'),
 ('lin25','Cataract, added to metformin',0.93,0.87,0.99,'Hazard ratio','Cataract',S,'Cataract surgery 1.01 (0.79 to 1.26).'),
 ('huang','Tirzepatide against naltrexone-bupropion',0.46,0.23,0.92,'Hazard ratio','Cataract',S,''),
 ('chenDOM26','Obesity, over 60',0.45,0.40,0.50,'Risk ratio','Cataract',S,''),
 ('ahujaCat','Obesity, against other weight-loss drugs',0.28,0.25,0.31,'Risk ratio','Cataract',S,'Implausible: the comparator group itself had twice the cataract rate of untreated people.'),
 ('su22','Dry eye, against SGLT2 inhibitor',1.28,1.12,1.47,'Hazard ratio','Dry eye and ocular surface',S,'Inverted from the published 0.78 (SGLT2 against GLP-1). 11.5 against 9.0 per 1,000 person-years.'),
 ('fan','Dry eye, Taiwan',0.85,0.67,0.99,'Hazard ratio','Dry eye and ocular surface',S,'Superficial keratitis 0.67.'),
 ('chenDOM26','Dry eye, obesity',0.36,0.31,0.42,'Risk ratio','Dry eye and ocular surface',S,''),
 ('phutinart','Papilloedema, network analysis',0.47,0.34,0.65,'Risk ratio','Idiopathic intracranial hypertension',M,''),
 ('song','Papilloedema',0.40,0.22,0.72,'Risk ratio','Idiopathic intracranial hypertension',M,'Visual disturbance or blindness 0.51.'),
 ('azzam','Tirzepatide, papilloedema',0.32,0.19,0.54,'Risk ratio','Idiopathic intracranial hypertension',S,'193 per group.'),
 ('gonzalez','Blindness, against DPP-4 inhibitor',1.04,0.97,1.11,'Odds ratio','Neovascular glaucoma and blindness',S,''),
 ('ramsey','Neovascular glaucoma, existing retinopathy',0.78,0.68,0.88,'Hazard ratio','Neovascular glaucoma and blindness',S,'Blindness 0.77 (0.73 to 0.82).'),
 ('jarrett','Legal blindness, 5 years',0.67,0.58,0.77,'Hazard ratio','Neovascular glaucoma and blindness',S,''),
 ('shahAJO','Neovascular glaucoma, people with retinopathy',0.65,0.47,0.89,'Hazard ratio','Neovascular glaucoma and blindness',S,''),
]
PV = [  # pharmacovigilance: key, database, drug, ROR, lo, hi, note
 ('kakkar','FAERS (US)','Semaglutide',94.5,None,None,'355 reports. Tirzepatide 2.94, liraglutide 4.58. No signal for dulaglutide, exenatide or lixisenatide.'),
 ('lakhaniBJO','FAERS (US)','Wegovy (weight-loss dose)',74.9,None,None,'Ozempic (diabetes dose) 18.8. Men had 3.3 times the odds of a report.'),
 ('lakhaniAJO','VigiBase (WHO)','Semaglutide',68.6,None,None,'FAERS 11.1 (8.2 to 15.2). Against metformin.'),
 ('cheng','VigiBase (WHO)','Semaglutide',40.2,None,None,'FAERS 31.5.'),
 ('procacci','FAERS (US)','Semaglutide',17.6,13.9,21.9,'Median onset 186 days. 18 of 53 recent reports from Denmark.'),
 ('fisch','FAERS (US)','Semaglutide, ischaemic optic neuropathy',4.42,1.41,13.87,''),
 ('castellana','FAERS (US)','Tirzepatide',2.60,1.78,3.80,'28 cases.'),
 ('suresh','VigiBase (WHO)','Semaglutide',None,None,None,'91 reports, 42% from Denmark, where the first cohort study was published.'),
]

# Event rates per 100,000 people per year, where the abstract or full text reports them.
# (key, label) -> (on drug, comparator, extra, how derived). None = not reported.
RATES = {
 ('hathaway','Semaglutide, diabetes, neuro-ophthalmology referrals'):(2970,600,None,'36-month cumulative incidence 8.9% against 1.8%, divided by 3'),
 ('hathaway','Semaglutide, obesity, referral clinic'):(2230,270,None,'36-month cumulative incidence 6.7% against 0.8%, divided by 3'),
 ('grauslund','Semaglutide, Denmark national register'):(22.8,9.3,None,'reported incidence rate'),
 ('simonsen','Semaglutide against SGLT2 inhibitor, Denmark and Norway'):(21.9,11.8,14.1,'Danish crude rates; extra is the adjusted pooled rate difference'),
 ('heberer','Semaglutide against SGLT2 inhibitor, US Veterans'):(123,67,None,'reported incidence rate'),
 ('noh','Against DPP-4 inhibitor, UK primary care, 1 year'):(18.5,7.2,None,'1-year risk'),
 ('tesfaye','Against SGLT2 inhibitor, three US insurance databases'):(None,None,29,'reported rate difference 0.29 per 1,000 person-years'),
 ('wang25','Semaglutide or tirzepatide, US records, 2 years'):(22,12,None,'2-year risk 35 and 19 of 79,699, divided by 2'),
 ('ueda','Against SGLT2 inhibitor, Sweden, 5 years'):(24,14,None,'5-year risk 0.12% against 0.07%, divided by 5'),
 ('cai25','Semaglutide against empagliflozin, 14 databases'):(14.5,None,None,'reported rate on semaglutide'),
 ('cai25','Same data, self-controlled case series'):(14.5,None,None,'reported rate on semaglutide'),
 ('choi','Against SGLT2 inhibitor, US Veterans, 3 years'):(130,98,None,'3-year risk 39.1 against 29.3 per 10,000, divided by 3'),
 ('abbass25','Semaglutide, 5 years'):(13,None,None,'5-year cumulative risk 0.065%, divided by 5'),
 ('silverii','69 trials'):(5.6,3.0,None,'reported rate'),
 ('liu','Observational studies, diabetes'):(26.7,18.9,None,'reported pooled rate'),
 ('chrz','5 studies, diabetes'):(None,None,14,'reported absolute excess 0.014% per year'),
 ('marso','SUSTAIN-6, semaglutide, retinopathy complications'):(1430,860,None,'3.0% against 1.8% over a median 2.1 years'),
 ('barkmeier24','Treated sight-threatening retinopathy, against DPP-4 inhibitor'):(200,180,None,'5-year probability 1.0% against 0.9%, divided by 5'),
 ('zheng23','Sweden'):(597,1285,None,'reported incidence rate'),
 ('hallajAMD','Any AMD'):(185,256,None,'5-year cumulative incidence 0.924% against 1.278%, divided by 5'),
 ('su22','Dry eye, against SGLT2 inhibitor'):(1150,900,None,'reported incidence rate'),
}

# Absolute-rate plot: (key, label, outcome group, on drug, comparator, extra, how derived), per 100,000 per year.
OUTCOME_OF = {'marso':'Diabetic retinopathy','barkmeier24':'Diabetic retinopathy','zheng23':'Diabetic retinopathy','hallajAMD':'Macular degeneration','su22':'Dry eye'}
SHORTLAB = {
 ('hathaway','Semaglutide, diabetes, neuro-ophthalmology referrals'):'Referral clinic, diabetes',
 ('hathaway','Semaglutide, obesity, referral clinic'):'Referral clinic, obesity',
 ('simonsen','Semaglutide against SGLT2 inhibitor, Denmark and Norway'):'Denmark and Norway, against SGLT2 inhibitor',
 ('cai25','Semaglutide against empagliflozin, 14 databases'):'14 US databases, semaglutide users',
}
SKIP = {('cai25','Same data, self-controlled case series')}
EXTRA_RATES = [
 ('reynolds','US, age 18 to 65, against SGLT2 inhibitor','NAION',56.7,36.7,None,'18-month risk 8.5 against 5.5 per 10,000, divided by 1.5'),
 ('reynolds','US, age 18 to 65, against DPP-4 inhibitor','NAION',52,28,None,'18-month risk 7.8 against 4.2 per 10,000, divided by 1.5'),
 ('vilsboll26','Pooled placebo-controlled trials, confirmed cases','NAION',3,6,None,'reported rate, about 3 against about 6'),
]
def rate_rows():
    out=[]
    for R in (NAION,DR,AMD,OTHER):
        for r in R:
            q=RATES.get((r[0],r[1]))
            if not q or (r[0],r[1]) in SKIP: continue
            out.append((r[0],SHORTLAB.get((r[0],r[1]),r[1]),OUTCOME_OF.get(r[0],'NAION'),q[0],q[1],q[2],q[3],STYPE.get(r[6],r[6])))
    ex=[e+(('Randomised trials, pooled' if e[0]=='vilsboll26' else 'Cohort studies in diabetes'),) for e in EXTRA_RATES]
    nai=[o for o in out if o[2]=='NAION']+ex
    order=['Cohort studies in diabetes','Cohort studies in obesity without diabetes','Randomised trials, pooled','Meta-analyses of observational studies']
    nai.sort(key=lambda o:order.index(o[7]) if o[7] in order else 9)
    return nai+[o for o in out if o[2]!='NAION']
STYPE={'Diabetes, cohort studies':'Cohort studies in diabetes','Obesity without diabetes':'Cohort studies in obesity without diabetes'}
