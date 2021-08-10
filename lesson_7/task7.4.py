import os
import sys

try:
    files = {}
    for a, b, c in os.walk(os.path.join(os.getcwd(), sys.argv[1])):
        for i in c:
            print(i)
            size = os.stat(os.path.join(a, i)).st_size
            if files.get('1' + '0' * len(str(size))) is None:
                files['1' + '0' * len(str(size))] = 1
            else:
                files['1' + '0' * len(str(size))] += 1
    print(files)
except Exception:
    print('Try to start from Terminal with foldername')
