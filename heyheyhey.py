import requests
from bs4 import BeautifulSoup
import re
s = requests.session()
s.get("http://www.porch.com")

protype = ['Plumbers','Electricians','HVAC Contractors', 'Roofers', 'General Contractors','Painters','Carpenters','Flooring Contractors','Landscapers']
location = ['Houston%252C%2520TX&zip=77002&lat=29.7601927&lon=-95.36938959999998', 'Beverly%2520Hills%252C%2520CA&zip=90210&lat=34.0736204&lon=-118.4003563', 'New%2520York&zip=32724&lat=29.0281855&lon=-81.2878341','Chicago%252C%2520IL&zip=60604&lat=41.8781136&lon=-87.62979819999998','Miami%252C%2520FL&zip=33136&lat=25.7890972&lon=-80.20404350000001','Los%2520Angeles%252C%2520CA&zip=90012&lat=34.0522342&lon=-118.2436849','Dallas%252C%2520TX&zip=75202&lat=32.7801399&lon=-96.80045109999998','Jacksonville%252C%2520FL&zip=32202&lat=30.3321838&lon=-81.65565099999998','http://porch.com/search/results?q=roofers&loc=San%2520Diego%252C%2520CA&zip=92101&lat=32.715738&lon=-117.16108380000003','loc=Indianapolis%252C%2520IN&zip=46204&lat=39.768403&lon=-86.15806800000001']
for x, y in [(x,y) for x in protype for y in location]:
    url = "http://porch.com/search/results?q=%s&loc=%s" % (x, y)
    source = s.get(url)
    soup = BeautifulSoup(source.content)
    #name = soup.findAll("div",{"class":"search-results-pro-info"})
    info = []
    bizname = soup.findAll("a",{"class":"search-result-pro-name pro-profile-link"})
    for biz in bizname:
           info.append(re.sub("\n\s*"," ",biz.text))
    companytype = soup.findAll("span",{"class":"company-type"})
    for company in companytype:
           info.append(re.sub("\n\s*"," ",company.text))
    citystate = soup.findAll("span",{"class":"city-state"})
    for city in citystate:
           info.append(re.sub("\n\s*"," ",city.text))
    print "\"" + "\"\n\"".join(info) + "\"\n"
