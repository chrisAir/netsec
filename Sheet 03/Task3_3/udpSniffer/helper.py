import textwrap


# Formats MAC Address
def formatMAC(rawMAC):
    byte_str = map('{:02x}'.format, rawMAC)
    mac_addr = ':'.join(byte_str).upper()
    return mac_addr


# Formats large output
def formatLines(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size % 2:
            size -= 1
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])