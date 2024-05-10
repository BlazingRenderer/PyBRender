#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import brender as Br
from ctypes import create_string_buffer

# library name
if os.name == "nt":
	libname = "libbrender.dll"
else:
	libname = "libbrender.so"

# make path absolute
libname = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + libname

# startup
Br.Begin(libname)

# an image
width = 32
height = 32
pixels = create_string_buffer(b'\xFF\x00\x00' * width * height)

# allocate a pixelmap
pm = Br.PixelmapAllocate(Br.PMT_RGB_888, width, height, pixels, Br.PMAF_NORMAL)

# save it
Br.PixelmapSave("test3.pix", pm)

# free it
Br.PixelmapFree(pm)

# shutdown
Br.End()
