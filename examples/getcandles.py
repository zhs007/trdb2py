# -*- coding:utf-8 -*-
import trdb2py

cfg = trdb2py.loadConfig('./config.yaml')
print(cfg)

ret = trdb2py.getAssetCandles(cfg, 'jrj.510310', 0, -1)
print(ret)
