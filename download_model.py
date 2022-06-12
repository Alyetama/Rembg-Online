# -*- coding: utf-8 -*-

from pathlib import Path
from urllib import request

model_url = 'https://github.com/Alyetama/Rembg-Online/releases/download/v0.0.0/u2net.onnx'  # noqa
request.urlretrieve(model_url, '/.u2net/u2net.onnx')
