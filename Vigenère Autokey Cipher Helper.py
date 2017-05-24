class VigenereAutokeyCipher:
    def __init__(self, key, abc):
        self.key = key
        self.abc = {}
        self.anti_abc = []
        for i in range(len(abc)):
            ch = abc[i]
            self.abc[ch] = i
            self.anti_abc.append(ch)

    def encode(self, text):
        key_pos = 0
        res = ""
        new_key = self.key + text
        for ch in text:
            if ch in self.abc:
                code = self.abc.get(ch)
                while not new_key[key_pos] in self.abc:
                    key_pos += 1
                key_code = self.abc.get(new_key[key_pos])
                res += self.anti_abc[(code + key_code) % len(self.abc)]
                key_pos += 1
            else:
               res += ch
        return res

    def decode(self, text):
        key_pos = 0
        res = ""
        new_key = self.key
        for ch in text:
            if ch in self.abc:
                code = self.abc.get(ch)
                key_code = self.abc.get(new_key[key_pos])
                new_char = self.anti_abc[(len(self.abc) + code - key_code) % len(self.abc)]
                res += new_char
                key_pos += 1
                if new_char in self.abc:
                    new_key += new_char
            else:
               res += ch
        return res

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'

c = VigenereAutokeyCipher(key, alphabet)

print(c.encode('codewars')); # returns 'rovwsoiv'
print(c.decode('laxxhsj')); # returns 'waffles'

# returns 'pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib'
print(c.encode('amazingly few discotheques provide jukeboxes'))
# returns 'amazingly few discotheques provide jukeboxes'
print(c.decode('pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib'))