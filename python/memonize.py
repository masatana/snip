#!/usr/bin/env python
# -*- coding: utf-8 -*-

# memonization tequnique with decorator
# ref. http://blog.thehumangeo.com/2015/07/28/profiling-in-python/
# You can use this technique only for functions
# without any side effects.

from functools import wraps
def memonize(f):
    cache = {}
    @wraps(f)
    def inner(arg):
        if arg not in cache:
            cache[arg] = f(arg)
        return cache[arg]
    return inner

import time
@memonize
def slow(you):
    time.sleep(3)
    print("hello after 3 seocnds, {}".format(you))
    return 3

if __name__ == "__main__":
    print(slow("da")) # -> print "hello after..." and 3
    print(slow("da")) # -> just print 3
    print(slow("vi"))
    print(slow("vi"))
