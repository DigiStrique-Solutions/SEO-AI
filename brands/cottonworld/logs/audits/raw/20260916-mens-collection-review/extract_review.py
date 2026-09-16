from crawl import *
pages=json.loads((ROOT/'pages.json').read_text(encoding='utf-8'))
targets=set()
for p in pages:
    if 'html_file' not in p: continue
    s=BeautifulSoup((ROOT/p['html_file']).read_text(encoding='utf-8'),'html.parser')
    b=s.select_one('.cw-collection-read-more__body')
    p['copy']=b.get_text('\n',strip=True) if b else ''
    p['copy_links']=[{'text':a.get_text(' ',strip=True),'url':urljoin(p['url'],a['href'])} for a in b.select('a[href]')] if b else []
    p['copy_headings']=[{'tag':h.name,'text':h.get_text(' ',strip=True)} for h in b.select('h1,h2,h3,h4')] if b else []
    targets.update(x['url'] for x in p['copy_links'])
(ROOT/'pages.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf-8')
known={p['url']:p for p in pages}
with ThreadPoolExecutor(max_workers=6) as ex:
    checks=list(ex.map(fetch,sorted(targets-set(known))))
checks += [known[u] for u in targets if u in known]
(ROOT/'destination-checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
for p in pages:
    print(json.dumps({'url':p['url'],'copy_words':len(p.get('copy','').split()),'copy_links':p.get('copy_links'),'copy_headings':p.get('copy_headings')},ensure_ascii=True))
print('DESTINATION CHECKS')
for p in checks: print(json.dumps({k:p.get(k) for k in ['url','status','final_url','h1','error']},ensure_ascii=True))
