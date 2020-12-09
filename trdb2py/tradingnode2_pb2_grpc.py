# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import tradingnode2_pb2 as tradingnode2__pb2


class TradingNode2Stub(object):
    """TradingNode2 - TradingNode2 service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getServerInfo = channel.unary_unary(
                '/tradingpb.TradingNode2/getServerInfo',
                request_serializer=tradingnode2__pb2.RequestServerInfo.SerializeToString,
                response_deserializer=tradingnode2__pb2.ReplyServerInfo.FromString,
                )
        self.calcPNL = channel.unary_unary(
                '/tradingpb.TradingNode2/calcPNL',
                request_serializer=tradingnode2__pb2.RequestCalcPNL.SerializeToString,
                response_deserializer=tradingnode2__pb2.ReplyCalcPNL.FromString,
                )


class TradingNode2Servicer(object):
    """TradingNode2 - TradingNode2 service
    """

    def getServerInfo(self, request, context):
        """getServerInfo - get server infomation
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def calcPNL(self, request, context):
        """calcPNL - calc PNL
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TradingNode2Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getServerInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.getServerInfo,
                    request_deserializer=tradingnode2__pb2.RequestServerInfo.FromString,
                    response_serializer=tradingnode2__pb2.ReplyServerInfo.SerializeToString,
            ),
            'calcPNL': grpc.unary_unary_rpc_method_handler(
                    servicer.calcPNL,
                    request_deserializer=tradingnode2__pb2.RequestCalcPNL.FromString,
                    response_serializer=tradingnode2__pb2.ReplyCalcPNL.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tradingpb.TradingNode2', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TradingNode2(object):
    """TradingNode2 - TradingNode2 service
    """

    @staticmethod
    def getServerInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tradingpb.TradingNode2/getServerInfo',
            tradingnode2__pb2.RequestServerInfo.SerializeToString,
            tradingnode2__pb2.ReplyServerInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def calcPNL(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tradingpb.TradingNode2/calcPNL',
            tradingnode2__pb2.RequestCalcPNL.SerializeToString,
            tradingnode2__pb2.ReplyCalcPNL.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
