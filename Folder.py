import os

# define the name of the directory to be created
path = "/tmp/year/month/week/day"

try:
    os.makedirs(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)
