import string
import re
aud = ['mp3', 'flac', 'alac', 'aac']
img = ['jpg', 'jpeg', 'png', 'bmp', 'gif']

def check(name, ext):
    for ch in name:
        if ch == '.':
            break
        elif not ch in string.ascii_letters:
            return False
    for e in ext:
        # reg = re.compile(r'[A-Za-z]*\.' + e)
        # if reg.match(name):
        #     return True
        if len(name) >= len(e) + 1:
            if name[len(name) - len(e) - 1:] == '.' +e:
                return True
    return False


def is_audio(file_name):
    return check(file_name, aud)

def is_img(file_name):
    return check(file_name, img)

print(is_img('nNBT.gif'))