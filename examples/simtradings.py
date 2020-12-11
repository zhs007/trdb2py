# -*- coding:utf-8 -*-
import trdb2py

cfg = trdb2py.loadConfig('./config.yaml')
print(cfg)

# paramsaip = trading2_pb2.AIPParams(
#     money=10000,
#     type=trading2_pb2.AIPTT_MONTHDAY,
#     day=1,
# )

# paramsinit = trading2_pb2.InitParams(
#     money=10000,
# )

# buyup = trading2_pb2.CtrlCondition(
#     name='indicatorsp',
#     operators=['up'],
#     strVals=['ema.30'],
# )

# buydown = trading2_pb2.CtrlCondition(
#     name='indicatorsp',
#     operators=['down'],
#     strVals=['ema.30'],
# )

# lststart = [1, 2, 3, 4, 5]
# lstend = [2, 3, 4, 5, 1]
# lsttitle = ['周一', '周二', '周三', '周四', '周五']
# lstparams = []
assets = ['jrj.510310']
# for day in range(0, 4):
#     for i in range(0, 5):
#         buy0 = trading2_pb2.CtrlCondition(
#             name='weekday',
#             vals=[lststart[i]],
#         )

#         sell0 = trading2_pb2.CtrlCondition(
#             name='weekday',
#             vals=[libtrdb2.nextWeekDay(lststart[i], day + 1)],
#         )

#         paramsbuy = trading2_pb2.BuyParams(
#             perHandMoney=1,
#         )

#         paramssell = trading2_pb2.SellParams(
#             perVolume=1,
#         )

#         s0 = trading2_pb2.Strategy(
#             name="normal",
#             asset=libtrdb2.str2Asset(assets[0]),
#         )

#         s0.buy.extend([buy0, buyup])
#         s0.sell.extend([sell0])
#         s0.paramsBuy.CopyFrom(paramsbuy)
#         s0.paramsSell.CopyFrom(paramssell)
#         s0.paramsInit.CopyFrom(paramsinit)
#         lstparams.append(trading2_pb2.SimTradingParams(
#             assets=[libtrdb2.str2Asset('cnfunds.510310')],
#             startTs=0,
#             endTs=-1,
#             strategies=[s0],
#             title='{}持有{}天up'.format(lsttitle[i], day+1)
#         ))

#         s1 = trading2_pb2.Strategy(
#             name="normal",
#             asset=libtrdb2.str2Asset(assets[0]),
#         )

#         s1.buy.extend([buy0, buydown])
#         s1.sell.extend([sell0])
#         s1.paramsBuy.CopyFrom(paramsbuy)
#         s1.paramsSell.CopyFrom(paramssell)
#         s1.paramsInit.CopyFrom(paramsinit)
#         lstparams.append(trading2_pb2.SimTradingParams(
#             assets=[libtrdb2.str2Asset('cnfunds.510310')],
#             startTs=0,
#             endTs=-1,
#             strategies=[s1],
#             title='{}持有{}天down'.format(lsttitle[i], day+1)
#         ))

# lstpnlaip = libtrdb2.simTradings(trdb2cfg, lstparams)

# baseline
lstparams = []

buy0 = trdb2py.trading2_pb2.CtrlCondition(
    name='buyandhold',
)

paramsbuy = trdb2py.trading2_pb2.BuyParams(
    perHandMoney=1,
)

paramsinit = trdb2py.trading2_pb2.InitParams(
    money=10000,
)

s1 = trdb2py.trading2_pb2.Strategy(
    name="normal",
    asset=trdb2py.str2Asset(assets[0]),
)

s1.buy.extend([buy0])
# s1.sell.extend([sell0])
s1.paramsBuy.CopyFrom(paramsbuy)
# s1.paramsSell.CopyFrom(paramssell)
s1.paramsInit.CopyFrom(paramsinit)
lstparams.append(trdb2py.trading2_pb2.SimTradingParams(
    assets=[trdb2py.str2Asset('jrj.510310')],
    startTs=0,
    endTs=-1,
    strategies=[s1],
    title='baseline',
))

print(lstparams)

lstpnlaip = trdb2py.simTradings(cfg, lstparams)

# pnl = trdb2py.simTradings(cfg, assets, 0, -1, [buy0], None, paramsbuy, None, paramsinit, None)
# lstpnlaip.append({'title': 'baseline', 'pnl': pnl})
