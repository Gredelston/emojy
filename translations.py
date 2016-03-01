def reverse_dict(d):
	nd = {y:x for x,y in d.items()}
	return nd

	
orig_translation = {
	">":"🖕",
	"<":"👇",
	"+":"👆",
	"-":"👎",
	"[":"🔁",
	"]":"🔚",
	".":"👄",
	",":"👂"
	}

translation = reverse_dict(orig_translation)