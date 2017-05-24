hb = {'0': '0000',
      '1': '0001',
      '2': '0010',
      '3': '0011',
      '4': '0100',
      '5': '0101',
      '6': '0110',
      '7': '0111',
      '8': '1000',
      '9': '1001',
      'a': '1010',
      'b': '1011',
      'c': '1100',
      'd': '1101',
      'e': '1110',
      'f': '1111'}
bh = {}
for k, v in hb.items():
    bh[v] = k

def bin_to_hex(binary_string):
    for i in range(4 - len(binary_string) % 4):
        binary_string = '0' + binary_string
    res = ''
    for i in range(len(binary_string) // 4):
        res += bh[binary_string[i * 4: i * 4 + 4]]
    while (len(res) > 1) and (res[0] == '0'):
        res = res[1:]
    return res if res != '' else '0'

def hex_to_bin(hex_string):
    res = ''
    for ch in hex_string:
        res += hb[ch.lower()]
    while (len(res) > 1) and (res[0] == '0'):
        res = res[1:]
    return res if res != '' else '0'

print(bin_to_hex('00000100111'))
