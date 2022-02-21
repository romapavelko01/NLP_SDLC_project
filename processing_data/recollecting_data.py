"""
Since json-file was unstructured and built-in python library json coud not
properly open and process it, so I has to create this module to manually
'structurize' the contents of an initial json-file so that it will be easier to work with.
"""
import json


data = open('data/News_Category_Dataset_v2.json').readlines()
# the above file has a dictionary as a line, but those dicts are not contained in a list, [],
# nor are they separated by commas
new_data = [eval(line.replace('\n,\n', '')) for line in data]
final_dict = {"data": new_data}

with open('data/final_news_category_dataset.json', 'w') as ff:
    json.dump(final_dict, ff)

