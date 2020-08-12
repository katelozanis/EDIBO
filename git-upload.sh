#!/bin/bash

git config --global user.email katelozanis@gmail.com
git add .
git commit -m  "$(date '+%Y%m%d_%H_%M')_upload_from_cli"
git push origin master
