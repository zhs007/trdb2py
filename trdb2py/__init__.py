# -*- coding:utf-8 -*-
from trdb2py.config import loadConfig
from trdb2py.indicator import isPriceIndicator, isNeedSecondY
from trdb2py.trdb2 import (simTradings, getAssetCandles,
                           simTrading, getAssetCandles2, simTradings3, getAssetCandles3)
from trdb2py.utils import str2asset, nextWeekDay, asset2str
from trdb2py.candlesutils import (calcCandlesSimilarity, calcCandlesSimilarity_LowLevel, 
                                  calcCandlesSimilarity_LowLevel2, calcCandlesSimilarity_ln)
from trdb2py.assetsutils import (calcAssetsSimilarity, calcAssetsSimilarity2,
                                 calcAssetsSimilarity_LowLevel, calcAssetsSimilarity2_LowLevel,
                                 calcAssetsSimilarity_LowLevel2, calcAssetsSimilarity2_LowLevel2,
                                 calcAssetsSimilarity_ln, calcAssetsSimilarity2_ln)
from trdb2py.timeutils import str2timestamp, getDayInYear, getYearDays, calcYears
from trdb2py.pdutils import (buildPNLReport, getPNLLastTs, getPNLValueWithTimestamp, mergePNL, mergePNLEx,
                             rmPNLValuesWithTimestamp, getPNLTimestampLowInMonth, getPNLTimestampHighInMonth,
                             countTradingDays4Year, calcAnnualizedVolatility, rebuildPNL, rebuildDrawdown,
                             calcAnnualizedReturns, calcSharpe, clonePNLWithTs, genCtrlData, buildPNLCtrlData)
from trdb2py.statistics import (calcPNLWinRateInYear, buildPNLWinRateInYears,
                                buildPNLWinRateInMonths, buildPNLListWinRateInYears2,
                                buildPNLListWinRateInMonths2, buildPNLListWinRate4Month,
                                buildPNLListResponseRateInYears2, calcCandles2Indicators, countIndicatorGroups)
from trdb2py.plotly import (showAssetCandles, showHeatmap, showHeatmapWinRateInYears,
                            showWinRateInYears, showHeatmapWinRateInMonths, showWinRateInMonths,
                            showBarWinRateInMonths, showBarWinRateInYears, showBarWinRate4Month,
                            showPNL, showPNLs, showPNLs2, showBarResponseRateInYears,
                            showAssetCandles2, showIndicators, showIndicatorPie, showBar, showPie, showHeatmap2)
from trdb2py.trdb2utils import (analysisResult, getIndicatorInResult, getFirstCtrlTs, buildPNLDataFrame,
                                sortIndicator, genPNLMap)
import trdb2py.trading2_pb2
