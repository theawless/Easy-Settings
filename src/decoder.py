import src.items
from src import *
from src.dictionaryhandler import DictionaryHandler
from src.elements import Stencil, Page, Section
from src.loader import Loader
from src.types import SaveStyle

logger = logging.getLogger(__name__)


class Decoder:
    def __init__(self, save_path):
        self.save_path = save_path
        self._dict_handler = None
        self.save_style = None

    def get_save_style(self):
        try:
            DictionaryHandler.check_for_file(self.save_path, ES_FILE_NAME, '.ini')
            self.save_style = SaveStyle.CONFIGPARSER
            self._dict_handler = DictionaryHandler(self.save_path, self.save_style)
        except FileNotFoundError:
            try:
                self._dict_handler.check_for_file(self.save_path, ES_FILE_NAME, '.json')
                self.save_style = SaveStyle.JSON
                self._dict_handler = DictionaryHandler(self.save_path, self.save_style)
            except FileNotFoundError:
                raise

    def _make_stencil(self, es_dict):
        stecil_name, stencil_display_name = next(iter(es_dict[ES_FILE_MAIN].items()))
        stencil = Stencil(stecil_name, stencil_display_name)
        for page_name, page_display_name in es_dict[ES_FILE_PAGES].items():
            page = Page(page_name, page_display_name)
            for section_name, section_display_name in es_dict[page_name].items():
                section = Section(section_name, section_display_name)
                for item_name, item_display_name in es_dict[section_name].items():
                    item_class = getattr(src.items, es_dict[ES_FILE_ITEM_TYPES][item_name])
                    item = item_class(item_name, item_display_name)
                    if isinstance(item, src.items.CompositeItem):
                        for subitem_name, subitem_display_name in es_dict[item_name].items():
                            subitem = item.subitem_class(subitem_name, subitem_display_name)
                            item.add_subitems(subitem)
                    section.add_items(item)
                page.add_sections(section)
            stencil.add_pages(page)
        return stencil

    def decode(self, load=True):
        if not self._dict_handler:
            self.get_save_style()
        stencil = self._make_stencil(self._dict_handler.read_dict(ES_FILE_NAME))
        if load:
            loader = Loader(self.save_path, self.save_style, stencil)
            loader.load()
        return stencil
