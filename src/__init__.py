import logging

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(threadName)s - %(levelname)s - %(message)s')
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setFormatter(formatter)
logger.addHandler(sh)

ES_FILE_NAME = '.__es__'
ES_FILE_MAIN = '###main###'
ES_FILE_ITEM_TYPES = '###itemtypes###'
ES_FILE_PAGES = '###pages###'
