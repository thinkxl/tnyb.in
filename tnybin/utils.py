from hashids import Hashids
import arrow


LANGS = {
    'markdown': 'md',
    'python': 'py',
    'javascript': 'js',
    'ruby': 'rb',
    'css': 'css',
    'sass': 'sass',
    'scss': 'scss',
    'lua': 'lua',
    'html': 'html',
}


def map_lang(lang):
    return LANGS[lang]


def map_ext(ext):
    for lang, extension in LANGS.items():
        if extension == ext:
            return lang


def gen_uid(num, name=''):
    hashids = Hashids(salt='some salt', min_length=5)
    return hashids.encrypt(num + 1)


def datetimeformat(date):
    past = arrow.get(date)
    return past.humanize()
