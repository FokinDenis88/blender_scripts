import re

PREFIX_REGEX = '^[^_]+_'
SUFFIX_REGEX = '_[^_]+\\Z'

def get_prefix(text):
    match_object = re.search(PREFIX_REGEX, text)
    if match_object is not None:
        return match_object[0]
    else:
        return ''

def get_suffix(text):
    match_object = re.search(SUFFIX_REGEX, text)
    if match_object is not None:
        return match_object[0]
    else:
        return ''