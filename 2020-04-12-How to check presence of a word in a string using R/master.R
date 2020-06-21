# How to check the presence of a word (pattern) in a string 
# or collection of strings ?
# 1. Present or not ? True or False output
# 2. Find the indices of strings that contain the word
# 3. Return the strings which has the word 


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
strings

# =====================================================
# Using stringr package
# =====================================================
# Check the presence of the word "captain"

# 1. Detect the presence of a word (pattern) match in a string/strings
str_detect(strings, "captain")

#Find the indices of strings that contains the word(pattern) match
str_which(strings, "captain") 

#Return only the strings that contains the word (pattern)
str_subset(string, "captain")


## check the presence of the word "thor"
str_detect(strings, "thor")
str_which(strings, "thor")
str_subset(strings, "thor")

# string[str_detect(string, "thor")]
# string[str_which(string, "thor")]
# str_subset(string, "thor")

# =====================================================
# Using Base R
# =====================================================
grepl("captain", strings) #equivalent str_detect
grep("captain", strings)  #equivalent to str_which

# grep("captain", string, value=TRUE) #str_subset


?grepl
