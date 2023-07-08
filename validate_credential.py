import sys
import json

args = sys.argv[1:]

mapper_raw = json.load(open('./keys/mapper.json', 'r'))
mapper = {sub_v:k for k, v in mapper_raw.items() for sub_v in v}
