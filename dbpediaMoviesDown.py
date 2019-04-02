import os
from time import sleep
import requests

querysub0 = 'http://dbpedia.org/sparql?default-graph-uri=http%3A%2F%2Fdbpedia.org&query=construct%7B+%3Fs+%3Fp+%3Fo%7D+where+%7B+%0D%0Aselect+distinct+%3Fs+%3Fp+%3Fo+where+%7B%0D%0A%7B%0D%0A%3Fs++%3Fp1+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2FFilm%3E+.%0D%0A%3Fs+++%3Fp+++%3Fo.%0D%0A%7D+Union%7B%0D%0A%3Fo3++%3Fp1+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2FFilm%3E+.%0D%0A%3Fs+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2Fstarring%3E++%3Fo3+.%0D%0A%3Fs+%3Fp+%3Fo+.%0D%0A%7D+Union%7B%0D%0A%3Fo3++%3Fp1+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2FFilm%3E+.%0D%0A%3Fs+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2Fdirector%3E++%3Fo3+.%0D%0A%3Fs+%3Fp+%3Fo+.%7D+%0D%0A%7D%0D%0ALimit+10000+offset+'
querysub1 = '+%7D%0D%0A&format=text%2Fplain&CXML_redir_for_subjs=121&CXML_redir_for_hrefs=&timeout=3000000&debug=on&run=+Run+Query+'

def download_big_file(counter):
    link = querysub0 + str(counter * 10000) + querysub1
    local_filename = "DBpediaMovie" + str(counter) + ".nt"
    r = requests.get(link, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    print local_filename, " is downloaded."

for counter in range(1, 500, 1):
    sleep(10)  # sleep so to let the server breath
    download_big_file(counter)

print "making dbpediaMovies.nt ..."
os.system('find . -name "*.nt" -size -15 -delete')
os.system("cat *.nt > a.ntt")
os.system("rm *.nt")
os.system("mv a.ntt dbpediaMovies.nt")
print "dbpediaMovies.nt  is created. have fun!"
