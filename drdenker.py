import re


def kandidaten(woorden, lengte, letter, pos):
	aantal = 0
	for woord in woorden:
		woord = woord.split()[0]
		woord = woord.split('/')[0]
		if len(woord) == lengte and woord[pos-1] == letter:
			print(woord)
			aantal += 1
			
	print('\n')
	print(aantal)



if __name__ == "__main__":
	with open('nldict.txt') as f:
		lines = f.readlines()
		
	kandidaten(lines, 11, 'e', 4)
	#kandidaten(lines, 9, 'm', 4)

