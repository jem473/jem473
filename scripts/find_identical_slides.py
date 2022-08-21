'''Little script to remove identical images in a designated directory
if they also exist in a source directory.'''

from os import listdir, remove
from os.path import join
from PIL import Image
import imagehash

SOURCE_PATH = './Original/'
REMOVAL_PATH = './New/'
FILETYPE = '.png'

def main():
    original_hashes = [imagehash.average_hash(Image.open(join(SOURCE_PATH, f))) for f in listdir(SOURCE_PATH) if f.endswith(FILETYPE)]

    for f in (filename for filename in listdir(REMOVAL_PATH) if filename.endswith(FILETYPE)):
        complete_path = join(REMOVAL_PATH, f)

        if imagehash.average_hash(Image.open(complete_path)) in original_hashes:
            remove(complete_path)

if __name__ == "__main__":
    main()
