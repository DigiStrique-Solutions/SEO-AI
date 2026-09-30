"""Source-grounded PDP editorial pass. Writes local proposals only."""
import json,re,html,collections
from pathlib import Path
R=Path(__file__).parent
records=json.loads((R/'records.json').read_text(encoding='utf-8'))
def meta(p,k): return next((v.strip() for n,v in p.items() if n.startswith(k+' (')), '')
def join(xs): return ', '.join(xs[:-1])+(' and '+xs[-1] if len(xs)>1 else xs[0]) if xs else ''
def cap(s): return s[:1].upper()+s[1:]
def norm(s): return re.sub(r'\s+',' ',s.strip()).upper()
def getbody(p):
 return {norm(html.unescape(re.sub('<[^>]+>','',a))):norm(html.unescape(re.sub('<[^>]+>','',b))) for a,b in re.findall(r'<li[^>]*>\s*(.*?):(.*?)</li>',p['Body (HTML)'],re.S)}
issues=[]
neck={'ROUND NECK':'a round neckline','SHIRT COLLAR':'a shirt collar','REGULAR COLLAR':'a regular collar','BAND COLLAR':'a band collar','BOWLING COLLAR':'a bowling collar','BUTTONDOWN COLLAR':'a button-down collar','BUTTON DOWN COLLAR':'a button-down collar','POLO':'a polo collar','POLO COLLAR':'a polo collar','JOHNY COLLAR':'a Johnny collar','JOHNNY COLLAR':'a Johnny collar','V NECK':'a V-neckline','HOODED':'a hood','HIGH MANDARIN COLLAR':'a high mandarin collar','BAND COLLAR WITH V NECK':'a band collar with a V-shaped opening','ROUND V NECK':'a shaped neckline','MANILLA COLLAR':'a Manila collar'}
sleeves={'SHORT SLEEVE':'short sleeves','HALF SLEEVES':'half sleeves','HALF SLEEVE':'half sleeves','FULL SLEEVES':'full sleeves','FULL SLEEVE':'full sleeves','LONG SLEEVE':'long sleeves','LONG SLEEVES':'long sleeves','3/4 SLEEVE':'three-quarter sleeves','SLEEVELESS':'a sleeveless cut','EXTENDED SHORT SLEEVE':'extended short sleeves','EXTENDED SLEEVE WITH ELASTIC':'extended sleeves with elastic','ELBOW LENGTH SLV':'elbow-length sleeves','ELBOW LENGTH SLEEVE':'elbow-length sleeves','SHORT SLEEVE WITH CUFF':'cuffed short sleeves','LONG SLEEVE WITH CUFF':'cuffed long sleeves','3/4 SLV WITH BIG CUFF':'three-quarter sleeves with wide cuffs','3/4 SLEEVE WITH CUFF':'cuffed three-quarter sleeves','3/4 SLEEVE WITH ELASTIC CUFF':'three-quarter sleeves with elasticated cuffs','SHORT SLV WITH D RING TABS':'short sleeves with D-ring tabs','LONG SLEEVE WITH TAB ON CUFF':'long sleeves with cuff tabs','RAGLAN SLEEVES':'raglan sleeves','ELASTICATED SLEEVES':'elasticated sleeves'}
openings={'BUTTON FRONT':'a button front','FOLDED PLACKET':'a folded placket','REGULAR PLACKET':'a regular placket','CONCEALED PLACKET':'a concealed placket','HALF OPEN WITH BUTTONS':'a half-open button placket','HALF OPEN WITH 02 BUTTONS':'a two-button half placket','FRONT ZIP':'a front zip','ZIPPER OPENING':'a zip opening','PULL ON WITH BUTTON DETAIL':'a pull-on design with button detailing','PULL ON BACK BUTTON AND SIDE SLITS':'a back button and side slits','OPEN FRONT':'an open front','OPEN FRONT WITH TIES':'an open front with ties','PULL ON WITH FRONT TIES':'a pull-on design with front ties','BUTTON AND ZIP':'a button-and-zip fastening','BUTTON AND ZIP CLOSURE':'a button-and-zip fastening','FITTED WAIST WITH SIDE BUTTON AND ZIPPER CLOSURE':'a side button-and-zip fastening','HOOK AND EYE / ZIPPER':'a hook-and-eye fastening with a zip','SIDE ZIP':'a side zip','ELASTIC AT WAIST WITH BUTTON AND ZIP AT FRONT':'a button-and-zip front','BACK ELASTIC FRONT BUTTON AND ZIP':'a button-and-zip front','ZIP FLY':'a zip fly','FRONT OPEN':'an open front','HALF OPEN':'a half-open front'}
hems={'STRAIGHT HEM':'a straight hem','STRAIGHT WITH SIDE SLIT':'a straight hem with side slits','STRAIGHT HEM WITH SLITS':'a straight hem with slits','SIDE SLIT HEM':'a hem with side slits','ROUND HEM':'a rounded hem','CURVED HEM':'a curved hem','FOLDED HEM':'folded hems','ROUND HEM WITH GUSSET':'a rounded hem with a gusset','ROUND HEM WITH SIDE SLITS':'a rounded hem with side slits','ELASTICATED':'an elasticated hem','ELASTICATED HEM':'an elasticated hem','ZIP HEM':'zipped hems'}
pockets={'SIDE SEAM AND BACK POCKETS':'side-seam and back pockets','SIDE SEAM POCKETS':'side-seam pockets','ONE POCKET':'one pocket','KANGAROO POCKET':'a kangaroo pocket','SIDE SEAM/COIN POCKET AND BACK POCKET':'side-seam, coin and back pockets','SIDE AND BACK POCKETS':'side and back pockets','2 FRONT POCKETS':'two front pockets','BACK POCKET':'a back pocket','INSEAM ANGLE POCKETS':'angled inseam pockets','MOCK POCKETS':'mock pockets','2 POCKETS':'two pockets','TWO POCKET':'two pockets','SIDE SEAM AND SINGLE BACK POCKET':'side-seam pockets and one back pocket','SIDE SEAM AND CARGO POCKETS':'side-seam and cargo pockets','FRONT AND SIDE POCKETS':'front and side pockets','FRONT POCKET':'a front pocket','SIDE SEAM AND FRONT POCKETS':'side-seam and front pockets','2 FLAP POCKETS':'two flap pockets','INSEAM POCKETS':'inseam pockets','SLANT POCKET':'a slant pocket','CARGO POCKET':'cargo pockets','MULTI POCKET':'multiple pockets'}
waists={'WITH BELT LOOPS':'belt loops','MID WAIST':'a mid-rise waist','FITTED WAIST':'a fitted waistband','ELASTIC WAIST WITH DRAWSTRING':'an elasticated drawstring waist','ELASTIC WAIST DRAWSTRING':'an elasticated drawstring waist','BACK ELASTIC':'elastic at the back waist','ELASTIC WAIST':'an elasticated waist','ELASTICATED':'an elasticated waist','ELASTICATED WAIST BAND':'an elasticated waistband','FULL ELASTIC':'an elasticated waist','HALF ELASTIC':'a partially elasticated waist','ELASTIC WAIST WITHOUT DRAWSTRING':'an elasticated waist','HIGH WAIST':'a high waist','REGULAR WAIST':'a regular waistband'}
legs={'STRAIGHT LEG':'straight legs','WIDE LEG':'wide legs','SKINNY':'a skinny leg','SKINNY LEG':'a skinny leg','BARREL LEG':'a barrel-leg shape','FITTED':'a fitted leg','FITTED LEG':'a fitted leg'}
types={'KDRESS':'dress','KDRESSES':'dress','DRESS':'dress','DRESSES':'dress','BLOUSE':'blouse','BLOUSES':'blouse','PANTS':'trousers','KPANTS':'trousers','SHORTS':'shorts','KSHORTS':'shorts','SHIRTS':'shirt','SHIRT':'shirt','CULOTTE':'culottes','CULOTTES':'culottes','TSHIRT':'T-shirt','T-SHIRTS':'T-shirt','TSHIRTS':'T-shirt','JACKET':'jacket','JACKETS':'jacket','WAISTCOAT':'waistcoat','WAISTCOATS':'waistcoat','KURTA':'kurta','KURTAS':'kurta','PYJAMA SUIT':'pyjama set','PYJAMA':'pyjama bottoms','PYJAMAS':'pyjama bottoms','SKIRT':'skirt','SKIRTS':'skirt','KTIGHTS':'tights','TIGHTS':'tights','TRACK PANT':'track pants'}
def source(r):
 p=r['product']; d=getbody(p)
 t=norm(d.get('TYPE') or meta(p,'Product Type')); noun=types.get(t)
 if not noun: raise ValueError((r['code'],t))
 if 'sweatshirt' in p['Title'].lower(): noun='sweatshirt'
 if 'pyjama suit' in p['Title'].lower(): noun='pyjama set'
 gender='women' if r['code'].startswith('l-') else 'men'
 colour=d.get('COLOR') or meta(p,'Colour') or re.sub(r'^[ml]-.*?-\d+-\d+-','',r['code'])
 colour=colour.lower().replace('lt.','light ').replace('dk.','dark ').replace('off white','off-white')
 colour=re.sub(r'\s+',' ',colour).replace('multi','multicolour').replace('lt brown','light brown').replace('ecru melan','ecru melange')
 colour=colour.replace('/',' and ').replace('offwhite','off-white').replace('dark-blue','dark blue').replace('darkoliveg','dark olive')
 if colour=='white a': colour='white'
 for bad,good in [('white-blue','white and blue'),('white-navy','white and navy'),('natural-black','natural and black'),('white-black','white and black'),('olive-black','olive and black'),('brown-white','brown and white'),('sky-olive','sky and olive'),('maroon-red','maroon red'),('teal-blue','teal blue')]: colour=colour.replace(bad,good)
 comp=meta(p,'Fabric Composition').lower().replace('ployester','polyester')
 comp=re.sub(r'\s+%','%',comp)
 parts=re.findall(r'\d+(?:\.\d+)?%\s+[a-z]+(?:\s+cotton)?',comp)
 parts=[x.replace('lycra','Lycra').replace('lurex','Lurex').replace('excel','Excel') for x in parts]
 if not parts: raise ValueError(('composition',r['code'],comp))
 fabric=join(parts)
 fit=(d.get('FIT TYPE') or meta(p,'Fit Type')).lower().replace('relax fit','relaxed fit')
 pattern=norm(d.get('PRINT') or meta(p,'Pattern'))
 pattern={'CHECKED':'CHECK','STRIPED':'STRIPE'}.get(pattern,pattern)
 attr={name:norm(d.get(dk) or meta(p,mk)) for name,dk,mk in [('neck','NECKCOLLOR','Neck Collar'),('sleeve','SLEEVE','Sleeve'),('opening','OPENING','Opening'),('hem','HEMLINE','Hemline'),('pocket','POCKET','Pocket'),('waist','WAIST','Waist'),('leg','LEG','Leg')]}
 if d.get('HEMLINE BOTTOM'): attr['hem']=d['HEMLINE BOTTOM']
 if attr['sleeve'] not in sleeves and attr['sleeve']:
  issues.append({'batch':r['batch'],'row':r['row'],'field':'sleeve','source':attr['sleeve'],'action':'Used valid sleeve metafield; discarded misplaced collar value.'})
  attr['sleeve']=norm(meta(p,'Sleeve'))
 if attr['neck'] not in neck and attr['neck']:
  issues.append({'batch':r['batch'],'row':r['row'],'field':'neck','source':attr['neck'],'action':'Omitted unrecognized/misplaced collar value.'})
  attr['neck']=''
 # Do not choose between contradictory title and structured cut labels.
 title=p['Title'].lower()
 if (('wide leg' in title or 'tapered' in title) and attr['leg']=='STRAIGHT LEG'):
  issues.append({'batch':r['batch'],'row':r['row'],'field':'leg','source':attr['leg'],'action':'Omitted cut claim: source title conflicts with structured leg field.'})
  attr['leg']=''
 return dict(noun=noun,gender=gender,colour=colour,fabric=fabric,fit=fit,pattern=pattern,attr=attr,knit=norm(meta(p,'Woven or Knit '))=='KNIT')
