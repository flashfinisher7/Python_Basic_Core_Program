import os
user_path = 'C:/'
for fname in os.listdir(user_path):
   path = os.path.join(user_path, fname)
   if os.path.isdir(path):
       # skip directories
       continue
   # print the file names
   print(fname)