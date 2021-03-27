import os
import time
import string
# you dont know where you put one specify file? just put the path you want to search on 
class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

class search:
    def search_path(self):
        self.put = input('Enter the path you want to search:' )
        self.dirct = os.chdir(self.put)
        print(bcolors.GREEN + '[+[+[+ Searching +]+]+]')
        time.sleep(3)
        for dirpath, dirnames, filenames in os.walk(self.put):
            print('Current Path:', dirpath)
            print('Directories:', dirnames)
            print('Files:', filenames)
            print()

if __name__ == '__main__':
    show_info = search()
    show_info.search_path()