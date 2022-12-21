import logging

logging.basicConfig(level=logging.INFO,
                    filename='core_log.log',
                    filemode="a",
                    format="%(asctime)s - [%(levelname)s] - %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)
log_form = logging.Formatter('%(asctime)s: %(message)')
log_handler = logging.StreamHandler()
logger.addHandler(log_handler)
from deep_translator import GoogleTranslator


class Trans(GoogleTranslator):

    def __init__(self, orig_text=None, **kwargs):
        super().__init__(**kwargs)
        self.orig_text = orig_text
        self.need_lang = str

    def trans(self, orig_text, need_lang):
        return GoogleTranslator(source='auto', target=need_lang).translate(orig_text)
