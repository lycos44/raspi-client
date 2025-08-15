import logging
import logging.config
import os
from rpc import RPCClient

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s : %(lineno)d - %(message)s',
                    handlers=[logging.FileHandler("logs/raspi-client.log"),
                              logging.StreamHandler()])

# create logger
logger = logging.getLogger('raspi-client')

def main():
    #server = RPCClient('192.168.178.43', 8080)
    server = RPCClient('192.168.178.35', 8080)

    server.connect()
    logger.info('Connected to server at %s', server._RPCClient__address)

    logger.info('Request result: {}'.format(server.add(5, 16)))
    logger.info('Request result: {}'.format(server.add(5, 6)))

    server.disconnect()
    logger.info('Disconnected from server')


if __name__ == '__main__':
    main() 