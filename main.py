import sys

def get_book_text(path):
	with open(path) as f:
		texts = f.read()

	return  texts


def main():
	try:
		sys.argv[1]
	except Exception:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
		prtint("test")
		return
	link = sys.argv[1]
	from stats import get_word_count
	count = get_word_count(link)
	sentance = f"Found {count} total words"
	#print(sentance)
	from stats import Number_Character
	numchar = Number_Character(link)
	#print(numchar)
	numalpha =[]
	for a in numchar:
		tempdict ={}
		moretemp ={}
		if a.isalpha():
			moretemp[a] = numchar[a]
			tempdict = {"char": a ,"num": numchar[a]}
			numalpha.append(tempdict)
	#print(numalpha)
	from stats import sort_on
	numalpha.sort(reverse=True, key=sort_on)
	#print(numalpha)
	ultra = ""
	for e in numalpha:
		great = f"""{e["char"]}: {e["num"]}
	"""
		ultra = ultra + great
	statement = f"""
	============ BOOKBOT ============
	Analyzing book found at books/frankenstein.txt...
	----------- Word Count ----------
	{sentance}
	--------- Character Count -------
	{ultra}
	============= END ===============
	"""
	print(statement)
#def main():
#	frank = get_book_text("./books/frankenstein.txt")
#	print(frank)
#
main()

