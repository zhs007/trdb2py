# -*- coding:utf-8 -*-
import sys 
sys.path.append("..")
import trdb2py

cfg = trdb2py.loadConfig('./config.yaml')
print(cfg)

asset = 'jqdata.000300_XSHG|1d'
tsStart = int(trdb2py.str2timestamp('2013-05-01', '%Y-%m-%d'))
tsEnd = int(trdb2py.str2timestamp('2020-09-30', '%Y-%m-%d'))
paramsinit = trdb2py.trading2_pb2.InitParams(
    money=10000,
)
paramsbuy = trdb2py.trading2_pb2.BuyParams(
    perHandMoney=1,
)
paramssell = trdb2py.trading2_pb2.SellParams(
    perVolume=1,
)

lstparams = []

asset = 'jqdata.000300_XSHG|1d'

# 起始时间，0表示从最开始算起
# tsStart = 0
tsStart = int(trdb2py.str2timestamp('2013-05-01', '%Y-%m-%d'))

# 结束时间，-1表示到现在为止
# tsEnd = -1
tsEnd = int(trdb2py.str2timestamp('2020-09-30', '%Y-%m-%d'))


for ema0 in range(2, 241):
    for ema1 in range(ema0 + 1, 241):
        buy0 = trdb2py.trading2_pb2.CtrlCondition(
            name='indicatorsp',
            operators=['upcross'],
            strVals=['ta-sma.{}'.format(ema1)],
        )

        buy1 = trdb2py.trading2_pb2.CtrlCondition(
            name='waittostart',
            vals=[ema0],
        )
        
        buy2 = trdb2py.trading2_pb2.CtrlCondition(
            name='indicatorsp',
            operators=['up'],
            strVals=['ta-sma.{}'.format(ema0)],
        )
        
        buy3 = trdb2py.trading2_pb2.CtrlCondition(
            name='waittostart',
            vals=[ema1],
        )        
        
        buy4 = trdb2py.trading2_pb2.CtrlCondition(
            name='indicatorsp',
            operators=['upcross'],
            strVals=['ta-sma.{}'.format(ema0)],
            group=1,
        )

        buy5 = trdb2py.trading2_pb2.CtrlCondition(
            name='waittostart',
            vals=[ema0],
            group=1,            
        )
        
        buy6 = trdb2py.trading2_pb2.CtrlCondition(
            name='indicatorsp',
            operators=['up'],
            strVals=['ta-sma.{}'.format(ema1)],
            group=1,            
        )
        
        buy7 = trdb2py.trading2_pb2.CtrlCondition(
            name='waittostart',
            vals=[ema1],
            group=1,            
        )                

        sell0 = trdb2py.trading2_pb2.CtrlCondition(
            name='indicatorsp',
            operators=['downcross'],
            strVals=['ta-sma.{}'.format(ema0)],
        )
        
        sell1 = trdb2py.trading2_pb2.CtrlCondition(
            name='indicatorsp',
            operators=['downcross'],
            strVals=['ta-sma.{}'.format(ema1)],
            group=1,                        
        )        
        
#         sell1 = trdb2py.trading2_pb2.CtrlCondition(
#             name='indicatorsp',
#             operators=['down'],
#             strVals=['ta-sma.{}'.format(ema0)],
#         )

        s0 = trdb2py.trading2_pb2.Strategy(
            name="normal",
            asset=trdb2py.str2asset(asset),
        )

        s0.buy.extend([buy0, buy1, buy2, buy3, buy4, buy5, buy6, buy7])
        s0.sell.extend([sell0, sell1])
        s0.paramsBuy.CopyFrom(paramsbuy)
        s0.paramsSell.CopyFrom(paramssell) 
        s0.paramsInit.CopyFrom(paramsinit)        
        lstparams.append(trdb2py.trading2_pb2.SimTradingParams(
            assets=[trdb2py.str2asset(asset)],
            startTs=tsStart,
            endTs=tsEnd,
            strategies=[s0],
            title='sma.{}&{}'.format(ema0, ema1),
            offset=ema1,
        ))
        
# len(lstparams)
lstpnlmix = trdb2py.simTradings(cfg, lstparams, ignoreTotalReturn=4, maxIgnoreNums=240*240)

# trdb2py.showPNLs(lstpnlmix + [pnlBaseline, lstpnl1[0]], toImg=isStaticImg, width=width, height=height)
df = trdb2py.buildPNLReport(lstpnlmix)
print(df[['title', 'totalReturns']])
