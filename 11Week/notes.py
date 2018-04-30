import random
import pronouncing


new_word = input('Enter a word: ')
rhyme = random.choice(pronouncing.rhymes(new_word))
print(rhyme)

#netcat (nc) command line tool to open http connection
#example nc blog.alden.website 80
#GET /
#Host: blog.alden.website
