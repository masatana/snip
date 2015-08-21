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

if __main__ == "__main__":
    import time
    @memonize
    def slow(you):
        time.sleep(3)
        print("Hello after 3 second,s, {}".format(you))
        return 3
    slow("Davis") # => print, and return 3
    slow("Davis") # => just return 3
    slow("Visitor") # => print, and return 3
    slow("Visitor") # => just return 3

