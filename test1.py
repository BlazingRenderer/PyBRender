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

import os
from ctypes import *

# import faulthandler
# faulthandler.enable()

# create null-terminated ascii c string
def CSTR(s): return c_char_p(s.encode('ascii'))

# library name
if os.name == "nt":
	LIBBRENDER = "libbrender.dll"
else:
	LIBBRENDER = "libbrender.so"

# make path absolute
LIBBRENDER = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + LIBBRENDER

# load library
brender = CDLL(LIBBRENDER)

# pixelmap types
BR_PMT_INDEX_8 = c_ubyte(3)

# pixelmap allocation flags
BR_PMAF_NORMAL = c_int(0x0000)
BR_PMAF_INVERTED = c_int(0x0001)
BR_PMAF_NO_PIXELS = c_int(0x0002)

# init brender
brender.BrV1dbBeginWrapper()

# allocate pixelmap
brender.BrPixelmapAllocate.restype = c_void_p
pm = brender.BrPixelmapAllocate(BR_PMT_INDEX_8, c_int(64), c_int(64), None, BR_PMAF_NORMAL)

# save pixelmap
brender.BrPixelmapSave.argtypes = [c_char_p, c_void_p]
brender.BrPixelmapSave(CSTR("test.pix"), pm)

# free pixelmap
brender.BrPixelmapFree.argtypes = [c_void_p]
brender.BrPixelmapFree(c_void_p(pm))

# shutdown brender
brender.BrV1dbEndWrapper()
