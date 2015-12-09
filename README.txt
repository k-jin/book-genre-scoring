# book-genre-scoring
Score book genres based on keywords found in their description

Usage of this script:

python book_scorer.py books.json keywords.csv

books.json and keywords.csv are file paths to the correct file to pass into the script. 

I spent about 3 hours on this and would have liked to spend more if it weren't for finals. 

Some things I want to improve upon are runtime. Right now, I'm searching through entire text for each keyword. 
This means if there are n keywords, then I am searching through each description n times which is extremely inefficient.
Ideally, I would iterate through the description once and look for every keyword in that single iteration. 
I'm not sure how I would implement this though.
I use many loops and I'm sure there is some way of optimizing this that I haven't had the chance to figure out yet.
I was planning on using regular expressions but the keywords weren't overly complex so that was unnecessary.

An interesting case I didn't notice until the very end was that certain keywords could be associated with multiple genres.
I had to go back and make some adjustments to my code,
such as the data structure I was using to hold keywords and their genres, and some of the logic to fit the new data structure.
It was an unexpected surprise but wasn't too hard to address.
