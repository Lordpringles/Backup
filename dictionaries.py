
fname = open('clown.txt', 'r')

words = dict()

for line in fname:
	line = line.rstrip()
	licketySplit = line.split()
	for word in licketySplit:
		#print(word)
		words[word] = words.get(word, 0) +1 
		print(word, words[word])


drinks = {
	'martini': {'vodka', 'vermouth'},
	'black russian': {'vodka', 'kahlua'},
	'white russian': {'cream', 'kahlua', 'vodka'},
	'manhattan': {'rye', 'vermouth', 'bitters'},
	'screwdriver': {'orange juice', 'vodka'}
}

for drink, content in drinks.items():
	if content & {'vermouth', 'orange juice'}:
		print(drink)