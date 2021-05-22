import pandas as pd
from datetime import datetime
import time
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from trdb2py.statistics import (buildPNLWinRateInYears, buildPNLListWinRateInYears2,
                                buildPNLWinRateInMonths, buildPNLListWinRateInMonths2, buildPNLListWinRate4Month,
                                buildPNLListResponseRateInYears2)
from trdb2py.trdb2utils import buildPNLDataFrame
from trdb2py.indicator import isPriceIndicator, isNeedSecondY
from trdb2py.pdutils import (buildPNLReport, getPNLLastTs, getPNLValueWithTimestamp, mergePNL, mergePNLEx,
                             rmPNLValuesWithTimestamp, getPNLTimestampLowInMonth, getPNLTimestampHighInMonth,
                             countTradingDays4Year, calcAnnualizedVolatility, rebuildPNL, rebuildDrawdown,
                             calcAnnualizedReturns, calcSharpe, clonePNLWithTs, genCtrlData)
import trdb2py.trading2_pb2


def showAssetCandles(title: str, dfCandles: pd.DataFrame, columm: str = 'close', toImg: bool = False, width=1024, height=768):
    fig = px.line(dfCandles, x='date', y=columm,
                  title=title)

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showPNL(pnl: dict, isPerValue: bool = True, dtFormat: str = '%Y-%m-%d', isShowBuy: bool = False, isShowSell: bool = False,
            toImg: bool = False, width=1024, height=768):
    if pnl is None:
        return 

    fv0 = {'date': [], 'value': []}
    for v in pnl['pnl'].values:
        fv0['date'].append(datetime.fromtimestamp(
            v.ts).strftime(dtFormat))

        if isPerValue:
            fv0['value'].append(v.perValue)
        else:
            fv0['value'].append(v.value - v.cost)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=fv0['date'], y=fv0['value'],
                             mode='lines',
                             name=pnl['title']))

    if isShowBuy:
        fv1 = genCtrlData(
            pnl['pnl'], trdb2py.trading2_pb2.CtrlType.CTRL_BUY, dtFormat=dtFormat)

        fig.add_trace(go.Scatter(x=fv1['date'], y=fv1['value'],
                                 mode='markers',
                                 name='{}:buy'.format(pnl['title'])))

    if isShowSell:
        fv1 = genCtrlData(
            pnl['pnl'], trdb2py.trading2_pb2.CtrlType.CTRL_SELL, dtFormat=dtFormat)

        fig.add_trace(go.Scatter(x=fv1['date'], y=fv1['value'],
                                 mode='markers',
                                 name='{}:sell'.format(pnl['title'])))

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showPNLs(lstpnl: list, isPerValue: bool = True, dtFormat: str = '%Y-%m-%d', isShowBuy: bool = False, isShowSell: bool = False,
             showNums: int = -1, toImg: bool = False, width=1024, height=768, startTs=0):

    fig = go.Figure()

    if showNums > 0:
        lstpnl = sorted(
            lstpnl, key=lambda curpnl: curpnl['pnl'].totalReturns, reverse=True)
        curnums = 0

        for pnl in lstpnl:
            df = buildPNLDataFrame(pnl, isPerValue, dtFormat, startTs)

            fig.add_trace(go.Scatter(x=df['date'], y=df['value'],
                                     mode='lines',
                                     name=pnl['title']))

            if isShowBuy:
                fv1 = genCtrlData(
                    pnl['pnl'], trdb2py.trading2_pb2.CtrlType.CTRL_BUY, dtFormat=dtFormat)
                fig.add_trace(go.Scatter(x=fv1['date'], y=fv1['value'],
                                         mode='markers',
                                         name='{}:buy'.format(pnl['title'])))

            if isShowSell:
                fv1 = genCtrlData(
                    pnl['pnl'], trdb2py.trading2_pb2.CtrlType.CTRL_SELL, dtFormat=dtFormat)
                fig.add_trace(go.Scatter(x=fv1['date'], y=fv1['value'],
                                         mode='markers',
                                         name='{}:sell'.format(pnl['title'])))

            curnums += 1

            if curnums >= showNums:
                break
    else:
        for pnl in lstpnl:
            df = buildPNLDataFrame(pnl, isPerValue, dtFormat, startTs)

            fig.add_trace(go.Scatter(x=df['date'], y=df['value'],
                                     mode='lines',
                                     name=pnl['title']))

            if isShowBuy:
                fv1 = genCtrlData(
                    pnl['pnl'], trdb2py.trading2_pb2.CtrlType.CTRL_BUY, dtFormat=dtFormat)
                fig.add_trace(go.Scatter(x=fv1['date'], y=fv1['value'],
                                         mode='markers',
                                         name='{}:buy'.format(pnl['title'])))

            if isShowSell:
                fv1 = genCtrlData(
                    pnl['pnl'], trdb2py.trading2_pb2.CtrlType.CTRL_SELL, dtFormat=dtFormat)
                fig.add_trace(go.Scatter(x=fv1['date'], y=fv1['value'],
                                         mode='markers',
                                         name='{}:sell'.format(pnl['title'])))

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showPNLs2(lstpnl: list, baseline: dict = None, isPerValue: bool = True, dtFormat: str = '%Y-%m-%d', isShowBuy: bool = False, isShowSell: bool = False,
              showNums: int = -1, toImg: bool = False, width=1024, height=768, startTs=0):

    fig = go.Figure()

    if showNums > 0:
        lstpnl = sorted(
            lstpnl, key=lambda curpnl: curpnl['pnl'].totalReturns, reverse=True)
        curnums = 0

        for pnl in lstpnl:
            df = buildPNLDataFrame(pnl, isPerValue, dtFormat, startTs)

            fig.add_trace(go.Scatter(x=df['date'], y=df['value'],
                                     mode='lines',
                                     name=pnl['title']))

            if isShowBuy:
                fv1 = genCtrlData(
                    pnl['pnl'], trdb2py.trading2_pb2.CtrlType.CTRL_BUY, dtFormat=dtFormat)
                fig.add_trace(go.Scatter(x=fv1['date'], y=fv1['value'],
                                         mode='markers',
                                         name='{}:buy'.format(pnl['title'])))

            if isShowSell:
                fv1 = genCtrlData(
                    pnl['pnl'], trdb2py.trading2_pb2.CtrlType.CTRL_SELL, dtFormat=dtFormat)
                fig.add_trace(go.Scatter(x=fv1['date'], y=fv1['value'],
                                         mode='markers',
                                         name='{}:sell'.format(pnl['title'])))

            curnums += 1

            if curnums >= showNums:
                break
    else:
        for pnl in lstpnl:
            df = buildPNLDataFrame(pnl, isPerValue, dtFormat, startTs)

            fig.add_trace(go.Scatter(x=df['date'], y=df['value'],
                                     mode='lines',
                                     name=pnl['title']))

            if isShowBuy:
                fv1 = genCtrlData(
                    pnl['pnl'], trdb2py.trading2_pb2.CtrlType.CTRL_BUY, dtFormat=dtFormat)
                fig.add_trace(go.Scatter(x=fv1['date'], y=fv1['value'],
                                         mode='markers',
                                         name='{}:buy'.format(pnl['title'])))

            if isShowSell:
                fv1 = genCtrlData(
                    pnl['pnl'], trdb2py.trading2_pb2.CtrlType.CTRL_SELL, dtFormat=dtFormat)
                fig.add_trace(go.Scatter(x=fv1['date'], y=fv1['value'],
                                         mode='markers',
                                         name='{}:sell'.format(pnl['title'])))

    if baseline != None:
        df = buildPNLDataFrame(baseline, isPerValue, dtFormat, startTs)

        fig.add_trace(go.Scatter(x=df['date'], y=df['value'],
                                 mode='lines',
                                 name=baseline['title']))

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showHeatmap(df: pd.DataFrame, columns: list, valtype: str = '', valoff: float = 0.0, toImg: bool = False, width=1024, height=768):
    data = []

    for index, row in df.iterrows():
        data.append([])

        for col in columns:
            if valtype == 'abs':
                data[index].append(abs(row[col] + valoff))
            else:
                data[index].append(row[col])
    # print(data)

    fig = go.Figure(data=go.Heatmap(
        z=data,
        x=columns,
        y=df['title']))

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showHeatmapWinRateInYears(lstpnl: list, sortby: str = '', valtype: str = '', valoff: float = 0.0, toImg: bool = False, width=1024, height=768):
    ret = buildPNLWinRateInYears(lstpnl)
    columns = []

    df = ret[0]

    if sortby != '':
        df = ret[0].sort_values(by=sortby).reset_index(drop=True)

    for y in range(ret[1], ret[2] + 1):
        columns.append('y{}'.format(y))

    columns.append('total')

    # print(columns)

    showHeatmap(df, columns, valtype, valoff, toImg, width, height)


