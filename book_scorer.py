import json, sys, csv, string, operator
from pprint import pprint

# books is an array of dictionaries
# each book has keys "title" and "description"
books = [
{
  "title": "Infinite Jest",
  "description": "With its baroque subplots, zany political satire, morbid, cerebral humor and astonishing range of cultural references, Wallace's brilliant but somewhat bloated dirigible of a second novel (after The Broom in the System) will appeal to steadfast readers of Pynchon and Gaddis. But few others will have the stamina for it. Set in an absurd yet uncanny near-future, with a cast of hundreds and close to 400 footnotes, Wallace's story weaves between two surprisingly similar locales: Ennet House, a halfway-house in the Boston Suburbs, and the adjacent Enfield Tennis Academy. It is the 'Year of the Depend Adult Undergarment' (each calendar year is now subsidized by retail advertising); the U.S. and Canada have been subsumed by the Organization of North American Nations, unleashing a torrent of anti-O.N.A.N.ist terrorism by Quebecois separatists; drug problems are widespread; the Northeastern continent is a giant toxic waste dump; and CD-like 'entertainment cartridges' are the prevalent leisure activity. The novel hinges on the dysfunctional family of E.T.A.'s founder, optical-scientist-turned-cult-filmmaker Dr. James Incandenza (aka Himself), who took his life shortly after producing a mysterious film called Infinite Jest, which is supposedly so addictively entertaining as to bring about a total neural meltdown in its viewer. As Himself's estranged sons?professional football punter Orin, introverted tennis star Hal and deformed naif Mario?come to terms with his suicide and legacy, they and the residents of Ennet House become enmeshed in the machinations of the wheelchair-bound leader of a Quebecois separatist faction, who hopes to disseminate cartridges of Infinite Jest and thus shred the social fabric of O.N.A.N. With its hilarious riffs on themes like addiction, 12-step programs, technology and waste management (in all its scatological implications), this tome is highly engrossing?in small doses. Yet the nebulous, resolutionless ending serves to underscore Wallace's underlying failure to find a suitable novelistic shape for his ingenious and often outrageously funny material."
},

{
  "title": "Hunger Games",
  "description": "In a not-too-distant future, the United States of America has collapsed, weakened by drought, fire, famine, and war, to be replaced by Panem, a country divided into the Capitol and 12 districts. Each year, two young representatives from each district are selected by lottery to participate in The Hunger Games. Part entertainment, part brutal intimidation of the subjugated districts, the televised games are broadcasted throughout Panem as the 24 participants are forced to eliminate their competitors, literally, with all citizens required to watch. When 16-year-old Katniss's young sister, Prim, is selected as the mining district's female representative, Katniss volunteers to take her place. She and her male counterpart, Peeta, the son of the town baker who seems to have all the fighting skills of a lump of bread dough, will be pitted against bigger, stronger representatives who have trained for this their whole lives. Collins's characters are completely realistic and sympathetic as they fight and form alliances and friendships in the face of overwhelming odds; the plot is tense, dramatic, and engrossing. This book will definitely resonate with the generation raised on reality shows like 'Survivor' and 'American Gladiator.' Book one of a planned trilogy."
}
]

# scores is a dictionary of arrays where each array has 
# index 0 = genre
# index 1 = points
# 

keywords = {"fast paced":["action", 7],
			"distant future":["action", 4],
			"fight":["action", 6],
			"murder":["mystery", 5],
			"death":["mystery", 8],
			"explosive":["mystery", 4],
			"great man":["biography", 7],
			"great woman":["biography", 7],
			"future":["sci-fi", 8],
			"dystopian":["sci-fi", 7],
			"space":["sci-fi", 6],
			"subplot":["literary fiction", 5], 
			"cerebral":["literary fiction", 7],
			"literary":["literary fiction", 9]}


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
 
for book in books:
	currTitle = book["title"]
	currDescription = book["description"]
	bookKeywordCount[currTitle] = {}
	bookScores[currTitle] = {}
	for keyword in keywords:
		matches = string.count(currDescription, keyword)
		for i in range(matches):
			genre = keywords[keyword][0]
			if genre in bookKeywordCount[currTitle]:
				if keyword in bookKeywordCount[currTitle][genre]:
					bookKeywordCount[currTitle][genre][keyword]+=1
				else:
					bookKeywordCount[currTitle][genre][keyword] = 1
			else:
				bookKeywordCount[currTitle][genre] = {keyword:1}
				bookScores[currTitle][genre] = 0

	for genresInBook in bookKeywordCount[currTitle]:
		keywordScores = []
		keywordCount = 0
		for keywordsInBook in bookKeywordCount[currTitle][genresInBook]:
			keywordScores.append(keywords[keywordsInBook][1])
			keywordCount += bookKeywordCount[currTitle][genresInBook][keywordsInBook]
		bookScores[currTitle][genresInBook] = sum(keywordScores) / len(keywordScores) * keywordCount

	for keyword in keywords:
		if (len(bookScores[currTitle]) >= 3):
			break
		genre = keywords[keyword][0]
		if genre not in bookScores[currTitle]:
			bookScores[currTitle][genre] = 0

sortedBooks = sorted(bookScores.items(), key=operator.itemgetter(0))

for book in sortedBooks:
	print book[0]
	sortedGenres = sorted(book[1].items(), key=operator.itemgetter(1))
	genreLength = len(sortedGenres)
	for i in range(3):
		print sortedGenres[genreLength - 1 - i][0] + ", " + str(sortedGenres[genreLength - 1 - i][1])	
	print "\n"
