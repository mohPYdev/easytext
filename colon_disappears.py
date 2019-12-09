
import pyperclip


stri = []
text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == ':':
            stri.append(lines[i][:j]+'\r')

text = '\n'.join(stri)
pyperclip.copy(text)




