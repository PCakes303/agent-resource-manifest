import json,re,sys
from pathlib import Path
ID=re.compile(r"^[a-z0-9][a-z0-9._/-]{2,127}$"); KINDS={"tool","skill","model","dataset","service","resource"}
def validate(d):
 e=[]
 if not isinstance(d,dict): return ["manifest must be an object"]
 for k in ("manifest_version","id","kind","name","version"):
  if not isinstance(d.get(k),str) or not d[k].strip(): e.append(k+" must be a non-empty string")
 if d.get("manifest_version")!="1.0": e.append("manifest_version must be 1.0")
 if isinstance(d.get("id"),str) and not ID.fullmatch(d["id"]): e.append("invalid id syntax")
 if d.get("kind") not in KINDS: e.append("unsupported kind")
 for k in ("permissions","dependencies"):
  v=d.get(k,[])
  if not isinstance(v,list) or any(not isinstance(x,str) or not x for x in v): e.append(k+" must be an array of non-empty strings")
  elif len(v)!=len(set(v)): e.append(k+" contains duplicates")
 x=d.get("integrity")
 if x is not None and (not isinstance(x,dict) or x.get("algorithm") not in {"sha256","sha384","sha512"} or not isinstance(x.get("digest"),str) or not x["digest"]): e.append("invalid integrity block")
 return e
if __name__=="__main__":
 p=Path(sys.argv[1]) if len(sys.argv)>1 else Path("examples/tool-resource.json")
 try: d=json.loads(p.read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError) as x: print(x,file=sys.stderr); sys.exit(2)
 e=validate(d)
 if e: print("\n".join(e),file=sys.stderr); sys.exit(1)
 print("valid resource manifest: "+d["id"])
