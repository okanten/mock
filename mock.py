import sys, pyperclip

if len(sys.argv) > 1:
    input = list(sys.argv[1].lower())
else:
    input = list(pyperclip.paste())
result = ""
for i, letter in enumerate(input):
    if i % 2 == 0:
        result = result + letter.upper()
    else:
        result = result + letter
if list(pyperclip.paste()) == input:
    pyperclip.copy(result)
else:
    print(result)
