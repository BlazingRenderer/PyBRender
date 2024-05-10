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

from ctypes import *

from brender.vector import *
from brender.pixelmap import *
from brender.model import *

# private
_BrLib = None
def _cstr(s): return c_char_p(s.encode('ascii'))

###########################
#
# library functions
#
##########################

#
# startup/shutdown
#

def Begin(libname="brender"):
	global _BrLib
	if _BrLib != None:
		raise Exception("BRender already started")
	_BrLib = CDLL(libname)
	_BrLib.BrV1dbBeginWrapper()

def End():
	global _BrLib
	_BrLib.BrV1dbEndWrapper()
	_BrLib = None

#
# pixelmaps
#

# allocate pixelmap
def PixelmapAllocate(pm_type, width, height, pixels, flags):
	_BrLib.BrPixelmapAllocate.argtypes = [c_ubyte, c_int, c_int, c_void_p, c_int]
	_BrLib.BrPixelmapAllocate.restype = c_void_p
	pm = _BrLib.BrPixelmapAllocate(pm_type, width, height, pixels, flags)
	return cast(pm, POINTER(pixelmap))

# free pixelmap
def PixelmapFree(pixelmap):
	_BrLib.BrPixelmapFree.argtypes = [c_void_p]
	_BrLib.BrPixelmapFree(pixelmap)

# save pixelmap
def PixelmapSave(filename, pixelmap):
	_BrLib.BrPixelmapSave.argtypes = [c_char_p, c_void_p]
	_BrLib.BrPixelmapSave(_cstr(filename), pixelmap)

# load pixelmap
def PixelmapLoad(filename):
	_BrLib.BrPixelmapLoad.argtypes = [c_char_p]
	_BrLib.BrPixelmapLoad.restype = c_void_p
	pm = _BrLib.BrPixelmapLoad(_cstr(filename))
	return cast(pm, POINTER(pixelmap))
