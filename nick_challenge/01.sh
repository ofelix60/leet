ls -lh /Users/oscar/Desktop/foo/content | awk '{print $9,$5}'

# or

find /Users/oscar/Desktop/foo/content -type f -exec du -ah {} \;


