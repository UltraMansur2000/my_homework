import os
import sys

files = {}
try:
    for a, b, c in os.walk(os.path.join(os.getcwd(), sys.argv[1])):
        for i in c:
            size = os.stat(os.path.join(a, i)).st_size
            if files.get('1' + '0' * len(str(size))) is None:
                files['1' + '0' * len(str(size))] = [1, {f'.{i.split(".")[-1]}'}]
            else:
                files['1' + '0' * len(str(size))][0] += 1
                files['1' + '0' * len(str(size))][1].add(f'.{i.split(".")[-1]}')
    for a, b in (files.items()):
        files[a] = tuple((b[0], list(b[-1])))
    print(files)
except Exception:
    print('Try to start from Terminal with folder name')