def style(s,r):
 n,g,c=s['noun'],s['gender'],s['colour']; v=(r['row']+r['batch'])%6
 dark=any(x in c for x in ['navy','black','brown','wine','maroon','olive','grey','green','blue','rust'])
 contrast='off-white' if dark else 'navy'
 if contrast in c: contrast='charcoal'
 printed=s['pattern'] not in ['SOLID','PLAIN','']
 if n=='pyjama set': return 'Wear the pieces together with slippers for evenings at home, or use the top as a separate with plain lounge trousers.'
 if n=='pyjama bottoms': return 'Pair them with a plain sleep T-shirt and slippers. Keep the top in a single colour to give the print space.' if printed else 'Pair them with a soft T-shirt and slippers for evenings at home. A loose top keeps the outfit simple.'
 if n in ['trousers','track pants','culottes','shorts','tights','skirt']:
  pron='it' if n=='skirt' else 'them'
  if n=='tights': return ['Wear them with a longline tunic and flats, adding an open shirt as a layer for daytime plans.','Pair them with an oversized shirt and trainers. Keep accessories simple and let the longer top set the proportions.'][v%2]
  if g=='men':
   options=[f'Wear {pron} with a {contrast} shirt and loafers for lunch or an informal workday.',f'Pair {pron} with a plain {contrast} T-shirt and canvas trainers for weekend plans.',f'Add a {contrast} polo and leather sandals for a relaxed daytime outfit.',f'Try {pron} with a {contrast} short-sleeve shirt and slip-on shoes.',f'Keep the outfit simple with a {contrast} crew-neck T-shirt and trainers.',f'Wear {pron} with a {contrast} shirt, leaving it untucked for a casual afternoon. Finish with loafers.']
  else:
   options=[f'Pair {pron} with a {contrast} blouse and flat sandals for daytime plans.',f'Wear {pron} with a plain {contrast} T-shirt and trainers for an easy weekend outfit.',f'Add a {contrast} shirt and loafers for lunch or an informal workday.',f'Try a {contrast} sleeveless top and leather slides, with an open shirt as an extra layer.',f'Wear {pron} with a {contrast} knit top and flats. Keep accessories small and simple.',f'Tuck in a {contrast} blouse to define the waist, then add sandals for a relaxed afternoon.']
  if n=='track pants': return 'Wear them with a plain T-shirt and trainers for casual days. Add a zip jacket when you want another layer.'
  if n=='shorts' and v in [0,2]: return f'Wear {pron} with a {contrast} short-sleeve shirt and flat sandals for a weekend outing.'
  return options[v]
 if n=='dress':
  return ['Wear it with flat sandals and a canvas tote for daytime plans. Add an open shirt for another layer.', 'Try it with leather slides for a relaxed afternoon, or change to loafers for dinner.', 'Keep the outfit simple with flat mules and a small shoulder bag. An unbuttoned jacket adds a layer.', 'Pair it with trainers and a crossbody bag for a day out. Choose simple accessories to keep the outfit uncluttered.', 'Add sandals and a small tote for lunch, then bring a light jacket for the evening.', 'Wear it with flats and a shoulder bag. Choose understated jewellery to leave room for the garment details.'][v]
 if n in ['jacket','waistcoat']:
  return [f'Layer it over a plain {contrast} T-shirt with straight trousers and loafers.',f'Wear it over a {contrast} shirt with dark jeans. Finish with trainers for casual plans.',f'Pair it with a {contrast} top and straight-leg trousers, keeping the layer underneath simple.'][v%3]
 if n=='kurta': return f'Pair it with {contrast} trousers and flat sandals. Keep the bottoms plain so the neckline and pattern remain visible.' if printed else f'Wear it with {contrast} trousers and flats for daytime plans. A small shoulder bag is enough to finish the outfit.'
 if n=='sweatshirt': return f'Wear it over a plain T-shirt with {contrast} trousers and trainers. For a casual weekend, switch to jeans.'
 bottom=f'{contrast} trousers'
 opts=[f'Wear it with {bottom} and loafers for a daytime outing.', f'Pair it with straight-leg jeans and trainers for the weekend. An open jacket adds a layer.', f'Try it with {contrast} shorts and flat sandals for casual afternoon plans.',f'Add {bottom} and simple leather sandals. Keep the rest of the outfit in solid colours.', f'Wear it with dark jeans and loafers, or choose {contrast} shorts for a more casual outfit.',f'Pair it with {bottom} and canvas trainers. Leave accessories simple so the garment details stay visible.']
 if printed: return [f'Pair it with plain {bottom} and loafers, letting the pattern be the focus.',f'Wear it with solid-colour jeans and trainers. Keep the jacket and accessories plain to avoid competing patterns.',f'Try it with plain {contrast} shorts and sandals for a relaxed day out.'][v%3]
 return opts[v]
