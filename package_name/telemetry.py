import logging
import os
import sys

if os.environ.get('INVOCATOR') != "systemd":
    print('Cannot invoke daemon from command line! Use systemd controls.')
    exit(1)

# Define the logger
logger = logging.getLogger('package_name')
logger.setLevel(logging.INFO)

# Define output for systemd
_systemd_out = logging.StreamHandler(sys.stdout)
_systemd_out.setLevel(logging.WARNING)

# Define output for logging file
_log_file = logging.FileHandler('/etc/package_name/daemon.log')
_log_file.setLevel(logging.INFO)
_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
_log_file.setFormatter(_formatter)

# Add the handlers
logger.addHandler(_systemd_out)
logger.addHandler(_log_file)
