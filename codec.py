def encode(codepoint):
	if codepoint < 0x80:
		return bytes([codepoint])
	elif codepoint < 0x800:
		b1 = (codepoint & 63) | 1 << 7
		b2 = (codepoint & 1984) >> 6 | 1 << 7 | 1 << 6
		return bytes([b2, b1])
	elif codepoint < 0x10000:
		b1 = (codepoint & 63) | 1 << 7
		b2 = (codepoint & 4032) >> 6 | 1 << 7
		b3 = (codepoint & 61440) >> 12 | 1 << 7 | 1 << 6 | 1 << 5
		return bytes([b3, b2, b1])
	elif codepoint < 0x110000:
		b1 = (codepoint & 63) | 1 << 7
		b2 = (codepoint & 4032) >> 6 | 1 << 7
		b3 = (codepoint & 258048) >> 12 | 1 << 7
		b4 = (codepoint & 1835008) >> 18 | 1 << 7 | 1 << 6 | 1 << 5 | 1 << 4
		return bytes([b4, b3, b2, b1])


def decode(bytes_object):
	if len(bytes_object) == 1:
		return bytes_object[0]
	elif len(bytes_object) == 2:
		b1 = bytes_object[1] & 63
		b2 = (bytes_object[0] & 63) << 6
		return b2 | b1
	elif len(bytes_object) == 3:
		b1 = bytes_object[2] & 63
		b2 = (bytes_object[1] & 63) << 6
		b3 = (bytes_object[0] & 15) << 12
		return b3 | b2 | b1
	elif len(bytes_object) == 4:
		b1 = bytes_object[3] & 63
		b2 = (bytes_object[2] & 63) << 6
		b3 = (bytes_object[1] & 63) << 12
		b4 = (bytes_object[0] & 7) << 18
		return b4 | b3 | b2 | b1

def main():
	pass

if __name__ == '__main__':
	main()