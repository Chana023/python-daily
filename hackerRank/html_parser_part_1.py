# https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

numberOfLines = int(input())
parser = MyHTMLParser()

for value in range(numberOfLines):
    
    line = input()
    parser.feed(line)