def rewrite(r):
 s=source(r); a=s['attr']; n=s['noun']; plural=n in ['trousers','shorts','culottes','pyjama bottoms','tights','track pants']; demonstrative='these' if plural else 'this'; verb='are' if plural else 'is'; poss='their' if plural else 'its'
 name=f"{s['gender']}'s {s['colour']} {n}"
 texture={'STRIPE':'striped','CHECK':'checked','PRINT':'printed','HAKOBA':'eyelet','EMBROIDERED':'embroidered'}.get(s['pattern'],'')
 if texture: name=f"{s['gender']}'s {s['colour']} {texture} {n}"
 fabric=s['fabric']; fit=s['fit']; v=r['row']%4
 intro=[f"{cap(demonstrative)} {name} {verb} made from {fabric} and cut in a {fit}.",f"Cut in a {fit}, {demonstrative} {name} {verb} made from {fabric}.",f"Made from {fabric}, {demonstrative} {name} {('have' if plural else 'has')} a {fit}.",f"{cap(demonstrative)} {name} combine{' ' if plural else 's '}{fabric} with a {fit}."][v]
 details=[]
 if n in ['trousers','shorts','culottes','tights','track pants','skirt','pyjama bottoms']:
  waist=waists.get(a['waist'],''); opening=openings.get(a['opening'],'')
  if a['opening']=='FRONT OPEN': opening=''
  if 'DRAWSTRING' in a['opening'] and 'drawstring' not in waist:
   waist='an elasticated drawstring waist' if 'ELASTIC' in a['opening'] or 'ELASTIC' in a['waist'] else 'a drawstring waist'
  if not waist and a['opening']=='ELASTIC': waist='an elasticated waist'
  if a['opening'].startswith('ELASTIC AT WAIST') and not 'elastic' in waist: waist='an elasticated waist'
  leg=legs.get(a['leg'],'') if n!='skirt' else ''
  parts=[x for x in [waist,opening,leg] if x]
  if parts: details.append(f"{'They have' if plural else 'It has'} {join(parts)}.")
  pocket=pockets.get(a['pocket'],''); hem=hems.get(a['hem'],'')
  if pocket and hem:
   if a['pocket']=='MOCK POCKETS': details.append(f'Mock pockets add detail. The legs finish with {hem}.')
   else: details.append(f"The design includes {pocket}; {'the legs finish' if plural else 'it is finished'} with {hem}.")
  elif pocket: details.append(f"The design includes {pocket}.")
  elif hem: details.append(f"{'The legs finish with' if plural else 'The design finishes with'} {hem}.")
  if not pocket and a['pocket'] in ['NO POCKETS','NO POCKET']: details.append('There are no pockets.')
  if n=='skirt': details=[x.replace('folded hems','a folded hem') for x in details]
 else:
  collar=neck.get(a['neck'],''); sleeve=sleeves.get(a['sleeve'],''); opening=openings.get(a['opening'],''); hem=hems.get(a['hem'],''); pocket=pockets.get(a['pocket'],'')
  pairs=[x for x in [collar,sleeve] if x]
  if collar and sleeve:
   details.append([f'{cap(collar)} is paired with {sleeve}.',f'The design has {collar} and {sleeve}.',f'It has {collar} and {sleeve}.'][r['row']%3])
  elif pairs: details.append('It has '+join(pairs)+'.')
  if opening and pocket: details.append(f'There is {opening}, along with {pocket}.')
  elif opening: details.append('It features '+opening+'.')
  elif pocket: details.append('It also has '+pocket+'.')
  if hem: details.append('The shape is finished with '+hem+'.')
  if a['opening']=='BOX PLEATS WITH STITCHING DETAILS AT BACK': details.append('Box pleats and stitching detail the back.')
  if a['opening']=='PEPLUM TOP': details.append('The top has a peplum shape.')
  if a['opening']=='PULL ON' and not opening and len(details)<2: details.append('It pulls on over the head.')
 if not details: raise ValueError(('no details',r['code']))
 if n=='pyjama set':
  details=[x.replace('It has ','The top has ').replace('The design has ','The top has ') for x in details]
 # Plain weave and knit are product facts; no unsupported comfort/performance promises.
 copy=intro+'\n\n'+' '.join(details)+'\n\nStyling note - '+style(s,r)+'\n\nProduct ID: '+r['code']
 copy=copy.replace('a off-white','an off-white').replace('a elasticated','an elasticated')
 if r['batch']==4 and r['row']==82:
  copy=copy.replace('Add a navy shirt and loafers for lunch or an informal workday.','Wear them with a navy blouse and sandals for lunch. Switch to a striped T-shirt and trainers for weekend plans.')
 return dict(batch=r['batch'],row=r['row'],code=r['code'],url=r['url'],before=r['old'],after=copy,comment=r['comment'],facts=s,source_handle=r['product']['Handle'],source_status=r['product']['Status'])
proposals=[rewrite(r) for r in records if r['batch']>1]
(R/'proposals.json').write_text(json.dumps(proposals,ensure_ascii=False,indent=2),encoding='utf-8')
(R/'source-issues.json').write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
for b in [2,3,4]:
 rr=[r for r in proposals if r['batch']==b]
 (R/f'review-batch{b}.txt').write_text('\n\n'.join(str(r['row'])+' | '+r['after'].replace('\n\n',' | ') for r in rr),encoding='utf-8')
 print('Batch',b,'proposals',len(rr),'words',min(len(r['after'].split()) for r in rr),max(len(r['after'].split()) for r in rr))
print('Source issues',len(issues))
