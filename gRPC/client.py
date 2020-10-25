import grpc
import ast

# import generated class
import message_pb2
import message_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50000')

# create a stub (client)
stub = message_pb2_grpc.MessageStub(channel)

# request message
name = message_pb2.reqName(name="messi")

# make remote call
response = stub.FindPlayer(name)

# print response
print(ast.literal_eval(response.obj))