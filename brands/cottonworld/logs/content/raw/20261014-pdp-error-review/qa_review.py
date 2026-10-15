"""Independent source and copy checks for all current product rows."""
import collections, html, json, re, statistics
from pathlib import Path
R=Path(__file__).parent
rows=json.loads((R/'revised.json').read_text(encoding='utf-8'))
before={x['row']:x for x in json.loads((R/'current.json').read_text(encoding='utf-8'))}
records={x['row']:x for x in json.loads((R.parent/'20261006-added-active-pdp/records.json').read_text(encoding='utf-8'))}
live={x['row']:x['product'] for x in json.loads((R/'live-products.json').read_text(encoding='utf-8')) if x.get('product')}
errors=[];warnings=[];repeats=[];checked=[]
stop=set('a an the with and in this these it they has have is are for to of from at its their them on or that when your you so as wash s'.split())
def percentages(s):
    return sorted((int(a),re.sub(r'\s+',' ',b.lower())) for a,b in re.findall(r'(\d+)%\s*(organic\s+cotton|cotton|linen|viscose|lyocell|tencel|modal|bamboo|elastane|lycra|polyester|silk)',s,re.I))
for x in rows:
    row=x['row'];text=x['after'];body=text.split('\n\nStyling note')[0];rec=records[row];p=rec['product'] or {};raw=live.get(row,{}).get('description',p.get('Body (HTML)',''))
    src=html.unescape(re.sub('<[^>]+>',' ',raw))
    identity=text.endswith('Product ID: '+rec['code']) and x['original_url']==rec['original_url'] and x['url']==rec['updated_url']
    if not identity:errors.append([row,'Product identity mismatch'])
    if len(text.split('\n\n'))!=4:errors.append([row,'Paragraph count'])
    if re.search(r'\b([a-z]+)\s+\1\b',text,re.I):errors.append([row,'Adjacent repeated word'])
    if re.search(r'cut for an? [^.]*\bcut\b|cut in [^.]*sleeveless cut|a a |\[needs source\]|lorem ipsum|\ufffd',body,re.I):errors.append([row,'Malformed wording or placeholder'])
    sentences=re.split(r'(?<=[.!?])\s+',text.split('Product ID:')[0].strip())
    if len(sentences)!=len(set(sentences)):errors.append([row,'Duplicate sentence'])
    for s in sentences:
        words=collections.Counter(re.findall(r"[a-z]+(?:['-][a-z]+)*",s.lower()))
        duplicate=[k for k,v in words.items() if v>1 and k not in stop]
        if duplicate:repeats.append({'row':row,'sentence':s,'words':duplicate})
    # Percentages come directly from the current or exported merchant description, then title/metafields.
    fm=re.search(r'FABRIC COMPOSITION:\s*(.*?)(?:FIT TYPE:|\n)',src,re.I|re.S)
    expected=percentages(fm.group(1)) if fm else []
    if not expected:expected=percentages(p.get('Fabric Composition (product.metafields.custom.fabric_composition)','') or p.get('Title',''))
    got=percentages(body)
    if row in (255,256):
        if got:errors.append([row,'Unverified exact fabric percentages retained'])
        warnings.append([row,'Current title and fabric composition conflict; exact percentages withheld pending merchant confirmation'])
    elif expected and expected!=got:errors.append([row,'Fabric percentage mismatch',expected,got])
    mode_source=src+' '+p.get('Woven or Knit  (product.metafields.custom.woven_or_knit)','')
    for token in ('woven','knit'):
        claimed=re.search(r'\b'+token+r'(?:ted)?\b',body,re.I)
        supported=re.search(r'\b'+token+r'(?:ted)?\b',mode_source,re.I)
        if claimed and not supported:warnings.append([row,'Textile construction lacks explicit source',token])
    if x['facts']['pattern'] in ('CHECK','PRINT','STRIPE') and not any(v in body.lower() for v in ('checked','printed','striped','pattern','stripes','checks','print')):
        errors.append([row,'Pattern not described'])
    checked.append({'row':row,'identity':'pass' if identity else 'fail','fabric_percentages':'not_checked_blocked' if row in (24,255,256) else 'pass' if expected==got and expected else 'not_applicable' if not expected else 'fail','source':'live_product' if row in live and raw else x['source_kind'],'construction_source_present':any(x['facts']['attr'].values())})
firsts=collections.defaultdict(list);bodies=collections.defaultdict(list)
for x in rows:
    firsts[x['after'].split('. ')[0]].append(x['row']);bodies[x['after'].split('Product ID:')[0]].append(x['row'])
duplicate_first=[v for v in firsts.values() if len(v)>1];duplicate_body=[v for v in bodies.values() if len(v)>1]
if duplicate_first:errors.append(['all','Duplicate opening sentences',duplicate_first])
if duplicate_body:errors.append(['all','Duplicate full descriptions',duplicate_body])
result={'rows_checked':len(rows),'rows_changed':sum(x['after']!=before[x['row']]['after'] for x in rows),'unique_opening_sentences':len(firsts),'unique_full_descriptions':len(bodies),'word_range':[min(x['words'] for x in rows),statistics.median(x['words'] for x in rows),max(x['words'] for x in rows)],'errors':errors,'source_warnings':warnings,'sentence_word_repetitions_for_review':repeats,'row_checks':checked}
(R/'qa.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('row_checks','sentence_word_repetitions_for_review')},indent=2))
print('REPETITIONS',json.dumps(repeats[:70],ensure_ascii=False,indent=2))
