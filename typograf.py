import re


def make_beautiful(text):
    actions = [
        (r'[ \t]+', ' '),
        # remove extra space and tabs
        (r'\n+', '\n'),
        # remove extra linebreak
        (r'[\"](.+)[\"]', r'«\1»'),
        # replace " to « »
        (r'[\'](.+)[\']', r'«\1»'),
        # replace ' to « »
        (r'(\d+)‐(\d+)', r'\1&ndash;\2'),
        # replacement hyphen on dash in the phone number
        (r'(\d+)\s+(\w+)', r'\1&nbsp;\2'),
        # connect number with word by non-breaking spaces
        (r'(\w+)—([то|либо|нибудь]+)', r'\1-\2'),
        # replacing dash on hyphen
        (r'(это)\s([а-яА-Я]+)', r'\1&nbsp;— \2'),
        # replacing hyphens on dashes
        (r'([^-]\b[а-яА-Я]{1,2}\b)\s+(\w+)', r'\1&nbsp;\2')
        # connect conjunctions and any words by non-breaking space
    ]
    for pattern, replacement in actions:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text
