import sys
import os

sys.argv = list(range(3))
sys.argv[1] = "test.txt"
sys.argv[2] = "out.txt"
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# print(SCRIPT_DIR)
# sys.path.append(os.path.dirname(SCRIPT_DIR + "/../server"))

from app import main

main()
