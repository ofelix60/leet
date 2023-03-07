# given a directory path foo/content, output a list of all files and directories in this directory. include the size of the file or directory. do this in python and bash.

# could extend it in a second part and only include directories

#!/bin/bash

echo 'directories: '
find /Users/oscar/Desktop/foo/content -mindepth 1 -maxdepth 1 -type d -exec sh -c 'echo "$0 - $(du -sk "$0" | cut -f1)KB"' {} \;
echo 'files: '
find /Users/oscar/Desktop/foo/content -mindepth 1 -maxdepth 1 -type f -exec sh -c 'echo "$(basename "$0") - $(du -sk "$0" | cut -f1)KB"' {} \;
echo 'both: '
find /Users/oscar/Desktop/foo/content -mindepth 1 -maxdepth 1 -exec sh -c 'echo "$0 - $(du -sk "$0" | cut -f1)KB"' {} \;
