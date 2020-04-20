import os
import time

from package_name.telemetry import logger


def start_daemon():
    """
    Main daemon code.
    """
    while True:
        logger.info('Daemon running...')
        time.sleep(60)


def shutdown_daemon(signum, frame):
    """
    Shuts down daemon when a SIGTERM is received from systemd
    """
    logger.info('signal ' + str(signum) + ' received from systemd')
    logger.info('Stopping daemon')
    exit(0)


def main():
    """
    Main invocation point for daemon.
    """
    if os.environ.get('INVOCATOR') == "systemd":
        logger.info('Starting daemon')
        start_daemon()
    else:
        logger.error('Cannot invoke daemon from command line! Use systemd controls.')
        exit(1)


if __name__ == "__main__":
    main()
