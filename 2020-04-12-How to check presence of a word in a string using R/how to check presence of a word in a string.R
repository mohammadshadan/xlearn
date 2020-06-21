# Mohammad Shadan
# Question :
# How to check the presence of a word (pattern) in a string 
# or collection of strings ?
# Present or not present? True or False output

# Load the library
#install.packages("stringr")
library(stringr)

# =====================================================
# Creating Scenario
# All movies from Marvel Universe
# =====================================================

movies = read.csv("../../datasets/marvel_movies.csv", 
                  stringsAsFactors = FALSE)
names(movies) = c("Movie", "US_release_date", 
                  "Directors", "Screenwriters", 
"Producers")
View(movies)

strings = tolower(movies$Movie[1:10])
# string = c("iron man", "the incredible hulk", "iron man 2", "thor", "captain america: the first avenger", 
#            "marvel's the avengers", "iron man 3", "thor: the dark world", 
#            "captain america: the winter soldier", "guardians of the galaxy"
# )

strings

# Check the presence of a word
# =====================================================
# Using stringr package
# =====================================================
# Check the presence of the word "captain"

?str_detect
# syntax : str_detect(strings, pattern)
# Detects the presence of a word (pattern) match 
# in a string/strings

## check the presence of the word "captain"
str_detect(strings, "captain")

## check the presence of the word "thor"
str_detect(strings, "thor")

# =====================================================
# Using Base R
# =====================================================
?grepl
# syntax : grepl(pattern, string)
# find "captain"
grepl("captain", strings) # str_detect(strings, "captain")

# find "thor"
grepl("thor", strings) # str_detect(strings, "thor")

# Summary
word ="captain"
strings
# using stringr package
str_detect(strings, word)

# using Base R
grepl(word, strings)


# Thank You :)



