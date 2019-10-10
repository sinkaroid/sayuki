#!python
#!C:\Python37\python.exe
import requests
from colorama import Fore, Back, Style
import feedparser
import webbrowser

print(Fore.RED)
print("""
 __                   _    _ 
/ _\ __ _ _   _ _   _| | _(_)
\ \ / _` | | | | | | | |/ / |
_\ \ (_| | |_| | |_| |   <| |
\__/\__,_|\__, |\__,_|_|\_\_|
          |___/ hentai-fetcer
""")
print(Style.RESET_ALL)
print ("Latest content:\n")

feed = feedparser.parse("https://www.underhentai.net/feed/")

feed_entries = feed.entries

for entry in feed.entries:

    article_title = entry.title
    article_link = entry.link
    
    content = entry.summary
    print ("{} -> [{}]".format(Fore.GREEN + article_title, article_link + Style.RESET_ALL))
 