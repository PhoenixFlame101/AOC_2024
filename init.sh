#!/bin/sh

highest=$(ls -1 | sort -r | sed -n '2p')
new_directory=$((highest + 1))

mkdir "$new_directory"
cd "$new_directory" || exit

touch "${new_directory}.py"
touch "file.in"
touch "sample.in"
