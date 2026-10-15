"""Apply reviewed, source-backed PDP corrections without changing sheet identity data."""
import collections, copy, html, json, re, statistics
from pathlib import Path
R=Path(__file__).parent
original=json.loads((R/'current.json').read_text(encoding='utf-8'))
records={x['row']:x for x in json.loads((R.parent/'20261006-added-active-pdp/records.json').read_text(encoding='utf-8'))}
live={x['row']:x['product'] for x in json.loads((R/'live-products.json').read_text(encoding='utf-8')) if x.get('product')}
def fields(raw):
    return {re.sub(r'\s+',' ',k.strip().upper()):re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',v)).strip().upper()) for k,v in re.findall(r'<li>\s*([^:<]+):\s*(.*?)\s*</li>',raw,re.I|re.S)}

# Each entry contains a natural rendering and a recognition pattern for existing copy.
vocab={
'neck':{
 'BAND NECK':('a band neckline',r'band (?:collar|neckline)'),
 'BAND COLLAR':('a band collar',r'band collar'),
 'BAND COLLAR WITH V NECK':('a band collar with a V-shaped opening',r'band collar with a V-shaped opening'),
 'BOAT NECK':('a boat neckline',r'boat neckline'),
 'BUTTON DOWN COLLAR':('a button-down collar',r'button-down collar'),
 'HOODED':('a hood',r'\bhood\b'),
 'JOHNNY COLLAR':('a Johnny collar',r'Johnny collar'),
 'LAPEL COLLAR':('a lapel collar',r'lapel collar'),
 'MANDARIN COLLAR':('a mandarin collar',r'mandarin collar'),
 'POLO':('a polo collar',r'polo collar'),
 'POLO COLLAR':('a polo collar',r'polo collar'),
 'REGULAR COLLAR':('a collar',r'\bcollar\b'),
 'SHIRT COLLAR':('a shirt collar',r'shirt collar'),
 'ROUND NECK':('a round neckline',r'round neckline'),
 'ROUND V NECK':('a rounded V-neckline',r'rounded V-neckline'),
 'ROUND NECK WITH V SHAPE AT BACK':('a round front neckline and a V-shaped back',r'round front neckline and a V-shaped back'),
 'SHAWL COLLAR':('a shawl collar',r'shawl collar'),
 'V NECK':('a V-neckline',r'V-neckline'),
},
'sleeve':{
 '3/4 SLEEVE':('three-quarter sleeves',r'three-quarter sleeves'),
 '3/4 SLEEVE WITH CUFF':('cuffed three-quarter sleeves',r'cuffed three-quarter sleeves'),
 'EXTENDED 3/4 SLEEVE':('extended three-quarter sleeves',r'extended three-quarter sleeves'),
 'EXTENDED 3/4 SLEEVE WITH CUFF':('extended three-quarter sleeves with cuffs',r'extended three-quarter sleeves with cuffs'),
 'EXTENDED LONG SLEEVE':('extended long sleeves',r'extended long sleeves'),
 'EXTENDED SHORT SLEEVE':('extended short sleeves',r'extended short sleeves'),
 'EXTENDED SHORT SLEEVE WITH CUFF':('extended short sleeves with cuffs',r'extended short sleeves with cuffs'),
 'EXTENDED SHORT SLEEVE WITH TIES':('extended short sleeves with ties',r'extended short sleeves with ties'),
 'EXTENDED SLEEVES':('extended sleeves',r'extended sleeves'),
 'BAT SLEEVE':('batwing sleeves',r'batwing sleeves'),
 'ELASTICATED SLEEVES':('elasticated sleeves',r'elasticated sleeves'),
 'FULL SLEEVE':('full sleeves',r'full sleeves'),
 'FULL SLEEVES':('full sleeves',r'full sleeves'),
 'HALF SLEEVE':('half sleeves',r'half sleeves'),
 'HALF SLEEVES':('half sleeves',r'half sleeves'),
 'LONG SLEEVE WITH CUFF':('cuffed long sleeves',r'cuffed long sleeves'),
 'RAGLAN SLEEVES':('raglan sleeves',r'raglan sleeves'),
 'SHORT SLEEVE':('short sleeves',r'short sleeves'),
 'SHORT SLEEVE WITH CUFF':('cuffed short sleeves',r'cuffed short sleeves'),
 'SHORT SLEEVE WITH FOLD':('short sleeves with folded cuffs',r'short sleeves with folded cuffs'),
 'SLEEVELESS':('a sleeveless design',r'sleeveless'),
 'STRAPS':('shoulder straps',r'shoulder straps'),
},
'opening':{
 'BACK ZIPPER':('a back zip',r'back zip'),
 'BUTTON AND ZIP':('a button-and-zip fastening',r'button-and-zip fastening'),
 'BUTTON AND ZIP CLOSURE':('a button-and-zip fastening',r'button-and-zip fastening'),
 'BUTTON FRONT':('a button front',r'button front|front has buttons'),
 'BUTTON FRONT / BELT':('a button front and a belt',r'button front and a belt'),
 'CONCEALED PLACKET':('a concealed placket',r'concealed placket'),
 'CONCEALED PLACKET /DRAWSTRING AT WAIST':('a concealed placket and a drawstring at the waist',r'concealed placket and a drawstring at the waist'),
 'DETAILED PLACKET':('a detailed front placket',r'detailed front placket'),
 'FOLDED PLACKET':('a folded placket',r'folded placket'),
 'FRONT MOCK BUTTONS':('decorative front buttons',r'decorative front buttons'),
 'FRONT OPEN':('a front opening',r'front opening|front has an opening'),
 'OPEN FRONT':('an open front',r'open front|front is open'),
 'FRONT YOKE':('a front yoke',r'front yoke'),
 'HALF OPEN':('a half-length front opening',r'half-length front opening'),
 'HALF OPEN WITH 02 BUTTONS':('a short two-button placket',r'short two-button placket'),
 'HALF OPEN WITH BUTTONS':('a half-length button placket',r'half-length button placket'),
 'PULL ON WITH BUTTON DETAIL':('a pull-on design with button detailing',r'pull-on design with button detailing'),
 'PULL ON WITH SHIRRING ON SHOULDERS':('a pull-on design with shirring at the shoulders',r'pull-on design with shirring at the shoulders'),
 'REGULAR PLACKET':('a front placket',r'(?:front )?placket'),
 'SIDE BUTTONS':('side buttons',r'side buttons'),
 'ZIP FLY':('a zip fly',r'zip fly'),
 'ZIPPER OPENING':('a zip opening',r'zip opening'),
},
'hem':{
 'ASSYMETRIC HEMLINE':('an asymmetric hem',r'asymmetric hem'),
 'STRAIGHT BOTTOM':('a straight hem',r'straight hem'),
 'STRAIGHT HEM WITH FOLD':('a straight, folded hem',r'straight, folded hem'),
 'BUBBLE HEM':('bubble hems',r'bubble hems'),
},
'pocket':{
 'FRONT PATCH POCKETS':('front patch pockets',r'front patch pockets'),
 'PATCH POCKETS':('patch pockets',r'patch pockets'),
 'CARGO POCKETS':('cargo pockets',r'cargo pockets'),
},
'waist':{
 '1/2 ELASTIC':('a partly elasticated waist',r'partly elasticated waist'),
 'SIDE ELASTIC WITH BUTTON AND ZIPPER':('elastic at the sides of the waist',r'elastic at the sides of the waist'),
 'WITH BELT LOOPS':('belt loops',r'belt loops'),
 'MID WAIST':('a mid-rise waist',r'mid-rise waist'),
},
}
changes=[];after=[];used_first=set();field_evidence=[]
for item in original:
    x=copy.deepcopy(item);row=x['row'];f=x['facts'];attrs=f['attr'];rec=records[row];p=rec['product'] or {}
    raw=live.get(row,{}).get('description',p.get('Body (HTML)',''))
    src=fields(raw)
    source_ref=('live-products.json#row='+str(row)) if row in live and raw else ('../20261006-added-active-pdp/records.json#row='+str(row))
    notes=[]
    for key,keys in {'neck':['NECKCOLLOR'],'sleeve':['SLEEVE'],'opening':['OPENING'],'hem':['HEMLINE','HEMLINE BOTTOM'],'pocket':['POCKET'],'waist':['WAIST'],'leg':['LEG']}.items():
        value=next((src[k] for k in keys if src.get(k)),None)
        if value:attrs[key]=value
    if row in (293,294,295):x['source_kind']='live_product'
    intro,detail,style,pid=x['after'].split('\n\n')
    desc=intro+'\n\n'+detail
    plural=f['noun'] in {'trousers','shorts','culottes','pyjama bottoms','track pants'}
    pronoun='They' if plural else 'It';have='have' if plural else 'has'
    fabric_fixes={121:('95% cotton and 5% elastane','96% cotton and 4% elastane'),122:('95% cotton and 5% elastane','96% cotton and 4% elastane'),169:('100% organic cotton','100% cotton'),179:('5% ellastane','5% elastane')}
    if row in fabric_fixes:
        old,new=fabric_fixes[row];desc=desc.replace(old,new);f['fabric']=f['fabric'].replace(old,new)
        notes.append({'kind':'fabric_correction','old':old,'new':new,'source_ref':source_ref})
    if row in (255,256):
        desc=desc.replace('The woven fabric is 99% cotton and 1% Lycra.','The shirt is made from woven cotton fabric.')
        f['fabric']='cotton'
        if row==255:
            desc=desc.replace('green striped shirt','green patterned shirt');f['pattern']='PATTERN'
        notes.append({'kind':'conflicting_source_neutralised','detail':'Removed precise blend percentages; current title and composition disagree.'})
    if row in (110,111):
        pattern='striped' if row==110 else 'printed'
        desc=desc.replace(f['colour']+' jumpsuit',f['colour']+' '+pattern+' jumpsuit')
        notes.append({'kind':'restored_pattern','source':src['PRINT'],'source_ref':source_ref})
    if row in (52,53,81,84,85,86,87):
        desc=desc.replace('The woven fabric is','The fabric is')
        notes.append({'kind':'unsupported_textile_claim_removed','detail':'Fabric blend supported; woven construction not explicitly sourced.'})

    # Replace imprecise or contradicted wording with the current source's fuller detail.
    replacements={
        'a shaped neckline':'a rounded V-neckline',
        'a half-open button placket':'a half-length button placket',
        'a two-button half placket':'a short two-button placket',
        'a half-open front':'a half-length front opening',
        'The design finishes with a straight hem with slits.':'The hem is straight, with slits.',
        'The design finishes with a straight hem with side slits.':'A straight hem with side slits completes the design.',
        'There is a button front, along with two front pockets.':'The front has buttons and two pockets.',
        'There is a button front, along with a front pocket.':'The front has buttons and a pocket.',
        'There is an open front, along with two front pockets.':'The front is open, with two pockets.',
    }
    if attrs['opening']=='FRONT OPEN':replacements['an open front']='a front opening'
    previous=item['facts']['attr']['sleeve']
    if attrs['sleeve']!=previous and previous in vocab['sleeve']:
        old_term=vocab['sleeve'][previous][0]
        if attrs['sleeve'] in vocab['sleeve'] and old_term in desc:
            replacements[old_term]=vocab['sleeve'][attrs['sleeve']][0]
    for old,new in replacements.items():
        if old in desc:desc=desc.replace(old,new);notes.append({'kind':'wording_or_source_precision','old':old,'new':new})
    desc=desc.replace('There is a front opening, along with a front pocket.','The front has an opening and a pocket.')
    # Avoid a repeated reference to the same wide-leg shape.
    if row==146:
        desc=desc.replace('They have an elasticated drawstring waist and wide legs.','They have an elasticated drawstring waist.')
        notes.append({'kind':'duplicate_feature','detail':'Removed the second wide-leg reference.'})
    if attrs['waist']=='ELASTICATED WAIST WITH SIDE DRAWSTRINGS':
        desc=desc.replace('an elasticated drawstring waist','an elasticated waist with side drawstrings')
        notes.append({'kind':'source_detail','detail':'Specified side drawstrings.'})
    intro,detail=desc.split('\n\n')
    missing=[]
    for key in ('neck','sleeve','opening','hem','pocket','waist'):
        val=attrs[key]
        if val in vocab.get(key,{}):
            term,pattern=vocab[key][val]
            if not re.search(pattern,desc,re.I):
                missing.append((key,val,term))
    # Shape and fastening details add useful substance where the old mapping omitted them.
    if missing:
        sentences=[]
        for key,val,term in missing:
            sentences.append(f'{pronoun} {have} {term}.')
            notes.append({'kind':'restored_source_detail','attribute':key,'source':val,'rendering':term,'source_ref':source_ref})
        detail=' '.join(sentences)+' '+detail
    if attrs['opening']=='PULL ON' and not re.search(r'pull[ -]on|pulls on',intro+' '+detail,re.I):
        detail=f'{pronoun} {have} a pull-on design. '+detail
        notes.append({'kind':'restored_source_detail','attribute':'opening','source':'PULL ON','source_ref':source_ref})
    if attrs['opening'] in ('EMBROIDERED FRONT','COLOUR BLOCK','PLEATED FRONT'):
        explicit={'EMBROIDERED FRONT':'Embroidery details the front of the blouse.','COLOUR BLOCK':'Colour-block detailing adds contrast to the design.','PLEATED FRONT':'Pleats add detail to the front of the blouse.'}[attrs['opening']]
        intro=intro.rsplit('. ',1)[0]+'. '+explicit
        notes.append({'kind':'replaced_generic_or_misleading_surface','source':attrs['opening'],'source_ref':source_ref})
    # Missing care: use only the instructions explicitly provided by the source.
    if not re.search(r'\b(?:Machine|Hand) wash',detail):
        raw_text=html.unescape(re.sub('<[^>]+>',' ',raw)).lower()
        if 'machine wash cold' in raw_text:
            care='Machine wash cold and wash dark colours separately.'
            if 'no bleach' in raw_text:care+=' Do not bleach.'
            if 'remove promptly' in raw_text:care+=' Remove promptly.'
            if 'dry in shade' in raw_text:care+=' Dry in the shade.'
        elif p.get('Wash Care Instruction (product.metafields.custom.wash_care_instruction)','').lower()=='machine wash':care='Machine wash.'
        else:care=''
        if care:detail+=' '+care;notes.append({'kind':'restored_care','source_ref':source_ref})
    # Abstract fit-led openings are replaced with fabric and fit facts.
    m=re.match(r'(A|An) (.+?) (?:shapes|defines) (this|these) (.+?)\.',intro)
    if m:
        fit=m.group(1).lower()+' '+m.group(2);subject=m.group(3)+' '+m.group(4)
        old_first,rest=intro.split('. ',1)
        fabric_sentence,rest=rest.split('. ',1)
        mode='woven' if 'woven fabric' in fabric_sentence else 'knit' if 'knit fabric' in fabric_sentence else ''
        material=f['fabric'].replace('tencel','Tencel')
        verb='are' if plural else 'is'
        construction={'woven':'woven','knit':'knitted','':'made'}[mode]
        subject_cap=subject[0].upper()+subject[1:]
        candidates=[f'{construction.capitalize()} from {material}, {subject} {have} {fit}.',f'{subject_cap} {verb} {construction} from {material} and {have} {fit}.',f'{subject_cap} {have} {fit} and {verb} {construction} from {material}.']
        candidate=next((c for c in candidates if c not in used_first),candidates[0])
        intro=candidate+' '+rest
        notes.append({'kind':'natural_opening','old':old_first+'.','new':candidate})
    if row==219:
        intro=intro.replace('The woven fabric is 100% linen.','The fabric is 100% linen.')
        notes.append({'kind':'unsupported_textile_claim_removed','detail':'Export supports linen, but does not explicitly identify woven construction.'})
    if intro.startswith('Cut in ') and 'sleeveless cut' in intro.split('. ')[0]:
        intro=intro.replace('a sleeveless cut','a sleeveless design',1)
        notes.append({'kind':'repeated_cut_word'})
    # Consistent fibre naming; avoid unhelpful repeated instructions in styling notes.
    intro=intro.replace('tencel','Tencel')
    if row in (293,294,295):
        intro=intro.replace('It works with pieces already in your wardrobe.','The plain fabric works with both jeans and tailored trousers.')
    if row==293:
        style=style.replace('A light jacket adds another layer without hiding the rounded hem.','Add a light jacket when you want an extra layer.')
        notes.append({'kind':'styling_precision','detail':'Removed unsupported promise that a jacket will not hide the hem.'})
    # Consolidate added source details into sentences rather than a series of It has lines.
    prefix=[]
    while detail.startswith(pronoun+' '+have+' ') and '. ' in detail:
        sentence,rest=detail.split('. ',1)
        prefix.append(sentence[len(pronoun+' '+have+' '):]);detail=rest
    if prefix:
        prefix=[part for phrase in prefix for part in phrase.split(' and ')]
        groups=[prefix[i:i+3] for i in range(0,len(prefix),3)]
        joined=[]
        for group in groups:
            phrase=group[0] if len(group)==1 else ' and '.join(group) if len(group)==2 else ', '.join(group[:-1])+' and '+group[-1]
            joined.append(f'{pronoun} {have} {phrase}.')
        detail=' '.join(joined)+' '+detail
    detail=detail.replace('a mid-rise waist, a drawstring waist and straight legs','a mid-rise waist with a drawstring and straight legs')
    first_overrides={
        18:"This women's maroon checked blouse has a boxy fit, a shirt collar and extended three-quarter sleeves with cuffs.",
        51:"This women's blue printed blouse has a regular fit, a round neckline and extended short sleeves with ties.",
        91:"This women's light green printed dress has a regular fit, a shirt collar and short sleeves with folded cuffs.",
        130:"These women's white trousers have a regular fit, straight legs and an elasticated waist with side drawstrings.",
    }
    if row in first_overrides:intro=first_overrides[row]+' '+intro.split('. ',1)[1]
    if row in (10,94):
        care=re.search(r'(?:Machine|Hand) wash.*$',detail)
        new_details={10:'It has a rounded V-neckline, extended short sleeves and a front yoke. The hem is straight.',94:'The sleeveless design has a round front neckline and a V-shaped back. It pulls on over the head and has a straight, folded hem. Side-seam pockets complete the design.'}
        detail=new_details[row]+(' '+care.group(0) if care else '')
    new='\n\n'.join([intro,detail.strip(),style,pid])
    x['after']=new;x['words']=len(new.split('Product ID:')[0].split())
    used_first.add(intro.split('. ')[0]+'.')
    if new!=item['after']:
        changes.append({'row':row,'code':x['code'],'before':item['after'],'after':new,'reasons':notes})
    after.append(x)
    field_evidence.append({'row':row,'source_ref':source_ref,'attributes':attrs})
(R/'revised.json').write_text(json.dumps(after,ensure_ascii=False,indent=2),encoding='utf-8')
(R/'changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf-8')
(R/'field-evidence.json').write_text(json.dumps(field_evidence,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'rows':len(after),'changes':len(changes),'reason_counts':dict(collections.Counter(r['kind'] for c in changes for r in c['reasons'])),'words':[min(x['words'] for x in after),statistics.median(x['words'] for x in after),max(x['words'] for x in after)]},indent=2))
