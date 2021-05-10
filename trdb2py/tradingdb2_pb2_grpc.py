# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import tradingdb2_pb2 as tradingdb2__pb2


class TradingDB2Stub(object):
    """TradingDB2 - TradingDB2 service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.updCandles = channel.stream_unary(
                '/tradingpb.TradingDB2/updCandles',
                request_serializer=tradingdb2__pb2.RequestUpdCandles.SerializeToString,
                response_deserializer=tradingdb2__pb2.ReplyUpdCandles.FromString,
                )
        self.getCandles = channel.unary_stream(
                '/tradingpb.TradingDB2/getCandles',
                request_serializer=tradingdb2__pb2.RequestGetCandles.SerializeToString,
                response_deserializer=tradingdb2__pb2.ReplyGetCandles.FromString,
                )
        self.updSymbol = channel.unary_unary(
                '/tradingpb.TradingDB2/updSymbol',
                request_serializer=tradingdb2__pb2.RequestUpdSymbol.SerializeToString,
                response_deserializer=tradingdb2__pb2.ReplyUpdSymbol.FromString,
                )
        self.getSymbol = channel.unary_unary(
                '/tradingpb.TradingDB2/getSymbol',
                request_serializer=tradingdb2__pb2.RequestGetSymbol.SerializeToString,
                response_deserializer=tradingdb2__pb2.ReplyGetSymbol.FromString,
                )
        self.getSymbols = channel.unary_stream(
                '/tradingpb.TradingDB2/getSymbols',
                request_serializer=tradingdb2__pb2.RequestGetSymbols.SerializeToString,
                response_deserializer=tradingdb2__pb2.ReplyGetSymbol.FromString,
                )
        self.simTrading = channel.unary_unary(
                '/tradingpb.TradingDB2/simTrading',
                request_serializer=tradingdb2__pb2.RequestSimTrading.SerializeToString,
                response_deserializer=tradingdb2__pb2.ReplySimTrading.FromString,
                )
        self.simTrading2 = channel.stream_stream(
                '/tradingpb.TradingDB2/simTrading2',
                request_serializer=tradingdb2__pb2.RequestSimTrading.SerializeToString,
                response_deserializer=tradingdb2__pb2.ReplySimTrading.FromString,
                )
        self.simTrading3 = channel.stream_stream(
                '/tradingpb.TradingDB2/simTrading3',
                request_serializer=tradingdb2__pb2.RequestSimTrading.SerializeToString,
                response_deserializer=tradingdb2__pb2.ReplySimTrading.FromString,
                )
        self.reqTradingTask3 = channel.stream_stream(
                '/tradingpb.TradingDB2/reqTradingTask3',
                request_serializer=tradingdb2__pb2.RequestTradingTask.SerializeToString,
                response_deserializer=tradingdb2__pb2.ReplyTradingTask.FromString,
                )


class TradingDB2Servicer(object):
    """TradingDB2 - TradingDB2 service
    """

    def updCandles(self, request_iterator, context):
        """updCandles - update candles
        这个接口现在是覆盖的，不会和原有数据做任何合并操作
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getCandles(self, request, context):
        """getCandles - get candles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updSymbol(self, request, context):
        """updSymbol - update symbol
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getSymbol(self, request, context):
        """getSymbol - get symbol
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getSymbols(self, request, context):
        """getSymbols - get symbols
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def simTrading(self, request, context):
        """simTrading - simulation trading
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def simTrading2(self, request_iterator, context):
        """simTrading2 - simulation trading
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def simTrading3(self, request_iterator, context):
        """simTrading3 - simulation trading
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def reqTradingTask3(self, request_iterator, context):
        """reqTradingTask3 - request trading task
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TradingDB2Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'updCandles': grpc.stream_unary_rpc_method_handler(
                    servicer.updCandles,
                    request_deserializer=tradingdb2__pb2.RequestUpdCandles.FromString,
                    response_serializer=tradingdb2__pb2.ReplyUpdCandles.SerializeToString,
            ),
            'getCandles': grpc.unary_stream_rpc_method_handler(
                    servicer.getCandles,
                    request_deserializer=tradingdb2__pb2.RequestGetCandles.FromString,
                    response_serializer=tradingdb2__pb2.ReplyGetCandles.SerializeToString,
            ),
            'updSymbol': grpc.unary_unary_rpc_method_handler(
                    servicer.updSymbol,
                    request_deserializer=tradingdb2__pb2.RequestUpdSymbol.FromString,
                    response_serializer=tradingdb2__pb2.ReplyUpdSymbol.SerializeToString,
            ),
            'getSymbol': grpc.unary_unary_rpc_method_handler(
                    servicer.getSymbol,
                    request_deserializer=tradingdb2__pb2.RequestGetSymbol.FromString,
                    response_serializer=tradingdb2__pb2.ReplyGetSymbol.SerializeToString,
            ),
            'getSymbols': grpc.unary_stream_rpc_method_handler(
                    servicer.getSymbols,
                    request_deserializer=tradingdb2__pb2.RequestGetSymbols.FromString,
                    response_serializer=tradingdb2__pb2.ReplyGetSymbol.SerializeToString,
            ),
            'simTrading': grpc.unary_unary_rpc_method_handler(
                    servicer.simTrading,
                    request_deserializer=tradingdb2__pb2.RequestSimTrading.FromString,
                    response_serializer=tradingdb2__pb2.ReplySimTrading.SerializeToString,
            ),
            'simTrading2': grpc.stream_stream_rpc_method_handler(
                    servicer.simTrading2,
                    request_deserializer=tradingdb2__pb2.RequestSimTrading.FromString,
                    response_serializer=tradingdb2__pb2.ReplySimTrading.SerializeToString,
            ),
            'simTrading3': grpc.stream_stream_rpc_method_handler(
                    servicer.simTrading3,
                    request_deserializer=tradingdb2__pb2.RequestSimTrading.FromString,
                    response_serializer=tradingdb2__pb2.ReplySimTrading.SerializeToString,
            ),
            'reqTradingTask3': grpc.stream_stream_rpc_method_handler(
                    servicer.reqTradingTask3,
                    request_deserializer=tradingdb2__pb2.RequestTradingTask.FromString,
                    response_serializer=tradingdb2__pb2.ReplyTradingTask.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tradingpb.TradingDB2', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TradingDB2(object):
    """TradingDB2 - TradingDB2 service
    """

    @staticmethod
    def updCandles(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/tradingpb.TradingDB2/updCandles',
            tradingdb2__pb2.RequestUpdCandles.SerializeToString,
            tradingdb2__pb2.ReplyUpdCandles.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getCandles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/tradingpb.TradingDB2/getCandles',
            tradingdb2__pb2.RequestGetCandles.SerializeToString,
            tradingdb2__pb2.ReplyGetCandles.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updSymbol(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tradingpb.TradingDB2/updSymbol',
            tradingdb2__pb2.RequestUpdSymbol.SerializeToString,
            tradingdb2__pb2.ReplyUpdSymbol.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getSymbol(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tradingpb.TradingDB2/getSymbol',
            tradingdb2__pb2.RequestGetSymbol.SerializeToString,
            tradingdb2__pb2.ReplyGetSymbol.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getSymbols(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/tradingpb.TradingDB2/getSymbols',
            tradingdb2__pb2.RequestGetSymbols.SerializeToString,
            tradingdb2__pb2.ReplyGetSymbol.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def simTrading(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tradingpb.TradingDB2/simTrading',
            tradingdb2__pb2.RequestSimTrading.SerializeToString,
            tradingdb2__pb2.ReplySimTrading.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def simTrading2(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/tradingpb.TradingDB2/simTrading2',
            tradingdb2__pb2.RequestSimTrading.SerializeToString,
            tradingdb2__pb2.ReplySimTrading.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def simTrading3(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/tradingpb.TradingDB2/simTrading3',
            tradingdb2__pb2.RequestSimTrading.SerializeToString,
            tradingdb2__pb2.ReplySimTrading.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def reqTradingTask3(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/tradingpb.TradingDB2/reqTradingTask3',
            tradingdb2__pb2.RequestTradingTask.SerializeToString,
            tradingdb2__pb2.ReplyTradingTask.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
