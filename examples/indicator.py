# -*- coding:utf-8 -*-
import sys 
sys.path.append("..")
import trdb2py

cfg = trdb2py.loadConfig('./config.yaml')
print(cfg)

ret = trdb2py.getAssetCandles2(cfg, 'jrj.510310', 0, -1, indicators=['ema.29'], ignoreCache=True)
print(ret)

trdb2py.showAssetCandles2('510310', ret, indicators=['ema.29'], toImg=True)
