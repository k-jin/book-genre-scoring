import json, sys, csv, string, operator
from pprint import pprint

if (len(sys.argv) != 3):
	print "usage: python book_scorer.py books.json keywords.csv"
	exit(0)

# books is an array of dictionaries
# each book has keys "title" and "description"

with open(sys.argv[1]) as jsonfile:
	books = json.load(jsonfile)

# scores is a dictionary of dictionaries where 
# key: keyword
# value: dictionary of points:
#		key: genre
#		value: points 
# ie:
# keywords = {"fast paced":{"action": 7},
# 			"distant future":{"action": 4, "sci-fi": 8},
# 			"fight":{"action": 6}}

keywords = {}
with open(sys.argv[2]) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		keyword = row[" Keyword"][1:]
		if keyword in keywords:
			keywords[keyword][row["Genre"]] = int(row[" Points"])
		else:
			keywords[keyword] = {row["Genre"]: int(row[" Points"])}

# bookKeywordCount is a dictionary of dictionaries where the key is the book title
# values are dictionaries of dictionaries of keywords where the keys are the genres 
# values are the number of occurences of the keyword
# ie: {"Hunger Games": {
#						"action":{"distant future": 1,
#								  "fight": 2},
# 						"sci-fi":{"future": 1}
#						},
# 	   "Infinite Jest": {"literary fiction":{"subplot": 1,
#											 "cerebral": 1},
#						 "sci-fi":{"future": 1}}
#      }
# bookScores is a dictionary of dictionaries where the key is the book title
# values are dictionaries of scores where the keys are the genres 
# ie: {"Hunger Games": {
#						"action":15, 
# 						"sci-fi":8
#						},
# 	   "Infinite Jest": {"literary fiction":12,
#						 "sci-fi":8
#      }



bookKeywordCount = {}
bookScores = {}

# looping through every book we imported
 
for book in books:
	currTitle = book["title"]
	currDescription = book["description"]
	bookKeywordCount[currTitle] = {}
	bookScores[currTitle] = {}

	# search for every keyword in each book description
	for keyword in keywords:
		# count the number of occurrences for each keyword
		matches = string.count(currDescription, keyword)
		for i in range(matches):
			for genre in keywords[keyword]:
				# add to the genre and keyword count bookKeywordCount
				# initialize bookScores for each new genre found
				if genre in bookKeywordCount[currTitle]:
					if keyword in bookKeywordCount[currTitle][genre]:
						bookKeywordCount[currTitle][genre][keyword] += 1
					else:
						bookKeywordCount[currTitle][genre][keyword] = 1
				else:
					bookKeywordCount[currTitle][genre] = {keyword:1}
					bookScores[currTitle][genre] = 0

	# calculate the score of each genre found in the current book 
	for genresInBook in bookKeywordCount[currTitle]:
		keywordScores = []
		keywordCount = 0
		for keywordsInBook in bookKeywordCount[currTitle][genresInBook]:
			keywordScores.append(keywords[keywordsInBook][genresInBook])
			keywordCount += bookKeywordCount[currTitle][genresInBook][keywordsInBook]
		bookScores[currTitle][genresInBook] = sum(keywordScores) / len(keywordScores) * keywordCount

	# pad bookScores if there are less than 3 genres found in the book description
	for keyword in keywords:
		for genre in keywords[keyword]:
			if (len(bookScores[currTitle]) >= 3):
				break
			if genre not in bookScores[currTitle]:
				bookScores[currTitle][genre] = 0

# sort books alphabetically
sortedBooks = sorted(bookScores.items(), key=operator.itemgetter(0))

# for each book, print its title and its top 3 genres along with their scores
for book in sortedBooks:
	print book[0]
	sortedGenres = sorted(book[1].items(), key=operator.itemgetter(1))
	genreLength = len(sortedGenres)
	for i in range(3):
		print sortedGenres[genreLength - 1 - i][0] + ", " + str(sortedGenres[genreLength - 1 - i][1])	
	print "\n"
