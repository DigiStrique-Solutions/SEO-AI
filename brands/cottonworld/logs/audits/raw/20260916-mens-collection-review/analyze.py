from crawl import *
from collections import Counter
pages=json.loads((ROOT/'pages.json').read_text(encoding='utf-8'))
checks=json.loads((ROOT/'destination-checks.json').read_text(encoding='utf-8'))
byurl={x['url']:x for x in pages+checks}
fixmap={'mens-pants':'mens-pants-2','mens-jackets':'men-jackets','mens-linen-shirts':'men-linen-shirts','mens-polos':'polo-collar'}
rows=[]
for p in pages:
    for n,a in enumerate(p.get('copy_links',[]),1):
        u=a['url']; h=urlsplit(u); handle=h.path.rsplit('/',1)[-1]
        category=None; replacement=None
        if h.netloc.endswith('shopifypreview.com'): category='broken_preview'; replacement=BASE+'/collections/best-sellers-mens'
        elif handle in fixmap: category='broken_collection'; replacement=BASE+'/collections/'+('mens-cotton-pants' if a['text']=="Men's Cotton Pants" else fixmap[handle])
        elif h.path=='/search':
            category='search_instead_of_collection'
            replacement=BASE+'/collections/'+('polo-collar' if 'polo' in h.query else 'mens-chinos' if 'chino' in h.query else 'men-linen-shirts')
        elif a['text']=='Organic Cotton Collection': category='wrong_collection'; replacement=BASE+'/collections/cotton-mens'
        elif handle=='mens-joggers': category='empty_collection'
        r={'source':p['url'],'occurrence':n,'anchor':a['text'],'current_url':u,'http_status':byurl.get(u,{}).get('status'),'category':category or 'no_link_issue_found','status':'fail' if category else 'pass','replacement':replacement,'replacement_status':byurl.get(replacement,{}).get('status'),'severity':'high' if category in ['broken_preview','broken_collection'] else 'medium' if category else None,'owner':'Shopify content editor' if category!='empty_collection' else 'Merchandising','confidence':'high','evidence_ref':'pages.json + destination-checks.json'}
        rows.append(r)
result={'run_id':'20260916-mens-collection-review','date':'2026-09-16','scope':'Landing page, men-specific navigation collections and additional men collection URLs in supplied Active Collections sheet; first collection page and its complete Read More body, excluding product detail pages and pagination product copy.','pages_checked':len(pages),'pages_with_copy':sum(bool(p.get('copy')) for p in pages),'link_occurrences':len(rows),'counts':dict(Counter(r['category'] for r in rows)),'rows':rows}
(ROOT/'link-findings.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
for p in pages:
    rr=[r for r in rows if r['source']==p['url']]
    print(urlsplit(p['url']).path, len(p.get('copy','').split()), dict(Counter(r['category'] for r in rr)))
print('TEXT ERRORS')
for p in pages:
    if p.get('copy'):
        for line in p['copy'].splitlines():
            if re.search(r'\bMens\b|Men.sT|\ba matching\b|a tucked-in|\bit shows|time you just|fabrics think|fibers think|Online[ “-]|”most|our.*Polo.*combine',line): print(p['url'],line)