def showWinRateInYears(lstpnl: list, valtype: str = '', valoff: float = 0.0, toImg: bool = False, width=1024, height=768):
    arr = buildPNLListWinRateInYears2(lstpnl)

    fig = go.Figure()

    if valtype == 'abs':
        for v in arr:

            vals = []
            for wrv in v['df']['winrate']:
                vals.append(abs(wrv + valoff))

            fig.add_trace(go.Scatter(x=v['df']['date'], y=vals,
                                     mode='lines',
                                     name=v['title']))
    else:
        for v in arr:
            fig.add_trace(go.Scatter(x=v['df']['date'], y=v['df']['winrate'],
                                     mode='lines',
                                     name=v['title']))

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showBarWinRateInYears(lstpnl: list, valtype: str = '', valoff: float = 0.0, toImg: bool = False, width=1024, height=768):
    arr = buildPNLListWinRateInYears2(lstpnl)

    lst = []

    if valtype == 'abs':
        for v in arr:

            vals = []
            for wrv in v['df']['winrate']:
                vals.append(abs(wrv + valoff))

            lst.append(go.Bar(x=v['df']['date'], y=vals,
                              name=v['title']))
    else:
        for v in arr:
            lst.append(go.Bar(x=v['df']['date'], y=v['df']['winrate'],
                              name=v['title']))

    fig = go.Figure(data=lst)

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showHeatmapWinRateInMonths(lstpnl: list, sortby: str = '', valtype: str = '', valoff: float = 0.0, toImg: bool = False, width=1024, height=768):
    ret = buildPNLWinRateInMonths(lstpnl)
    columns = []

    df = ret[0]

    if sortby != '':
        df = ret[0].sort_values(by=sortby).reset_index(drop=True)

    for y in range(ret[1], ret[3] + 1):
        if y == ret[1]:
            for m in range(ret[2], 12 + 1):
                columns.append('m{}{}'.format(y, m))
        elif y == ret[3]:
            for m in range(1, ret[4] + 1):
                columns.append('m{}{}'.format(y, m))
        else:
            for m in range(1, 12 + 1):
                columns.append('m{}{}'.format(y, m))

    columns.append('total')

    # print(columns)

    showHeatmap(df, columns, valtype, valoff, toImg, width, height)


