import grpc
from concurrent import futures
import time

# import generated class
import message_pb2
import message_pb2_grpc

# import remote procedure
import player

# create a class to define server functions
class MessageServicer(message_pb2_grpc.MessageServicer):
    def FindPlayer(self, request, context):
        response = message_pb2.resObj()
        response.obj = player.FindPlayer(request.name)
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# add defined class to the server
message_pb2_grpc.add_MessageServicer_to_server(MessageServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50000.')
server.add_insecure_port('[::]:50000')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

