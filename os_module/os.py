import os
from datetime import datetime

# list all methods in os module
# print(dir(os))

# print working directory
# print(os.getcwd())
# output --> /Users/oscar/Desktop/-py/os_module

# Navigate to location in file system
os.chdir("/Users/oscar/Desktop")
# # print(os.getcwd())

# # see files/directories in location
# #   - default: current dir
# #   - pass in path
# print(os.listdir())

# # create directory
# # os.mkdir("OS-Demo-2")
# # or for nested directories
# os.mkdirs("OS-Demo-2/Sub-Dir-1")

# # Deleting Folders (same as above one v nested) BE CAREFULL WHEN DELETING RECURSIVELY
# # os.rmdir()
# os.removedirs("OS-Demo-2/Sub-Dir-1")


# # Renaming files
# os.rename('originalFileName.txt', "newFileName.txt")

# looking at file information
# print(os.stat("rfi").st_size)
# mod_time = os.stat("rfi").st_mtime

# print(datetime.fromtimestamp(mod_time))

# traverse directory tree
# returns path/directories in path/files in path
# for dirpath, dirnames, filenames in os.walk("/Users/oscar/Desktop/foo/content"):
#     print("Current path: ", dirpath)
#     print("Directories: ", dirnames)
#     print("Files: ", filenames)
#     print()


# access enviornment variables
# lists all env vars
# print(os.environ)
# get specific dir
# print(os.environ.get("HOME"))

# create new file in HOME dir


# PATH

# os.path module has useful methods for paths
# os.path.join() joins paths
# file_path = os.path.join(os.environ.get("HOME"), "test.txt")

# gets base name (file name in this case)
# print(os.path.basename("/tmp/test.txt"))

# gets base dir (tmp dir in this case)
# print(os.path.dirname("tmp/test.txt"))

# both dir and basefile (return tuple with both)
# print(os.path.split("/tmp/test.txt"))

# check if a path exists
# print(os.path.exists("/tmp/text.txt"))

# check if object is dir or file
# print(os.path.isdir("/tmp/asdf"))
# print(os.path.isfile("/tmp/sdfa"))

# split file root and extension (test.txt --> test .txt)
# print(os.path.splitext("/tmp/test.txt"))
