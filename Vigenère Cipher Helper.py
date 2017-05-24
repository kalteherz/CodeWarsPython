class VigenereCipher:
    def __init__(self, key, abc):
        self.key = key.decode('utf-8')
        self.abc = abc.decode('utf-8')

    def code(self, text, decode):
        key_pos = 0
        res = []
        for ch in text.decode('utf-8'):
            if ch in self.abc:
                code = self.abc.index(ch)
                key_code = self.abc.index(self.key[key_pos])
                res.append(self.abc[(len(self.abc) * decode + code + key_code * (1 - 2 * decode)) % len(self.abc)])
            else:
                res.append(ch)
            key_pos = (key_pos + 1) % len(self.key)
        return ''.join(res).encode('utf-8')

    def encode(self, text):
        return self.code(text, 0)

    def decode(self, text):
        return self.code(text, 1)

abc = "abcdefghijklmnopqrstuvwxyz";
key = "password"
c = VigenereCipher(key, abc);

print(c.encode('codewars'))#, 'rovwsoiv');
print(c.encode('srawedoc'))#, 'hrsoarff');

print(c.decode('laxxhsj'))