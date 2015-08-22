#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ref. http://www.python-course.eu/python3_formatted_output.php

# => Art:   453, Price per unit:    59.06
print("Art: {0:5d}, Price per unit: {1:8.2f}".format(453, 59.058))

# =>Art:   453, Price per unit:    59.06
print("Art: {a:5d}, Price per unit: {p:8.2f}".format(a=453, p=59.058))
