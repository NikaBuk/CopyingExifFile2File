import string
import exiftool
from glob import glob

folder_a_path = 'Python Photo Project/Folder A'
folder_b_path = 'Python Photo Project/Folder B'

files_fold_a = sorted(glob(f'{folder_a_path}/*'))
files_fold_b = sorted(glob(f'{folder_b_path}/*'))

#./exiftool -TagsFromFile Python\ Photo\ Project/Folder\ A/%f.%e -all:all Python\ Photo\ Project/Folder\ B/ -overwrite_original


