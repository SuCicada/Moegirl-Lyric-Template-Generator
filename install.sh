#!/bin/bash
set -e

current="$(realpath "$(dirname "$0")")"
echo "$current"
python3 -m pip install -r "$current"/server/pip.txt

conf_dir=~/etc/supervisor/conf.d/
test -d $conf_dir || mkdir -p $conf_dir

cp "$current"/deploy/moehira.conf $conf_dir/moehira.ini

sed -i "s|\${deploy.path}|$current|g" $conf_dir/moehira.ini

~/bin/supervisorctl.sh update
~/bin/supervisorctl.sh restart moehira
