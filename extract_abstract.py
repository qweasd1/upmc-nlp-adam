import xml.sax as sax
import gzip

class Parser(sax.ContentHandler):
    def __init__(self,output):
        self.is_catching = False
        self.output = output
        self.cache = []
    def startElement(self, name, attrs):
        if name == "AbstractText":
            self.is_catching = True

    def endElement(self, name):
        if name == "AbstractText":
            self.is_catching = False
            self.output.append("".join(self.cache))
            self.cache.clear()
    def characters(self,text):
        if self.is_catching:
            self.cache.append(text)


#
# with open("/Users/tony/Downloads/medline_xml.part5/medline17n0851.xml") as input_file:
#     with open("input.txt","w") as output:
#         sax.parse(input_file,Parser(output))


def extract_abstract(input_file_path):
    texts = []
    with gzip.open(input_file_path) as input_file:
        sax.parse(input_file, Parser(texts))
    return texts

# def parse(input_file_path,output_file_path):
#     with gzip.open(input_file_path) as input_file:
#         with open(output_file_path, "w") as output:
#             sax.parse(input_file, Parser(output))
#
# with gzip.open("/Users/tony/Downloads/medline_xml.part5/medline17n0863.xml.gz") as input_file:
#     with open("input_2.txt", "w") as output:
#         sax.parse(input_file, Parser(output))



# sax.parseString('<doc><AbstractText id="1">test</AbstractText><a>aa</a></doc>',Parser())

