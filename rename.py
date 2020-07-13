import os
folder = '/Users/judewang/Downloads/thumbnails/circle_thumbnails/no_border'
for filename in os.listdir(folder):
    if filename.startswith('lesson avatar'):
        new_name = folder + '/' + '_'.join(filename.split())
        # print(new_name)
        os.rename(folder + '/' + filename, new_name)