import os
total_size = 0
start_path = '/Users/judewang/Work/ct152-mobile/src'  # To get size of current directory
for path, dirs, files in os.walk(start_path):
    for f in files:
        fp = os.path.join(path, f)
        if f.endswith('jpg') or f.endswith('png'):
            total_size += os.path.getsize(fp)
print("Directory size: " + str(total_size * 1.0 / 1024 / 1024) + "  MB")