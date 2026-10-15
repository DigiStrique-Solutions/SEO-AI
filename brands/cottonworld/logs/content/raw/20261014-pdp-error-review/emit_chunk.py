import json, sys
from pathlib import Path
rows=json.loads((Path(__file__).parent/'revised.json').read_text(encoding='utf-8'))
start,end=map(int,sys.argv[1:3])
print(json.dumps([{'row':x['row'],'text':x['after']} for x in rows[start:end]],ensure_ascii=False))
