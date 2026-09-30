"""Expand verified PDP facts to Batch 1 depth without new performance claims."""
import json,re,statistics,collections,html
from pathlib import Path
R=Path(__file__).parent
PREV=R.parent/'20260930-pdp-batches234-review'
old=json.loads((PREV/'proposals.json').read_text(encoding='utf-8'))
records={(r['batch'],r['row']):r for r in json.loads((PREV/'records.json').read_text(encoding='utf-8'))}
def meta(p,k):return next((v.strip() for n,v in p.items() if n.startswith(k+' (')),'')
def wc(t):return len(t.split('Product ID:')[0].split())
def cap(t):return t[0].upper()+t[1:]
def intro(r):
 s=r['facts']; n=s['noun']; g=s['gender']; plural=n in ['trousers','shorts','culottes','pyjama bottoms','tights','track pants']; dem='these' if plural else 'this'; pro='they' if plural else 'it'; v=r['row']%4
 pattern={'STRIPE':'striped','CHECK':'checked','PRINT':'printed','HAKOBA':'eyelet','EMBROIDERED':'embroidered'}.get(s['pattern'],'')
 name=f"{g}'s {s['colour']} {pattern+' ' if pattern else ''}{n}"
 occasions={
  'shirt':['From the morning commute to a late lunch','For workdays with room for evening plans','For a weekend lunch or an informal day at work','For days that move between errands and meeting friends'],
  'T-shirt':['For a morning out or an afternoon close to home','For everyday plans that call for simple combinations','For days when a few familiar pieces are enough','For a weekend walk, coffee or time at home'],
  'blouse':['For lunch with friends or an informal workday','For days that move from work to a relaxed evening','For a morning out and plans that follow','For a simple change from your usual daytime separates'],
  'trousers':['For everyday plans, from the commute to lunch','For workdays and weekends built around familiar separates','For a day at work or a relaxed evening out','For days when you want a considered but simple outfit'],
  'shorts':['For weekends, local errands and afternoons outdoors','For an easy change of pace on days off','For casual lunches and time away from the weekday routine','For a morning walk or a relaxed afternoon with friends'],
  'dress':['For lunch, errands or an evening with friends','For days when one piece can anchor an outfit','For daytime plans that may run into the evening','For a simple way to get dressed and head out'],
  'culottes':['For daytime plans with a little room to dress up','For informal workdays and relaxed lunches','For a change from your usual weekend separates','For days that move from errands to meeting friends'],
  'jacket':['For a layer to take from work into the evening','For adding another element to familiar daytime separates','For days when you want to build an outfit in layers','For a simple finishing layer over everyday pieces'],
  'waistcoat':['For a light approach to dressing in layers','For a change from your usual shirt-and-trouser pairing','For adding interest to familiar daytime separates','For a layer to wear over a simple top'],
  'kurta':['For daytime outings and unhurried lunches','For a straightforward outfit on a busy morning','For meeting friends or spending an afternoon out','For days that call for simple, coordinated separates'],
  'sweatshirt':['For casual days and time between plans','For a weekend outfit built around familiar layers','For an easy layer on a day off','For relaxed afternoons at home or out with friends'],
  'pyjama set':['For evenings at home and a slower start the next day','For winding down after a full day','For a quiet evening and an unhurried morning','For time at home when dressing can stay simple'],
  'pyjama bottoms':['For evenings at home and a slower start the next day','For winding down after a full day','For a quiet evening and an unhurried morning','For time at home when dressing can stay simple'],
  'skirt':['For lunch with friends or a relaxed day out','For an alternative to your usual daytime separates','For a simple outfit that works around the rest of your day','For informal workdays and plans afterwards'],
  'tights':['For wearing under longer tops on casual days','For a simple base beneath a tunic or oversized shirt','For outfits built around loose tops and longer layers','For relaxed daytime combinations with a longline top'],
  'track pants':['For casual days and time at home','For a day off with few plans to dress around','For weekends and everyday errands','For a relaxed outfit between one plan and the next']}
 first=f"{occasions[n][v]}, {dem} {name} {'offer' if plural else 'offers'} a {s['fit']}."
 knit=s['knit']; comp=s['fabric']
 textile='knit' if knit else 'woven'
 second=f"The {textile} fabric is {comp}."
 if pattern:
  third='The surface detailing brings a point of interest to an otherwise straightforward silhouette.'
 else:
  third='The solid finish is easy to coordinate with the rest of your wardrobe.'
 return ' '.join([first,second,third])
