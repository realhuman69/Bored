#!/bin/bash

# Navigate to your local GitHub repository
cd /home/shayan/Desktop/programs/Bored || exit

# Check for changes in the folder
if [ -n "$(git status --porcelain)" ]; then
    # Add all changes to staging
    git add .

    # Commit changes with a message
    git commit -m "Auto-upload $(date)"

    # Push changes to the remote repository
    git push origin main  # Change 'main' to 'master' if your default branch is named 'master'
else
    echo "No changes to upload."
fi
