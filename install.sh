#!/bin/bash

current="$(dirname "$0")"
echo "$current"
python3 -m pip install -r "$current"/pip.txt

conf_dir=~/etc/supervisor/conf.d/
test -d $conf_dir || mkdir -p $conf_dir
sed -i "s/\${deploy.path}/$current/" moehira.conf

cp "$current"/moehira.conf $conf_dir

supervisorctl reread
supervisorctl restart moehira
