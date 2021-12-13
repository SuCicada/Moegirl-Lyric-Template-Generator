#!/bin/bash

current="$(dirname "$0")"
echo "$current"
python3 -m pip install -r "$current"/pip.txt
cp "$current"/moehira.conf ~/etc/supervisor/conf.d/
# supervisorctl moehira restart
