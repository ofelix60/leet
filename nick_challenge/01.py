# given a directory path foo/content, output a list of all files and directories in this directory. include the size of the file or directory. do this in python and bash.

# could extend it in a second part and only include directories

import os

d = []
f = []
everything = []

for path, dirs, files in os.walk("/Users/oscar/Desktop/foo/content"):
    for directory in dirs:
        dir_name = os.path.join("/Users/oscar/Desktop/foo/content", directory)
        if os.path.exists(dir_name):
            d.append((f"{directory} - {os.stat(dir_name).st_size}KB"))

    for file in files:
        file_path = os.path.join("/Users/oscar/Desktop/foo/content", file)
        if os.path.exists(file_path):
            f.append((f"{file} - {os.stat(file_path).st_size}KB"))
            # print((f"{file} - {os.stat(dir_name).st_size}KB"))
    break

print("directories: ", d)
print()
print("files: ", f)
print()
everything = [d, f]
print("everything: ", everything)
