# -*- coding:utf-8 -*-
import trdb2py.trading2_pb2


def str2Asset(asset: str) -> trdb2py.trading2_pb2.Asset:
    arr = asset.split('.', -1)
    if len(arr) != 2:
        raise ValueError

    return trdb2py.trading2_pb2.Asset(
        market=arr[0],
        code=arr[1],
    )
