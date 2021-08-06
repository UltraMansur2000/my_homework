import sys
import shutil

try:
    shutil.copytree(sys.argv[1], sys.argv[2])
except Exception:
    print('Try to start from Terminal and enter copy_folder, enter_folder')
