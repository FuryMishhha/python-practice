import struct

def f31(binary: bytes) -> dict:
    def struct_a(offset: int) -> dict:
        [length] = struct.unpack('< H', binary[offset: offset + 2])
        offset += 2
        [link_str] = struct.unpack('< H', binary[offset: offset + 2])
        offset += 2
        a1 = str([struct.unpack('<' + str(length) + 's', binary[link_str: link_str + length])])[4:-4]

        [a2] = struct.unpack('< I', binary[offset: offset + 4])
        offset += 4

        [a3] = struct.unpack('< H', binary[offset: offset + 2])
        offset += 2

        [a4, a5, a6] = struct.unpack('< h b h', binary[offset: offset + 2 + 1 + 2])
        return {
            'A1': a1,
            'A2': struct_b(a2),
            'A3': struct_c(a3),
            'A4': a4,
            'A5': a5,
            'A6': a6
        }

    def struct_b(offset: int) -> dict:
        [b1, b2] = struct.unpack('< q h', binary[offset: offset + 8 + 2])
        return {
            'B1': b1,
            'B2': b2
        }

    def struct_c(offset: int) -> dict:
        [length] = struct.unpack('< H', binary[offset: offset + 2])
        offset += 2
        [link_list] = struct.unpack('< I', binary[offset: offset + 4])
        offset += 4
        list_links = [struct.unpack('< H', binary[link_list + i * 2: link_list + (i + 1) * 2])[0]
                      for i in range(length)]
        c1 = [struct_d(list_links[i]) for i in range(length)]

        c2 = list(struct.unpack('< 7I', binary[offset: offset + 7 * 4]))
        offset += 7 * 4

        [c3] = struct.unpack('< d', binary[offset: offset + 8])
        return {
            'C1': c1,
            'C2': c2,
            'C3': c3
        }

    def struct_d(offset: int) -> dict:
        [d1, d2] = struct.unpack('< d B', binary[offset: offset + 8 + 1])
        offset += 8 + 1

        [length] = struct.unpack('< H', binary[offset: offset + 2])
        offset += 2

        [link_str] = struct.unpack('< I', binary[offset: offset + 4])
        d3 = list(struct.unpack('<' + str(length) + 'B', binary[link_str: link_str + length]))
        return {
            'D1': d1,
            'D2': d2,
            'D3': d3
        }

    return struct_a(4)

print(f31(b'PLTR\x03\x00\x13\x00\x16\x00\x00\x00a\x00x\xd1\xfc\xaaToza\xce.'
          b'\xc3\xba\xbc\xcc\xfbi\xfa\xd2\x8fay\xd8\xd7\xccK\xae\x16\xc4?P\x03\x00 \x00'
          b'\x00\x00\xa4\xe3\xd1\x02|\xcc\xb1\xe0q\xa1Y\xf4\xb1\xac\xbfR\x07\x00'
          b'2\x00\x00\x00\xe9r\x12\xbe\x1cp\xa2\x84,t\xe1\xbfV\x04\x00H\x00\x00\x00#'
          b'\x009\x00L\x00\x03\x00[\x00\x00\x00\x99\x18\xb3\xe7\xc0\x0c\xf0\xcc\xae'
          b"!)t\xaa2'\x17[# >po\x05\x83\xa5X\xc49\xe0\x04i\x0b=\x99\xcc?"))
print(f31(b'PLTR\x05\x00\x13\x00\x18\x00\x00\x00}\x000\x93\xb4\xfa\x12cqokf\xd1uL\xf5'
          b'\x85E=\xbf\x04\x1a\xeb\x8d\xb2\xdb\x8b\x89a\x14\xacc\x9f^\x11\xda'
          b'\xbf\x7f\x07\x00"\x00\x00\x00\xf3\x12k\xb0\x9eow\xfaC4\xeb\xbf\xa6\x04\x008'
          b'\x00\x00\x00\xf7\xccN1\xb6H\x08\xb8+c\x10\xdf\xbf\x8a\x05\x00K\x00\x00\x008'
          b'\x8f1\xbb\xe9\xe8v\xd8\x93\xa2\xd6o\xe6\xc6\xbf]\x07\x00_\x00\x00\x00)\x00<'
          b'\x00P\x00f\x00\x04\x00u\x00\x00\x00\x1f\x9f\xc1\x01h\xefK\xd9\xe1B5e\x9a'
          b'\xb5%\x8b\xe4\x90\xed\xdcB\x073.\x13\x14\xc2h\x16\x93\xe1\x94z;\xe7\xbf'))
