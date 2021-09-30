import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("List16.py")))
print("Created: %s" % time.ctime(os.path.getctime("List16.py")))