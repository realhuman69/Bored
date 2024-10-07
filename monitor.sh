#!/bin/bash

# Navigate to your local GitHub repository
cd /home/shayan/Desktop/programs/Bored || exit

# Monitor for changes
inotifywait -m -r -e modify,create,delete --format '%w%f' . | while read FILE
do
    echo "Change detected in $FILE"
    ./auto_upload.sh  # Run your upload script
done
