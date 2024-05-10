#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from ctypes import *

# private
_BrLib = None
def _cstr(s): return c_char_p(s.encode('ascii'))

# pixelmap types
PMT_INDEX_1 = c_ubyte(0)
PMT_INDEX_2 = c_ubyte(1)
PMT_INDEX_4 = c_ubyte(2)
PMT_INDEX_8 = c_ubyte(3)
PMT_RGB_555 = c_ubyte(4)
PMT_RGB_565 = c_ubyte(5)
PMT_RGB_888 = c_ubyte(6)
PMT_RGBX_888 = c_ubyte(7)
PMT_RGBA_8888 = c_ubyte(8)
PMT_YUYV_8888 = c_ubyte(9)
PMT_YUV_888 = c_ubyte(10)
PMT_DEPTH_16 = c_ubyte(11)
PMT_DEPTH_32 = c_ubyte(12)
PMT_ALPHA_8 = c_ubyte(13)
PMT_INDEXA_88 = c_ubyte(14)
PMT_NORMAL_INDEX_8 = c_ubyte(15)
PMT_NORMAL_XYZ = c_ubyte(16)
PMT_BGR_555 = c_ubyte(17)
PMT_RGBA_4444 = c_ubyte(18)
PMT_RBG_bab = c_ubyte(19)
PMT_RBG_1aba = c_ubyte(20)
PMT_RGB_332 = c_ubyte(21)
PMT_DEPTH_8 = c_ubyte(22)
PMT_ARGB_8888 = c_ubyte(23)
PMT_ALPHA_4 = c_ubyte(24)
PMT_INDEXA_44 = c_ubyte(25)
PMT_DEPTH_15 = c_ubyte(26)
PMT_DEPTH_31 = c_ubyte(27)
PMT_DEPTH_FP16 = c_ubyte(28)
PMT_DEPTH_FP15 = c_ubyte(29)
PMT_RGBA_5551 = c_ubyte(30)
PMT_ARGB_1555 = c_ubyte(31)
PMT_ARGB_4444 = c_ubyte(32)
PMT_RGBA_8888_ARR = c_ubyte(33)
PMT_MAX = c_ubyte(34)
PMT_AINDEX_44 = PMT_INDEXA_44
PMT_AINDEX_88 = PMT_INDEXA_88

# pixelmap allocation flags
PMAF_NORMAL = c_int(0x0000)
PMAF_INVERTED = c_int(0x0001)
PMAF_NO_PIXELS = c_int(0x0002)

# vector2
class vector2(Structure):
	_fields_ = [("x", c_float), ("y", c_float)]

# vector3
class vector3(Structure):
	_fields_ = [("x", c_float), ("y", c_float), ("z", c_float)]

# vector4
class vector4(Structure):
	_fields_ = [("x", c_float), ("y", c_float), ("z", c_float), ("w", c_float)]

# bounds2
class bounds2(Structure):
	_fields_ = [("min", vector2), ("max", vector2)]

# bounds3
class bounds3(Structure):
	_fields_ = [("min", vector3), ("max", vector3)]

# bounds4
class bounds4(Structure):
	_fields_ = [("min", vector4), ("max", vector4)]

# vertex
class vertex(Structure):
	_fields_ = [
		("p", vector3),
		("map", vector2),
		("index", c_ubyte),
		("red", c_ubyte),
		("grn", c_ubyte),
		("blu", c_ubyte),
		("_pad0", c_ushort),
		("n", vector3)
	]

# face
class face(Structure):
	_fields_ = [
		("vertices", c_ushort),
		("smoothing", c_ushort),
		("material", c_void_p),
		("index", c_ubyte),
		("red", c_ubyte),
		("grn", c_ubyte),
		("blu", c_ubyte),
		("flags", c_ubyte),
		("_pad0", c_ubyte),
		("_pad1", c_uint),
		("n", vector3),
		("d", c_float)
	]

# model
class model(Structure):
	_fields_ = [
		("_reserved", c_void_p),
		("identifier", c_char_p),
		("vertices", c_void_p),
		("faces", c_void_p),
		("nvertices", c_ushort),
		("nfaces", c_ushort),
		("pivot", vector3),
		("flags", c_ushort),
		("custom", c_void_p),
		("user", c_void_p),
		("crease_angle", c_float),
		("radius", c_float),
		("bounds", bounds3),
		("prepared", c_void_p),
		("stored", c_void_p),
		("nprimitive_lists", c_ushort),
		("primitive_list", c_void_p)
	]

# colour range
class colour_range(Structure):
	_fields_ = [("low", c_uint), ("high", c_uint)]

# pixelmap
class pixelmap(Structure):
	pass
pixelmap._fields_ = [
		("_reserved", c_void_p),
		("identifier", c_char_p),
		("pixels", c_void_p),
		("map", POINTER(pixelmap)),
		("src_key", colour_range),
		("dst_key", colour_range),
		("key", c_uint),
		("row_bytes", c_short),
		("mip_offset", c_short),
		("type", c_ubyte),
		("copy_function", c_ushort),
		("flags", c_ushort),
		("base_x", c_ushort),
		("base_y", c_ushort),
		("width", c_ushort),
		("height", c_ushort),
		("origin_x", c_short),
		("origin_y", c_short),
		("user", c_void_p),
		("stored", c_void_p)
	]

#
# startup / shutdown
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
