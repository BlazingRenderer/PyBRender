#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
