import os
import inspect
import json

filePath = "../../resources/sfi.json"

class Dummy:
    pass

baseDir = os.path.dirname(inspect.getabsfile(Dummy))

sfi = []
with open(os.path.join(baseDir, filePath)) as f:
    sfi = json.loads(f.read())


