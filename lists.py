fname = open('mbox-short.txt', 'r')

for line in fname:
	if line.upper().startswith('FROM '):
		lickety = line.split()
		print(lickety[2])