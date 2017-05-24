import string
def pig_it(text):
    word = ''

    def pig(s):
        return (s + s[0])[1:] + 'ay' if s != '' else ''

    res = ''
    for ch in text:
        if ch not in string.ascii_letters:
            res += pig(word) + ch
            word = ''
        else:
            word += ch
    return res + pig(word)

print(pig_it('Pig latin is cool'))