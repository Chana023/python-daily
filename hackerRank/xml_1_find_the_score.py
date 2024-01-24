# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    count=0
    for _ in node.iter():
        if _.attrib:
            count+=len(_.attrib)
    return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(root)