#!/usr/bin/env python
# -*- coding: utf-8 -*-

# memonization tequnique with decorator
# ref. https://docs.python.org/3/library/functools.html

import functools

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print([fib(n) for n in range(16)])
