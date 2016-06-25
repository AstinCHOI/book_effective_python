
####
# 1) unicode to binary: encode, vice versa: decode
####

# python3
# character sequence: bytes(raw 8 bit), str(unicode)
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    
    return value # str instance
    
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    
    return value # bytes instance
    

# python2
# character sequence: str(raw 8 bit), unicode(unicode)
def to_str(unicode_or_str):
    if isinstance(unicode_or_str, bytes):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    
    return value # str instance
    
def to_bytes(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    
    return value # bytes instance


####
# 2) open
####

# python2 ok, python3 not, which added encoding argument(default=utf-8)
# so, use 'wb' for both
with open('/tmp/random.bin', 'w') as f:
    f.write(os.urandom(10))

# TypeError: must be str, not bytes