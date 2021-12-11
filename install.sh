#!/bin/bash

current="$(dirname "$0")"
echo "$current"
python3 -m pip install -r "$current"/pip.txt
echo "${PASSWORD}" | sudo -S -v
echo "${PASSWORD}"
sudo cp "$current"/moehira.conf /etc/supervisor/conf.d/
# sudo supervisor