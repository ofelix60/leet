#!/bin/bash

if [ -f "/tmp/content.txt" ]; then
    echo "fdjlfdsjksf" >> /tmp/content.txt
    echo "append"
else
    echo "fdjlfdsjksf" >> /tmp/content.txt
    echo "created"
fi

# or

echo "fdjlfdsjksf" >> "/tmp/content.txt" || touch "/tmp/content.txt" && echo "created"
