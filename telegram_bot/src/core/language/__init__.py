from .en import EN
from .ru import RU
from .lang import Language


languages = {
    'EN': EN,
    'RU': RU
}


def get_locale(locale):
    return languages[locale]()


__all__ = [
    'get_locale',
    'Language'
]
