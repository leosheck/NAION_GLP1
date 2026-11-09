# GLP-1 drugs and NAION

Interactive page on the risk of non-arteritic anterior ischaemic optic neuropathy (NAION) with GLP-1 receptor agonists such as semaglutide and tirzepatide. It shows every published estimate (cohort studies, randomised trials and meta-analyses) with 95% confidence intervals, the absolute yearly rates where reported, and a numbered source for every figure. Literature to 28 October 2026.

Live page: https://leosheck.github.io/NAION_GLP1/

- `index.html`: the page, self-contained (data embedded).
- `data.json`: the study estimates, absolute rates and references used by the page.
- `search-log.md`: library and PubMed search log for the wider GLP-1 and eye review this page was taken from.
- `src/`: build files. `data_rows.py` holds every extracted estimate, `pubmed_metadata.json` the citation details, and `build_page.py` fills `template_naion.html`. The script carries the file paths of the environment it was written in, and they need editing before rerunning.

Compiled for Leo Sheck, Retina Specialists, Auckland.
