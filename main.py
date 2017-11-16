from extract_from_adam import parse_from_adam
from extract_abstract import extract_abstract
from adam_parser import parse_from_abstract
from generate_xml import generate_xml

import os
result = {}

print("[start] adam")
parse_from_adam("adam_database.txt",result)
print("[end] adam")

print("[start] medline")
# change here to use another root of all medline data
medline_root = "/Users/tony/Downloads/medline_xml.part5"
medline_files = [os.path.join(medline_root,file_name) for file_name in os.listdir(medline_root) if file_name.endswith(".gz")]
for index,file_path in enumerate(medline_files):
    texts = extract_abstract(file_path)
    parse_from_abstract(texts,result)
    print("file {0} processed".format(index+1))

print("[end] medline")

print("[start] generate xml")
generate_xml(result,"abbr_sense.xml")
print("[end] generate xml")