def detail(r):
 s=r['facts']; a=s['attr']; n=s['noun']; p=records[(r['batch'],r['row'])]['product']
 text=r['after'].split('\n\n')[1]
 # Replace repetitive fact-list phrasing with complete, product-specific sentences.
 text=text.replace('The shape is finished with','The design finishes with')
 if n=='pyjama set':
  text=text.replace('There is an open front, along with side-seam pockets.','Side-seam pockets are included in the set.')
  text=text.replace('It also has side-seam pockets.','Side-seam pockets are included in the set.')
  if text.startswith('A round neckline is paired with'):text=text.replace('A round neckline is paired with','The top pairs a round neckline with',1)
 # Add genuine, currently omitted length detail where the source explicitly provides it.
 length=meta(p,'Length').lower()
 if n in ['shorts','trousers','culottes'] and length in ['knee length','bermuda length','ankle length','crop length','full length']:
  lengthwords={'knee length':'The length falls at the knee.','bermuda length':'The Bermuda length gives the cut a longer outline.','ankle length':'The cut finishes at ankle length.','crop length':'The cropped length leaves the ankle visible.','full length':'The cut is full length.'}
  if len(text.split())<40:text+=' '+lengthwords[length]
 # Replace the extra styling sentence with useful care information from this
 # product's own export; preserve the three-paragraph Batch 1 format.
 body=html.unescape(re.sub('<[^>]+>',' ',p['Body (HTML)'])).lower()
 if 'hand wash' in body:
  care='Hand wash separately; do not bleach. Remove promptly and dry in the shade.'
 else:
  assert 'machine wash cold' in body,(r['batch'],r['row'],'care source missing')
  care='Machine wash cold and wash dark colours separately.'
  if 'no bleach' in body or 'do not bleach' in body:care+=' Do not bleach; remove promptly and dry in the shade.'
  if 'do not iron on print' in body:care+=' Do not iron on the print.'
  if 'iron on low heat' in body:care+=' Iron on low heat.'
  if 'warm iron' in body:care+=' Use a warm iron.'
 return text+' '+care
