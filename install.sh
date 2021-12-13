#!/bin/bash

current="$(dirname "$0")"
pip3 install -r "$current"/pip.txt
cp "$current"/moehira.conf ~/etc/supervisor/conf.d/
# supervisorctl moehira restart