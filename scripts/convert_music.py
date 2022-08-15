'''Basic script for converting FLAC files to a separate '''

import os
import subprocess

HQ_DIR = '/mnt/n0/Music'

def main():
    for root, _, files in os.walk(HQ_DIR):
        for name in files:
            if name.endswith('.flac'):
                old_file = os.path.join(root, name)
                new_root = root.replace(
                    HQ_DIR.split('/')[-1],
                    os.path.join('ConvertedMusic', 'M4A VBR')
                )
                new_name = name[:-4] + 'm4a'
                new_file = os.path.join(new_root, new_name)
                print(new_file)
                if not os.path.exists(new_root):
                    os.makedirs(new_root)
                if not os.path.exists(new_file):
                    command = [
                        'ffmpeg',
                        '-vn',
                        '-i',
                        old_file,
                        '-c:a',
                        'libfdk_aac',
                        '-vbr',
                        '5',
                        new_file
                    ]
                    subprocess.run(command)

if __name__ == "__main__":
    main()