import string


__key = "OMG"

__encode_map = {char: idx for idx, char in enumerate(string.ascii_letters)}
__decode_map = {idx: char for idx, char in enumerate(string.ascii_letters)}

__key_map = [__encode_map[char] for char in __key]
