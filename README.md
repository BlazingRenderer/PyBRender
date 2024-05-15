# PyBRender

Experimental Python wrapper for BRender using `ctypes`.

The files `libbrender.dll` and `libbrender.so` in this repository were built from
[BRender commit 6bfa0dc](https://github.com/BlazingRenderer/BRender/commit/6bfa0dc).

Currently, you can only allocate/free/load/save models, pixelmaps, and materials.
Their fields should be properly editable, allowing for scriptable BRender asset
creation.

## Suggested Usage

```python
import os
import brender as Br

if os.name == "nt":
	lib = "libbrender.dll"
else:
	lib = "libbrender.so"

# setup library path
lib = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + lib

# startup brender
Br.Begin(lib)

# allocate a model
mdl = Br.ModelAllocate("cube", 8, 12)

# do something with the created model here
# you can access and modify the fields defined in brender/model.py

# save to disk, then free
Br.ModelSave("cube.dat", mdl)
Br.ModelFree(mdl)

# shutdown brender
Br.End()
```

## License

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
