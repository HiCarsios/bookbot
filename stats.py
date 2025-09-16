def get_word_count(path):
	with open(path) as f:
		texts = f.read()
		textsplit = texts.split()
		count = len(textsplit)
	return count

def Number_Character(path):
	with open(path) as f:
		texts = f.read()
		ultimate = {}
		lowertext = texts.lower()
		listword =  list(lowertext)
		for l in listword:
			if l in ultimate:
				ultimate[l] +=1
			else:
				ultimate[l] = 1
	return ultimate

def sort_on(items):
	return items["num"]

def sorted(items):
	listings = items.sort(reverse=True, key=sort_on)
	return listings
