import re

FULLTEXT_ABBR_PATTERN = re.compile(".*?\([^(]*\)")
FULLTEXT_ABBR_PAIR_PATTERN = re.compile("(.*?)\(([^(]*)\)")

WHITESPACE_PATTERN = re.compile(r"\s")
SPLIT_PATTERN = re.compile(r"[\s\-_/]")



def parse_fulltext_abbr_pair(text):
    return [FULLTEXT_ABBR_PAIR_PATTERN.match(segment).groups() for segment in FULLTEXT_ABBR_PATTERN.findall(text)]

def parse_pattern_1(text, abbr):
    text_cursor = len(text) - 1
    abbr_cursor = len(abbr) - 1

    while text_cursor > -1:
        if SPLIT_PATTERN.match(text[text_cursor]):
            text_cursor -=1
            continue
        else:
            break

    start = None
    final_word_bound = None
    while text_cursor > -1:
        is_bounding = False
        if SPLIT_PATTERN.match(text[text_cursor]):
            is_bounding = True
            final_word_bound = text_cursor+1
            start = text[final_word_bound]
        elif text_cursor == 0:
            is_bounding = True
            final_word_bound = 0
            start = text[final_word_bound]

        if is_bounding:
            if abbr_cursor < 0:
                return None
            if abbr[abbr_cursor].lower() == start.lower():
                if abbr_cursor > 0:
                    abbr_cursor -=1
                else:
                    return text[final_word_bound:].strip()
            else:
                return None

        text_cursor -=1







def parse_from_abstract(texts, result):
    for text in texts:
        pairs = parse_fulltext_abbr_pair(text)
        for seg, abbr in pairs:
            long_form = parse_pattern_1(seg, abbr)
            # result.append((abbr,long_form))
            if long_form:
                if abbr not in result:
                    result[abbr] = {}
                longs = result[abbr]
                if long_form not in longs:
                    longs[long_form] = 1
                else:
                    longs[long_form] += 1










