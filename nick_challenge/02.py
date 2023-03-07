# create a file containing the text "fdjlfdsjksf" at path /tmp/content.txt. if the file and directory does not already exist you should create it.

# another exercise same as the one above. but if the file already exists, you should append "fdjslaflkdjs" to the file (preserve any content already there)

import os

if os.path.exists("/tmp/content.txt"):
    with open("/tmp/content.txt", "a") as f:
        f.write("\nfdjlfdsjksf")
    print("append")
else:
    with open(os.path.join("/tmp/", "content.txt"), "a") as f:
        f.write("fdjlfdsjksf")
    print("created")
