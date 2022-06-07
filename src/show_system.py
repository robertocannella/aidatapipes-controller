
import json
from services import mongodb_service as db

with open("system.json", 'r') as f:
  data = json.load(f)   #print(data['system']['id'])


system = db.getOrAddSystem(data['system']['systemId'])

zone_index = 1
line_type = "lineRT"
degF = 90.9



json_formatted_str = json.dumps(data, indent=2)     #print(json_formatted_str)

#db.addHydroZoneData(system_id,zone_index,line_type,degF)

