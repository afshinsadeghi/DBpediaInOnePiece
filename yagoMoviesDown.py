import os
from time import sleep
import requests

querysub0 = 'https://linkeddata1.calcul.u-psud.fr/sparql?default-graph-uri=&query=construct%7B+%3Fs+%3Fp+%3Fo%7D+where+%7B+%0D%0Aselect+distinct+%3Fs+%3Fp+%3Fo+where+%7B%0D%0A%7B%0D%0A%3Fs1+++%3Chttp%3A%2F%2Fyago-knowledge.org%2Fresource%2FactedIn%3E+++%3Fs+.%0D%0A%3Fs2+++%3Chttp%3A%2F%2Fyago-knowledge.org%2Fresource%2Fdirected%3E+++%3Fs+.%0D%0A%3Fs+++%3Fp+++%3Fo.%0D%0A%7D+Union%7B%0D%0A%3Fs+++%3Chttp%3A%2F%2Fyago-knowledge.org%2Fresource%2FactedIn%3E+++%3Fs3+.%0D%0A%3Fs4+++%3Chttp%3A%2F%2Fyago-knowledge.org%2Fresource%2Fdirected%3E+++%3Fs3+.%0D%0A%3Fs+++%3Fp+++%3Fo.%0D%0A%7D+Union%7B%0D%0A%3Fs7+++%3Chttp%3A%2F%2Fyago-knowledge.org%2Fresource%2FactedIn%3E+++%3Fs5+.%0D%0A%3Fs+++%3Chttp%3A%2F%2Fyago-knowledge.org%2Fresource%2Fdirected%3E+++%3Fs5+.%0D%0A%3Fs+++%3Fp+++%3Fo.%7D+%0D%0A%7D%0D%0ALimit+10000+offset+'
querysub1 = '+%7D%0D%0A&format=text%2Fplain&timeout=0'

def download_big_file(counter):
    link = querysub0 + str(counter * 10000) + querysub1
    local_filename = "YagoMovie" + str(counter) + ".nt"
    r = requests.get(link, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
    print local_filename, " is downloaded."

for counter in range(1, 700, 1):
    sleep(10)  # sleep so to let the server breath
    download_big_file(counter)

print "making yagoMovies.nt ..."
os.system('find . -name "*.nt" -size -15 -delete')
os.system("cat *.nt > a.ntt")
os.system("rm *.nt")
os.system("mv a.ntt yagoMovies.nt")
print "yagoMovies.nt  is created. have fun!"