def showWinRateInMonths(lstpnl: list, valtype: str = '', valoff: float = 0.0, toImg: bool = False, width=1024, height=768):
    arr = buildPNLListWinRateInMonths2(lstpnl)

    fig = go.Figure()

    if valtype == 'abs':
        for v in arr:

            vals = []
            for wrv in v['df']['winrate']:
                vals.append(abs(wrv + valoff))

            fig.add_trace(go.Scatter(x=v['df']['date'], y=vals,
                                     mode='lines',
                                     name=v['title']))
    else:
        for v in arr:
            fig.add_trace(go.Scatter(x=v['df']['date'], y=v['df']['winrate'],
                                     mode='lines',
                                     name=v['title']))

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showBarWinRateInMonths(lstpnl: list, valtype: str = '', valoff: float = 0.0, month: int = 0, toImg: bool = False, width=1024, height=768):
    arr = buildPNLListWinRateInMonths2(lstpnl)

    lst = []

    if month > 0 and month <= 12:
        if valtype == 'abs':
            for v in arr:
                lstdate = []
                vals = []
                for i in range(0, len(v['df']['winrate'])):
                    if v['df']['month'][i] == month:
                        vals.append(abs(v['df']['winrate'][i] + valoff))
                        lstdate.append(v['df']['date'][i])

                lst.append(go.Bar(x=lstdate, y=vals,
                                  name=v['title']))
        else:
            for v in arr:
                lstdate = []
                vals = []
                for i in range(0, len(v['df']['winrate'])):
                    if v['df']['month'][i] == month:
                        vals.append(v['df']['winrate'][i])
                        lstdate.append(v['df']['date'][i])

                lst.append(go.Bar(x=lstdate, y=vals,
                                  name=v['title']))
    else:
        if valtype == 'abs':
            for v in arr:

                vals = []
                for wrv in v['df']['winrate']:
                    vals.append(abs(wrv + valoff))

                lst.append(go.Bar(x=v['df']['date'], y=vals,
                                  name=v['title']))
        else:
            for v in arr:
                lst.append(go.Bar(x=v['df']['date'], y=v['df']['winrate'],
                                  name=v['title']))

    fig = go.Figure(data=lst)

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showBarWinRate4Month(lstpnl: list, valtype: str = '', valoff: float = 0.0, toImg: bool = False, width=1024, height=768):
    arr = buildPNLListWinRate4Month(lstpnl)

    lst = []

    if valtype == 'abs':
        for v in arr:

            vals = []
            for wrv in v['df']['winrate']:
                vals.append(abs(wrv + valoff))

            lst.append(go.Bar(x=v['df']['month'], y=vals,
                              name=v['title']))
    else:
        for v in arr:
            lst.append(go.Bar(x=v['df']['month'], y=v['df']['winrate'],
                              name=v['title']))

    fig = go.Figure(data=lst)

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showBarResponseRateInYears(lstpnl: list, toImg: bool = False, width=1024, height=768):
    arr = buildPNLListResponseRateInYears2(lstpnl)

    lst = []

    for v in arr:
        lst.append(go.Bar(x=v['df']['date'], y=v['df']['responserate'],
                          name=v['title']))

    fig = go.Figure(data=lst)

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showAssetCandles2(title: str, candles2: dict, indicators: list = None, columm: str = 'close', toImg: bool = False, width=1024, height=768):
    if indicators == None:
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=candles2['candle']['date'], y=candles2['candle'][columm],
                                 mode='lines',
                                 name=title))

        if toImg:
            fig.show(renderer="png", width=width, height=height)
        else:
            fig.show()

        return

    if isNeedSecondY(indicators):
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(go.Scatter(x=candles2['candle']['date'], y=candles2['candle'][columm],
                                 mode='lines',
                                 name=title),
                      secondary_y=False)

        for v in indicators:
            if v in candles2:
                if isPriceIndicator(v):
                    fig.add_trace(go.Scatter(x=candles2[v]['date'], y=candles2[v]['val'],
                                             mode='lines',
                                             name=v),
                                  secondary_y=False)
                else:
                    fig.add_trace(go.Scatter(x=candles2[v]['date'], y=candles2[v]['val'],
                                             mode='lines',
                                             name=v),
                                  secondary_y=True)

        fig.update_yaxes(title_text="price", secondary_y=False)

        if toImg:
            fig.show(renderer="png", width=width, height=height)
        else:
            fig.show()

        return

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=candles2['candle']['date'], y=candles2['candle'][columm],
                             mode='lines',
                             name=title))

    for v in indicators:
        if v in candles2:
            fig.add_trace(go.Scatter(x=candles2[v]['date'], y=candles2[v]['val'],
                                     mode='lines',
                                     name=v))

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showIndicators(title: str, candles2: dict, indicators: list = None, mode: str = 'markers',
                   colummX: str = 'date', colummY: str = 'val', toImg: bool = False, width=1024, height=768):
    fig = go.Figure()

    for v in indicators:
        if v in candles2:
            fig.add_trace(go.Scatter(x=candles2[v][colummX], y=candles2[v][colummY],
                                     mode=mode,
                                     name=v))

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showIndicatorPie(title: str, dfIndicator: pd.DataFrame, lstname: list, funcCountIndex,
                     toImg: bool = False, width=1024, height=768):
    lstnums = []
    for _ in lstname:
        lstnums.append(0)

    for _, row in dfIndicator.iterrows():
        ii = funcCountIndex(row['val'])
        lstnums[ii] = lstnums[ii] + 1

    fig = go.Figure(data=[go.Pie(labels=lstname, values=lstnums)])

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showBar(title: str, x, y, toImg: bool = False, width=1024, height=768):
    fig = go.Figure(
        data=[go.Bar(x=x, y=y)])

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showPie(title: str, labels, values, toImg: bool = False, width=1024, height=768):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()


def showHeatmap2(title: str, x, y, z, toImg: bool = False, width=1024, height=768):
    # z - arr[y][x]

    fig = go.Figure(data=go.Heatmap(
        z=z,
        x=x,
        y=y))

    if toImg:
        fig.show(renderer="png", width=width, height=height)
    else:
        fig.show()
