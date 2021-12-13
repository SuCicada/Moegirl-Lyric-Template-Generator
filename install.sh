#!/bin/bash

current="$(realpath "$(dirname "$0")")"
echo "$current"
python3 -m pip install -r "$current"/pip.txt

conf_dir=~/etc/supervisor/conf.d/
test -d $conf_dir || mkdir -p $conf_dir

cp "$current"/moehira.conf $conf_dir/moehira.conf

sed -i "s/\${deploy.path}/$current/" $conf_dir/moehira.conf

supervisorctl reread
supervisorctl restart moehira
