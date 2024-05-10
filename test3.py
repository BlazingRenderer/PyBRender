#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
MIT License

Copyright (c) 1992-1998 Argonaut Technologies Limited
Copyright (c) 2014-2024 Zane van Iperen, erysdren

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
import brender as Br

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
pixels = b'\xFF\x00\x00' * width * height

# allocate a pixelmap
pm = Br.PixelmapAllocate(Br.PMT_RGB_888, width, height, pixels, Br.PMAF_NORMAL)

# set identifier
pm.contents.identifier = Br.CSTR("test3")

# save it
Br.PixelmapSave("test3.pix", pm)

# free it
Br.PixelmapFree(pm)

# shutdown
Br.End()
