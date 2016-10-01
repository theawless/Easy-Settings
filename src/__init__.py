import logging

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(threadName)s - %(levelname)s - %(message)s')
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setFormatter(formatter)
logger.addHandler(sh)