def styling(r):
 s=r['facts'];n=s['noun'];g=s['gender'];c=s['colour'];v=(r['batch']+r['row'])%4
 # Two useful outfit directions instead of a repeated full product name.
 contrast='off-white' if any(x in c for x in ['navy','black','blue','brown','olive','green','grey','wine','rust']) else 'navy'
 if contrast in c:contrast='charcoal'
 art='an' if contrast=='off-white' else 'a'
 if n in ['trousers','culottes','shorts','skirt']:
  pro='it' if n=='skirt' else 'them';top='shirt' if g=='men' else 'blouse'
  if n=='shorts':return f'Wear {pro} with {art} {contrast} short-sleeve shirt and sandals for a casual afternoon. For a walk or a day of errands, switch to a plain crew-neck T-shirt and canvas trainers, keeping the rest of the outfit simple.'
  return [f'Pair {pro} with {art} {contrast} {top} and loafers for lunch or an informal workday. For the weekend, choose a plain T-shirt and trainers instead. A small shoulder bag keeps the outfit practical without adding another layer.',f'Try {pro} with a plain {contrast} top and flat sandals for daytime plans. Add a short jacket and switch to loafers for dinner, keeping the layers simple so the proportions stay clear.',f'Wear {pro} with {art} {contrast} {top}, tucked in to show the waist, and finish with loafers. For a more relaxed afternoon, leave a lightweight shirt open over a plain tee and choose trainers.',f'Keep daytime dressing simple with {art} {contrast} knit top and flat shoes. A crisp shirt offers another option for meeting friends; add a small bag and understated accessories rather than several extra layers.'][v]
 if n=='dress':return ['Wear it with flat sandals and a canvas tote for lunch or a day out. For dinner, change to loafers or flat mules and a smaller bag. An open jacket gives you another layer without covering the neckline.', 'Pair it with trainers and a crossbody bag for a morning of errands. Switch to leather slides and a small shoulder bag for an afternoon with friends, keeping jewellery understated so the garment details can stand out.', 'Try it with flat mules for daytime plans, then add an unbuttoned jacket when you want another layer. A simple tote works for errands; choose a compact shoulder bag for lunch or an evening out.', 'Wear it with sandals and a shoulder bag for a relaxed afternoon. For a different mood, add an open shirt and canvas trainers. Keep the accessories simple and let the shape remain visible beneath the extra layer.'][v]
 if n in ['jacket','waistcoat']:return f'Layer it over a plain {contrast} top with straight trousers and loafers for a daytime outing. For the weekend, switch to jeans and trainers. Keep the layer underneath simple so the front detailing and outline remain easy to see.'
 if n=='kurta':return f'Pair it with plain {contrast} trousers and flat sandals for lunch or a day out. Choose straight bottoms to keep the proportions balanced, then add a small shoulder bag. Flats offer another footwear option when you want a neater finish.'
 if n=='tights':return 'Wear them beneath a longline tunic with flat shoes for everyday plans. An oversized shirt and trainers offer a second option for the weekend. Keep the top loose enough to balance the closer lower silhouette, with a simple shoulder bag alongside.'
 if n=='pyjama set':return 'Wear the two pieces together with slippers for an evening at home. The top can also be paired with plain lounge trousers when you want a different combination. Keep extra layers loose and simple for reading, breakfast or a slow morning.'
 if n=='pyjama bottoms':return 'Pair them with a plain sleep T-shirt and slippers for evenings at home. On a slower morning, add a loose overshirt while you make breakfast or read. Choose a single-colour top to give the print space rather than adding another pattern.'
 if n=='track pants':return 'Wear them with a plain T-shirt and trainers for errands or a day off. A zip jacket makes a useful extra layer for the journey home. Keep the top in a single colour and use a small bag for the rest of your essentials.'
 if n=='sweatshirt' or s['attr']['neck']=='HOODED':return f'Wear it over a plain T-shirt with {contrast} trousers and trainers for casual daytime plans. For a weekend at home, switch to lounge bottoms and slippers. Keep any outer layer open so the neckline and front details remain visible.'
 if s['pattern'] not in ['SOLID','PLAIN','']:
  return f'Pair it with plain {contrast} trousers and loafers for lunch or meeting friends. For a day off, choose solid-colour shorts and sandals. Keep the jacket and accessories simple so the pattern has room to stand out in either combination.'
 return [f'Wear it with {contrast} trousers and loafers for an informal workday or lunch. For a day off, choose straight-leg jeans and trainers instead. Add an open jacket only when you need another layer, keeping the neckline visible.',f'Try it with {contrast} shorts and sandals for a casual afternoon. Straight-leg trousers and loafers offer a second option for dinner or meeting friends. Keep the rest of the outfit uncluttered, with a simple bag and just a few accessories.',f'Pair it with dark jeans and canvas trainers for weekend plans. For a neater daytime outfit, choose {contrast} trousers and loafers. An unbuttoned shirt or light jacket adds another layer without taking attention away from the shape.',f'Wear it with {contrast} trousers and flat shoes for a simple daytime combination. Switch to jeans and trainers when the plans are more casual, and leave an outer layer open to show the neckline. A small bag is enough to finish.'][v]
out=[]
for r in old:
 b=r['batch'];row=r['row']; fresh=json.loads((R/f'before-batch{b}.json').read_text(encoding='utf-8'))['structuredContent']['sheets'][0]['data'][0]['rowData'][row-1]['values']
 assert fresh[0]['userEnteredValue']['stringValue']==r['code']
 current=fresh[2]['userEnteredValue']['stringValue']; assert current==r['after'],(b,row,'source changed')
 paragraphs=[intro(r),detail(r),'Styling note - '+styling(r),'Product ID: '+r['code']]
 after='\n\n'.join(paragraphs)
 out.append(dict(batch=b,row=row,code=r['code'],before=current,after=after,words=wc(after),facts=r['facts'],source_ref=f'../20260930-pdp-batches234-review/records.json#{b}:{row}'))
(R/'proposals.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
for b in [2,3,4]:
 rr=[r for r in out if r['batch']==b]
 (R/f'review-batch{b}.txt').write_text('\n\n'.join(str(r['row'])+' | '+r['after'].replace('\n\n',' | ') for r in rr),encoding='utf-8')
 print(b,len(rr),min(r['words'] for r in rr),statistics.median(r['words'] for r in rr),max(r['words'] for r in rr))
