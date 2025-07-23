from rpc import RPCClient

#server = RPCClient('192.168.178.43', 8080)
server = RPCClient('10.42.0.3', 8080)

server.connect()

print(server.add(5, -16))
print(server.sub(5, 6))

server.disconnect()