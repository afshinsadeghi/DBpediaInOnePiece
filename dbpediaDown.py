import mechanize
import os
from time import sleep
import requests

br = mechanize.Browser()

br.open('http://downloads.dbpedia.org/current/core-i18n/en/')

f = open("source.html", "w")
f.write(br.response().read())

filetype = ".ttl.bz2"
myfiles = []
for l in br.links():
    if filetype in str(l):
        myfiles.append(l)


def download_big_file(l):
    local_filename = l.text
    r = requests.get(str(l), stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    print local_filename, " is downloaded. Extracting..."
    os.system("bzip2 -d " + l.text)


for l in myfiles:
    sleep(5)  # sleep so to let the server breath
    download_big_file(l)

print "making dbpedia.ttl ..."
os.system("cat *.ttl > a.ttt")
os.system("rm source.html")
os.system("rm *.ttl")
os.system("mv a.ttt DBpedia.ttl")
print "DBpedia.ttl  is created. have fun!"
