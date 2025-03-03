#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
MIT License

Copyright (c) 1992-1998 Argonaut Technologies Limited
Copyright (c) 2014-2025 Zane van Iperen, erysdren

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from ctypes import *

def ERROR_MAKE(klass, sub):
	return c_uint(klass | sub)

# error classes
ECLASS_NONE = 0x0000
ECLASS_MISC = 0x1000
ECLASS_APPLICATION = 0x2000
ECLASS_DATABASE = 0x3000
ECLASS_RENDERER = 0x4000
ECLASS_FILE = 0x5000
ECLASS_TOKEN = 0x6000
ECLASS_MATH = 0x7000
ECLASS_DOSIO = 0x8000
ECLASS_HOST = 0x9000
ECLASS_DEVICE = 0xA000

# everything ok
E_OK = c_uint(0x00)

# misc errors
E_UNKNOWN = ERROR_MAKE(ECLASS_MISC, 1)
E_FAIL = ERROR_MAKE(ECLASS_MISC, 2)
E_NO_MEMORY = ERROR_MAKE(ECLASS_MISC, 3)
E_OVERFLOW = ERROR_MAKE(ECLASS_MISC, 4)
E_UNDERFLOW = ERROR_MAKE(ECLASS_MISC, 5)
E_NOT_ACTIVE = ERROR_MAKE(ECLASS_MISC, 6)
E_ALLREADY_ACTIVE = ERROR_MAKE(ECLASS_MISC, 7)
E_UNSUPPORTED = ERROR_MAKE(ECLASS_MISC, 8)
E_INVALID = ERROR_MAKE(ECLASS_MISC, 9)

# device errors
E_DEV_FAIL = ERROR_MAKE(ECLASS_DEVICE, 1)
E_DEV_HARDWARE_NOT_PRESENT = ERROR_MAKE(ECLASS_DEVICE, 2)
E_DEV_NO_MEMORY = ERROR_MAKE(ECLASS_DEVICE, 3)
E_DEV_NO_VIDEO_MEMORY = ERROR_MAKE(ECLASS_DEVICE, 4)
E_DEV_UNSUPPORTED = ERROR_MAKE(ECLASS_DEVICE, 5)
E_DEV_HARDWARE_SET = ERROR_MAKE(ECLASS_DEVICE, 6)
E_DEV_HARDWARE_NOT_READY = ERROR_MAKE(ECLASS_DEVICE, 7)
E_DEV_NOT_FOUND = ERROR_MAKE(ECLASS_DEVICE, 8)
E_DEV_REFUSED = ERROR_MAKE(ECLASS_DEVICE, 9)
E_DEV_LOCK_FAIL = ERROR_MAKE(ECLASS_DEVICE, 10)
E_DEV_OUTPUT_UNAVAILABLE = ERROR_MAKE(ECLASS_DEVICE, 11)
E_DEV_ALREADY_INIT = ERROR_MAKE(ECLASS_DEVICE, 12)
E_DEV_DIRECTDRAW_ERROR = ERROR_MAKE(ECLASS_DEVICE, 13)
