# -*- coding:utf-8 -*-
import trdb2py

cfg = trdb2py.loadConfig('./config.yaml')
print(cfg)

asset = 'jrj.510310'

buy0 = trdb2py.trading2_pb2.CtrlCondition(
    name='buyandhold',
)

paramsbuy = trdb2py.trading2_pb2.BuyParams(
    perHandMoney=1,
)

paramsinit = trdb2py.trading2_pb2.InitParams(
    money=10000,
)

s0 = trdb2py.trading2_pb2.Strategy(
    name="normal",
    asset=trdb2py.str2Asset(asset),
    buy=[buy0],
    paramsBuy=paramsbuy,
    paramsInit=paramsinit,
)

params = trdb2py.trading2_pb2.SimTradingParams(
    assets=[trdb2py.str2Asset(asset)],
    strategies=[s0],
)

ret = trdb2py.simTrading(cfg, params)
print(ret)
