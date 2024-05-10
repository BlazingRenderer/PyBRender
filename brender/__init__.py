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

####################################################
#
# private
#
####################################################

_BrLib = None

####################################################
#
# utilities
#
####################################################

def CSTR(s): return c_char_p(s.encode('ascii'))

####################################################
#
# startup/shutdown
#
####################################################

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

####################################################
#
# pixelmaps
#
####################################################

# allocate
def PixelmapAllocate(pm_type, width, height, pixels, flags):
	_BrLib.BrPixelmapAllocate.argtypes = [c_ubyte, c_int, c_int, c_void_p, c_int]
	_BrLib.BrPixelmapAllocate.restype = POINTER(pixelmap)
	if type(pixels) == "bytes":
		pixels = create_string_buffer(pixels, len(pixels))
	return _BrLib.BrPixelmapAllocate(pm_type, width, height, pixels, flags)

# free
def PixelmapFree(pm):
	_BrLib.BrPixelmapFree.argtypes = [POINTER(pixelmap)]
	_BrLib.BrPixelmapFree(pm)

# save
def PixelmapSave(filename, pm):
	_BrLib.BrPixelmapSave.argtypes = [c_char_p, POINTER(pixelmap)]
	_BrLib.BrPixelmapSave.restype = c_uint
	return _BrLib.BrPixelmapSave(CSTR(filename), pm)

# load
def PixelmapLoad(filename):
	_BrLib.BrPixelmapLoad.argtypes = [c_char_p]
	_BrLib.BrPixelmapLoad.restype = POINTER(pixelmap)
	return _BrLib.BrPixelmapLoad(CSTR(filename))

####################################################
#
# models
#
####################################################

# allocate
def ModelAllocate(name, nvertices, nfaces):
	_BrLib.BrModelAllocate.argtypes = [c_char_p, c_int, c_int]
	_BrLib.BrModelAllocate.restype = POINTER(model)
	return _BrLib.BrModelAllocate(CSTR(name), nvertices, nfaces)

# free
def ModelFree(m):
	_BrLib.BrModelFree.argtypes = [POINTER(model)]
	_BrLib.BrModelFree(m)

# save
def ModelSave(filename, m):
	_BrLib.BrModelSave.argtypes = [c_char_p, POINTER(model)]
	_BrLib.BrModelSave.restype = c_uint
	return _BrLib.BrModelSave(CSTR(filename), m)

# load
def ModelLoad(filename):
	_BrLib.BrModelLoad.argtypes = [c_char_p]
	_BrLib.BrModelLoad.restype = POINTER(model)
	return _BrLib.BrModelLoad(CSTR(filename))
