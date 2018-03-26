import mechanize
import os
from time import sleep
br = mechanize.Browser()

br.open('http://downloads.dbpedia.org/current/core-i18n/en/')

f=open("source.html","w")
f.write(br.response().read())

filetypes=[".ttl.bz2"]
myfiles=[]
for l in br.links():
    for t in filetypes:
        if t in str(l):
            myfiles.append(l)


def downloadlink(l):
    f=open(l.text,"w")
    br._factory.is_html = True
    br.follow_link(l)
    f.write(br.response().read())
    print l.text," is downloaded. Extracting..."
    os.system("bzip2 -dk " + l.text)
    os.system("rm " + l.text)

for l in myfiles:
    sleep(1) # sleep so to let the server breath
    downloadlink(l)


print "making dbpedia.ttl ..."
os.system("cat *.ttl > a.ttt")
os.system("rm source.html")
os.system("rm *.ttl")
os.system("mv a.ttt DBpedia.ttl")
print "DBpedia.ttl  is created. have fun!"