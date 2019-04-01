#!/usr/bin/env python3

import sys
import time
import random
import string
import redis

SLEEP = 300 #5 minutes

def main ():
    """Redis Load main function"""
    host = input("Redis Hosts? [default: localhost] ")
    if not host:
        host = 'localhost'
    r = redis.Redis(host=host, port=6379, db=0)
    while True:
        key = randomString(10)
        try:
            print('Adding key: ', key)
            r.set(key, 'world')
            time.sleep(SLEEP)
        except KeyboardInterrupt:
            print('[x] Caught CRTL+C ... Exiting ...')
            sys.exit(0)

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

if __name__ == "__main__":
    main()
