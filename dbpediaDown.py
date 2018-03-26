import mechanize
from subprocess import call
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
    br.click_link(l)
    f.write(br.response().read())
    print l.text," is downloaded."
    call(["bzip2 - d", l.tex])


for l in myfiles:
    sleep(1) # sleep so to let the server breath
    downloadlink(l)

call(["rm *.bz2"])
call(["cat *.ttl > a.ttt"])
call(["rm *.ttl"])
call(["mv a.ttt DBpedia.ttl"])