#!/bin/bash
# shellcheck disable=SC2155

export FLASK_APP=$(dirname "$0")/server/server.py
python3 -u -m flask run -h 0.0.0.0 -p 41401
