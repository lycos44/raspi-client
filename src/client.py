from collections import namedtuple
import logging
import sys
import argparse
import json
from rpc import RPCClient
from status import Status
from logging.handlers import TimedRotatingFileHandler
from time import sleep

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(module)s - %(levelname)s - %(funcName)s : %(lineno)d - %(message)s',
                    handlers=[TimedRotatingFileHandler("logs/raspi-client.log", when="midnight", interval=1, backupCount=7),
                              logging.StreamHandler()])

# create logger
logger = logging.getLogger('raspi-client')

def main():
    parser = argparse.ArgumentParser(description="Raspi Client.")
    parser.add_argument('--address', type=str, help='EV3 Server IPv4 address.')
    parser.add_argument('--port', type=int, help='EV3 Server port.')

    args = parser.parse_args()
    if args.address and args.port:
        server = RPCClient(args.address, args.port)
    else:
        exit("Please provide both --address and --port arguments.")
        
    try:
        server.connect()
        logger.info('Connected to server at %s', server._RPCClient__address)
        
        logger.info('Request result: {}'.format(server.drive_forward()))
        sleep(2)
        logger.info('Request result: {}'.format(server.stop()))

        logger.info('Request result: {}'.format(server.drive_backward()))
        sleep(2)
        logger.info('Request result: {}'.format(server.stop()))
    except Exception as e:
        logger.error('An error occurred: %s', e)
    finally:
        server.disconnect()
        logger.info('Disconnected from server')

if __name__ == '__main__':
    main() 