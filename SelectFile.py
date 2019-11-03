import os
import re
import sys

if __name__ == "__main__":
    args = sys.argv
    for i in range(1, len(args)):
        url = "https://github.com/"
        hit = re.match(r'https://github.com/([\w\-]*/[\w\-]*)/([a-zA-Z0-9\-_/.]*)', args[i])
        try:
            url += hit.group(1)
            rec = re.match(r'\w*/master/([a-z_A-Z/0-9.]*)', hit.group(2))
            # /tree/master/ directory /blob/master/ file
            url += '/trunk/' + rec.group(1)
        except AttributeError:
            print("Error: The specified URL is invalid.")
        os.system('svn export ' + url)
        
