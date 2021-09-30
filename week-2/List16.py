from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/Desktop\Week-2') if isfile(join('/Desktop\Week-2', f))]
print(files_list);