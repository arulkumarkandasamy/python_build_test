#!/usr/bin/python

import yaml
import sys

repository_name = 'helloworld'
new_version = '0.1.31'

fname = repository_name + "values.yaml"

with open(fname) as f:
    dict_obj = yaml.load(f)

dict_obj["Image"]["version"] = new_version

with open(fname, "w") as f:
    yaml.dump(dict_obj, f)