import json
import os
import sys

merged_data = {}
dir = sys.argv[1]

for file_name in os.listdir(os.path.join("input",dir)):
    with open(os.path.join("input",dir,file_name), 'r') as f:
        data = json.load(f)
        merged_data.update(data)

with open(os.path.join("output",dir + '.json'), 'w') as f:
    json.dump(merged_data, f,indent=4)
