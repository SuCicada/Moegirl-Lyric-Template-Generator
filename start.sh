#!/bin/bash

FLASK_APP=$(dirname "$0")/server.py flask run -h 0.0.0.0 -p 41401 