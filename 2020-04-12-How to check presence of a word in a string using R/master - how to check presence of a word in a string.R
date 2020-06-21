# How to check the presence of a word (pattern) in a string 
# or collection of strings ?
# 1. Present or not ? True or False output

# Load the library
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

# string = c("iron man", "the incredible hulk", "iron man 2", "thor", "captain america: the first avenger", 
#            "marvel's the avengers", "iron man 3", "thor: the dark world", 
#            "captain america: the winter soldier", "guardians of the galaxy"
# )
strings = tolower(movies$Movie[1:10])

string

# Check the presence of a word
# =====================================================
# Using stringr package
# =====================================================
# Check the presence of the word "captain"

?str_detect
# Detects the presence of a word (pattern) match 
# in a string/strings

str_detect(strings, "captain")

## check the presence of the word "thor"
str_detect(strings, "thor")

# =====================================================
# Using Base R
# =====================================================
?grepl
strings
grepl("captain", strings) #equivalent str_detect
grepl("thor", strings)

