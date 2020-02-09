import urllib2
import bs4
import re

url = "https://endocode.com/about/"
response = urllib2.urlopen(url)

html = response.read()

soup = bs4.BeautifulSoup(html)

properties = soup.findAll('a', onclick=True)

members = {}
for eachproperty in properties:
    member_info = eachproperty['onclick'].encode("utf-8").replace("showTeamMember(", "").replace(")","").replace("'", "").split(",")
    members[member_info[0]] = {}
    members[member_info[0]]['title'] = member_info[1]
    members[member_info[0]]['desc'] = member_info[2]

from collections import OrderedDict

sorted_members = sorted(members.items(), key=lambda i: i)

# show the initial letter of the name of the endocoder, urllib2then surname, then
# title and finally bio, sorted surname. Show exclusively that information, extracted from the website, and in
# that sorting.

for member,info in sorted_members:
    print(member[:1] + "\t" + member + "\t" + info['title'] + "\t" + info['desc'])


             