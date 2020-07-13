import os
import shutil
f = open('/Users/judewang/Work/ct152-mobile/images.txt', 'r')
for line in f:
    name = line.split('/')[-1].strip()
    shutil.copyfile('/Users/judewang/Work/ct152-mobile/' + line.strip(), '/Users/judewang/Random/scripts/compressed_images/' + name)
