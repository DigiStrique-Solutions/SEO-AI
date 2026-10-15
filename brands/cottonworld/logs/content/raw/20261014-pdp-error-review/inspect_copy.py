import collections, html, json, re, sys
from pathlib import Path
ROOT = Path(__file__).parent
cells = json.loads((ROOT/'before-cells.json').read_text(encoding='utf-8'))['sheets'][0]['data'][0]['rowData']
prior = {x['row']:x for x in json.loads((ROOT.parent/'20261009-pdp-intro-variation/revised.json').read_text(encoding='utf-8'))}
records = {x['row']:x for x in json.loads((ROOT.parent/'20261006-added-active-pdp/records.json').read_text(encoding='utf-8'))}
current = []
for row,c in enumerate(cells[1:],2):
    vals=[v.get('userEnteredValue',{}).get('stringValue','') for v in c['values']]
    old=prior[row]
    current.append(dict(old,after=vals[2],original_url=vals[0],url=vals[1]))
(ROOT/'current.json').write_text(json.dumps(current,ensure_ascii=False,indent=2),encoding='utf-8')
mode=sys.argv[1] if len(sys.argv)>1 else 'summary'
if mode=='summary':
    changed=[x['row'] for x in current if x['after']!=prior[x['row']]['after']]
    print('CURRENT_CHANGED_FROM_LAST_RUN',changed)
    for i in range(4):
        c=collections.Counter(x['after'].split('\n\n')[i] for x in current)
        print('PARA',i,'unique',len(c),'most common',c.most_common(3))
    print('SURFACE SENTENCES')
    print('\n'.join(f'{n}: {s}' for s,n in collections.Counter(x['after'].split('\n\n')[0].split('. ')[-1] for x in current).most_common()))
elif mode=='rows':
    lo,hi=map(int,sys.argv[2:4])
    for x in current:
        if not lo<=x['row']<=hi:continue
        p=x['after'].split('\n\n')
        print(x['row'],x['code'],'|',p[0].split('. ')[0],'|',re.split(r'Machine wash|Hand wash',p[1])[0],'| SRC',json.dumps(x['facts']['attr']))
elif mode=='styles':
    for s,rows in sorted(((s,[x['row'] for x in current if x['after'].split('\n\n')[2]==s]) for s in set(x['after'].split('\n\n')[2] for x in current)),key=lambda x:x[1][0]):
        print(rows, s)
