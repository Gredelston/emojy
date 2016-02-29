import sys
from translations import orig_translation
trns = ""
with open(sys.argv[1]) as bffile:
	for char in bffile.read():
		if char in ['.', ',', '[', ']', '<', '>', '+', '-']:
			trns += orig_translation[char]
		else:
			trns += char
if len(sys.argv) > 2:
	with open(sys.argv[2], "w") as emojyfile:
		emojyfile.write(trns)
else:
	print(trns)