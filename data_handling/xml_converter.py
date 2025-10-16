import sys
import xml.etree.ElementTree as ET
def read_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    print("Root tag:", root.tag)
    print("Child tags:", [child.tag for child in root])
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python xml_converter.py <path-to-xml>")
    else:
        read_xml(sys.argv[1])
