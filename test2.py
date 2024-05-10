#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

# allocate a pixelmap
pm = Br.PixelmapAllocate(Br.PMT_INDEX_8, 64, 64, None, Br.PMAF_NORMAL)

# free it
Br.PixelmapFree(pm)

# load a pixelmap from disk
checkerboard = Br.PixelmapLoad("checkerboard32.pix")
Br.PixelmapSave("checkerboard32 copy.pix", checkerboard)
Br.PixelmapFree(checkerboard)

# shutdown
Br.End()
