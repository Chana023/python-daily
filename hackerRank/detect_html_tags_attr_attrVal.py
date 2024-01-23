# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true

from html.parser import HTMLParser

class  MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        print(tag)

        for value in attrs:
            print(f'-> {value[0]} > {value[1]}')


numberOfLines = int(input())
parser = MyHTMLParser()

for value in range(numberOfLines):
    
    line = input()
    parser.feed(line)