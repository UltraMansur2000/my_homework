import sys
import os

if sys.argv[1] == '-d':
    os.chdir(os.path.join(os.getcwd(), input("Folder path name(folder name/if none don't press anything):")))
    try:
        os.mkdir(sys.argv[2])
        print('Directory was created!')
    except FileExistsError:
        print('Directory already exists or wrong path. Try again!')
elif sys.argv[1] == '-f':
    os.chdir(os.path.join(os.getcwd(), input("Folder path name(folder name/if none don't press anything):")))
    try:
        with open(sys.argv[2], 'x') as f:
            print('File was created!')
    except FileExistsError:
        print('File already exists or wrong path. Try again')
