# DBPediaDownloder

This code creates a single dbpedia.ttl of the last dbpedia.

## How it works:

This code downloads and extracts and merges all ttl files of the current version of DBpedia into one file
 with name dbpedia.ttl


## How to use it:

 1. Make > 300 GB of free disk space on your disk

 2. Install bzip2 on your system

 3. Install these python packages: "requests" "mechanize" "subprocess" ,"time"
 
 virtualenv env
 source env/bin/activate
 pip install requests
 pip install mechanize
 pip install subprocess
 pip install time
 
 4. Run as:   python dbpediaDown.py
 
## Questions? find me @:

http://afshn.com

http://sda.cs.uni-bonn.de/people/afshin-sadeghi/

https://scholar.google.com/citations?user=uWTszVEAAAAJ&hl=en&oi=ao

### other datases

Linkedmdb movie dataset:

http://www.cs.toronto.edu/~oktie/linkedmdb/

dbpedia movie subset:
to create that run dbpediaMoviesDown.py


