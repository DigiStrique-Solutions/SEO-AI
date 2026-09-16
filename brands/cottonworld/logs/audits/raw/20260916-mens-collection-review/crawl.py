import json, re, time, hashlib
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup

ROOT=Path(__file__).parent
BASE='https://cottonworld.net'
def fetch(url):
    t=time.time()
    try:
        r=requests.get(url,timeout=50)
        s=BeautifulSoup(r.content,'html.parser')
        key=(urlsplit(url).path.strip('/').replace('/','__') or 'home')+'-'+hashlib.sha256(url.encode()).hexdigest()[:8]
        (ROOT/(key+'.html')).write_bytes(r.content)
        main=s.find('main') or s
        for el in main.select('script,style'): el.decompose()
        links=[{'text':a.get_text(' ',strip=True),'url':urljoin(url,a['href'])} for a in main.select('a[href]')]
        blocks=[]
        for el in main.select('[class]'):
            if any(re.search(r'description|seo|richtext|rich-text',c,re.I) for c in el.get('class',[])):
                txt=el.get_text(' ',strip=True)
                if len(txt)>100 and not any(x['text']==txt for x in blocks):
                    blocks.append({'tag':el.name,'class':el.get('class'),'text':txt,'links':[{'text':a.get_text(' ',strip=True),'url':urljoin(url,a['href'])} for a in el.select('a[href]')]})
        return {'url':url,'status':r.status_code,'final_url':r.url,'redirects':[{'status':x.status_code,'url':x.url} for x in r.history], 'title':s.title.get_text() if s.title else '', 'h1':[x.get_text(' ',strip=True) for x in main.select('h1')], 'canonical':(s.select_one('link[rel=canonical]') or {}).get('href'), 'links':links,'blocks':blocks,'text':main.get_text('\n',strip=True),'html_file':key+'.html','elapsed':round(time.time()-t,2)}
    except Exception as e: return {'url':url,'error':str(e)}

if __name__=='__main__':
    landing=fetch(BASE+'/pages/landing-page-men')
    (ROOT/'landing.json').write_text(json.dumps(landing,indent=2,ensure_ascii=False),encoding='utf-8')
    s=BeautifulSoup((ROOT/landing['html_file']).read_text(encoding='utf-8'),'html.parser')
    nav=[]
    for a in s.select('a[href]'):
        href=urljoin(BASE,a['href'])
        if '/collections/' in href and not '/products/' in href:
            nav.append({'text':a.get_text(' ',strip=True),'url':href})
    (ROOT/'navigation.json').write_text(json.dumps(nav,indent=2,ensure_ascii=False),encoding='utf-8')
    print(json.dumps({'landing_links':landing['links'],'nav_links':nav},ensure_ascii=False))
