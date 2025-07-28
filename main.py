import time
from sites.bugcrowd import run_background_checker

while True:
    run_background_checker()
    time.sleep()