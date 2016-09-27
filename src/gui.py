import logging
from gi.repository import GObject

logger = logging.getLogger(__name__)


class Gui(GObject.GObject):
    __gsignals__ = {
        'page_dirtied': (GObject.SIGNAL_RUN_FIRST, None, (object,))
    }
