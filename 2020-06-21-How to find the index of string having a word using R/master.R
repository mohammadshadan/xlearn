# Mohammad Shadan
# Question :
# How to find indexes of strings that contain a word 
# or pattern 


# Load the library
#install.packages("stringr")
library(stringr)

# =====================================================
# Creating Scenario
# All movies from Marvel Universe
# =====================================================

# movies = read.csv("../../datasets/marvel_movies.csv", 
#                   stringsAsFactors = FALSE)
# names(movies) = c("Movie", "US_release_date", 
#                   "Directors", "Screenwriters", 
# "Producers")
# View(movies)
# strings = tolower(movies$Movie[1:10])

string = c("iron man", "the incredible hulk", "iron man 2", "thor", "captain america: the first avenger",
           "marvel's the avengers", "iron man 3", "thor: the dark world",
           "captain america: the winter soldier", "guardians of the galaxy"
)

strings

# =====================================================
# Using stringr package
# =====================================================

?str_which
# syntax : str_which(string, pattern)
# Indexes of strings that contains a word or pattern

## Indexes of strings that contains the word "captain"
str_which(strings, "captain")

## check the presence of the word "thor"
str_which(strings, "thor")

# =====================================================
# Using Base R
# =====================================================
?grepl
# syntax : grepl(pattern, string)
# find "captain"
grep("captain", strings) # str_detect(strings, "captain")

# find "thor"
grep("thor", strings) # str_detect(strings, "thor")

# Summary
word ="captain"
strings
# using stringr package
str_detect(strings, word)

# using Base R
grepl(word, strings)


# Thank You :)



