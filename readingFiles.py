fhand = open('pokemon.txt', 'r')
print(fhand)

#inp = fhand.read()
#print(len(inp))

'''
count = 0
for hand in fhand:
	count += 1
	print(hand, '\n')

print('Line Count: ', count)


for line in fhand:
	line = line.rstrip()
	if not line.startswith('...'):
		continue
	print(line)
'''

count = 0
lineCount = 0
for line in fhand:
	count+=1
	if 'pi' in line:
		lineCount+=1
		print('line: ', count,' ', line.rstrip())

print(f'there are {lineCount} results that match your criteria' )
