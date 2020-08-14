#!/bin/bash

git config --global user.email katelozanis@gmail.com
git add .
git commit -m  "$(date '2020200814')_upload_from_cli"
git push origin master
