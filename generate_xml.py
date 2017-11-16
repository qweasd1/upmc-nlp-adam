import lxml.etree
import lxml.builder    
from collections import Counter

E = lxml.builder.ElementMaker()


ROOT = E.abbrs
ABBR = E.abbr
SENSE = E.sense




def generate_xml(abbrs,output_file_path):
    abbrs = {abbr:Counter(longs).most_common() for abbr,longs in abbrs.items()}
    sorted(abbrs.items(), key=lambda x: x[0])

    doc = ROOT(
        *[ABBR(
            *[SENSE(long, freq=str(freq)) for long, freq in longs if long.strip()],
            name=abbr
        ) for abbr, longs in sorted(abbrs.items(), key=lambda x: x[0]) if abbr.isalpha()]
    )

    with open(output_file_path, "w") as output:
        output.write(lxml.etree.tostring(doc, pretty_print=True).decode('utf-8'))


generate_xml({
    "aa":{
        "bb":3
    }
},"test.xml")













