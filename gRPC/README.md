# Simple gRPC Implementation

## File Structure
```
.
│-- player.py               # remote procedure
|
│-- message.proto           # protobuf definition file
|
│-- message_pb2.py          # generated class for message
│-- message_pb2_grpc.py     # generated class for server/client
|
│-- client.py               # client-side implementation
│-- server.py               # server-side implementation
```

## Pre-requisites
Install the following libraries:
- grpcio
- grpcio-tools

Generate RPC classes for server/client and message:
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. message.proto
```

Two files will be generated:
- message_pb2.py:
    - contains message classes
    - **message_pb2.reqName()** for request
    - **message_pb2.resObj()** for response
- message_pb2_grpc.py:
    - **message_pb2_grpc.MessageServicer** for the server
    - **message_pb2_grpc.MessageStub** for the client

## References
- [A simplified guide to gRPC in Python](https://www.semantics3.com/blog/a-simplified-guide-to-grpc-in-python-6c4e25f0c506/)
- [Introduction to gRPC](https://grpc.io/docs/what-is-grpc/introduction/)