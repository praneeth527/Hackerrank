from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if len(attrs) > 0:
            for attr in attrs:
                print("->", attr[0], ">", str(attr[1]))

    def handle_startendtag(self, tag, attrs):
        print(tag)
        if len(attrs) > 0:
            for attr in attrs:
                print("->", attr[0], ">", str(attr[1]))


parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
