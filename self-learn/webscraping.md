
04/01/2021

Try to do a better job at writing down your questions during the week and submit them to Gaz before Thursday. 

What encompasses state and behaviours?
Can we do some demonstrations of how to use super()?
Composite/Component classes
Practice with Decorators? I still don't quite understand these. 
Static vs Class Methods - I don't really understand the difference. Both are called from a class but I think I just need some more examples of implementation. 

04/13/2021
# Webscraping

Hallie asked me to scrap some images off a website and show her how. 

There are a couple of ways to do it. 

## Here is an incomplete python-ic way.

I found the below script on stackoverflow:'
pulled from: https://stackoverflow.com/questions/18408307/how-to-extract-and-download-all-images-from-a-website-using-beautifulsoup

```python
import requests
import re
from bs4 import BeautifulSoup

site = 'http://www.accu-climemechanicalservices.com/'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls:
    print(url)
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
        print("Regex didn't match with the url: {}".format(url))
        continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)
```

This pulls images off of that one page give as the site...but how do I navigate to all pages?

Bion shared with me this article: [https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python]


## The other way
Bion showed me how to create a copy of an entire website w/ `wget`

What is wget?
A package for retrieving files using HTTP, HTTPS, FTP and FTPS, the most widely used Internet protocols. It is a non-interactive commandline tool, so it may easily be called from scripts, cron jobs, terminals without X-Windows support, etc.

full command used:
`wget --mirror --convert-links --adjust-extension --page-requisites --no-parent http://www.accu-climemechanicalservices.com/`

06/14/2021
- Make app that is downloaded onto your computer.
- Timer app
  -  20/20/20. 
      - Every 20 minutes, look 20 meters away for 20 seconds. 
  - Pomodoro Timer
  - 
