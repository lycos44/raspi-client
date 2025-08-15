# https://medium.com/@taraszhere/coding-remote-procedure-call-rpc-with-python-3b14a7d00ac8
# https://github.com/TarasZhere/RPC

# raspberry pi as a bridge
# https://pimylifeup.com/raspberry-pi-wifi-bridge/
# install iptables
# https://piprojects.us/iptables-firewall-rules-for-your-pi/
import json
import socket
import inspect
import logging
from threading import Thread

SIZE = 1024

logger = logging.getLogger('raspi-client')

class RPCClient:
    def __init__(self, host:str='localhost', port:int=8080) -> None:
        logger.debug('Creating RPCClient instance with host: %s, port: %d', host, port)
        self.__sock = None
        self.__address = (host, port)


    def isConnected(self):
        logger.debug('Checking connection status to %s:%d', *self.__address)
        try:
            self.__sock.sendall(b'test')
            self.__sock.recv(SIZE)
            return True

        except:
            return False


    def connect(self):
        logger.debug('Connecting to server at %s:%d', *self.__address)
        try:
            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__sock.connect(self.__address)
        except EOFError as e:
            logger.exception(e)
            raise Exception('Client was not able to connect.')
        
    
    def disconnect(self):
        logger.debug('Disconnecting from server at %s:%d', *self.__address)
        try:
            self.__sock.close()
        except:
            pass


    def __getattr__(self, __name: str):
        logger.debug('Creating remote procedure call for method: %s', __name)
        def excecute(*args, **kwargs):
            self.__sock.sendall(json.dumps((__name, args, kwargs)).encode())

            response = json.loads(self.__sock.recv(SIZE).decode())
   
            return response
        
        return excecute


    def __del__(self):
        logger.debug('Cleaning up RPCClient instance')
        try:
            self.__sock.close()
        except:
            pass