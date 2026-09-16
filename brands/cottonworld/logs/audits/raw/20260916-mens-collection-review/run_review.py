from crawl import *
nav=json.loads((ROOT/'navigation.json').read_text(encoding='utf-8'))
urls=[]
for x in nav:
    if x['url'].endswith('/women-new-arrivals'): break
    if x['url'] not in urls: urls.append(x['url'])
landing=json.loads((ROOT/'landing.json').read_text(encoding='utf-8'))
urls+= [x['url'] for x in landing['links'] if '/collections/' in x['url'] and '/products/' not in x['url']]
sheet=json.loads((ROOT/'reference-sheet.json').read_text(encoding='utf-8'))['structuredContent']['values']
urls += [x[7].strip() for x in sheet if len(x)>7 and x[1]=='Men' and x[7] and '/women' not in x[7]]
urls=list(dict.fromkeys(urls))
with ThreadPoolExecutor(max_workers=6) as ex: pages=list(ex.map(fetch,urls))
(ROOT/'pages.json').write_text(json.dumps(pages,indent=2,ensure_ascii=False),encoding='utf-8')
for p in pages:
    print(json.dumps({'url':p['url'],'status':p.get('status'),'h1':p.get('h1'),'blocks':p.get('blocks'), 'error':p.get('error')},ensure_ascii=True))
