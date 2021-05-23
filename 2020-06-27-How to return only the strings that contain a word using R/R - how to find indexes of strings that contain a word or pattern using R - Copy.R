# Mohammad Shadan
# Question :
# How to find indexes of strings that contain a word 
# or pattern match

# =====================================================
# Creating Scenario
# All movies from Marvel Universe
# =====================================================

string = c("iron man", "the incredible hulk", 
           "iron man 2", "thor", 
           "captain america: the first avenger",
           "marvel's the avengers", "iron man 3", 
           "thor: the dark world", 
           "captain america: the winter soldier", 
           "guardians of the galaxy"
)

strings

# Load the library
# install.packages("stringr")
library(stringr)

# =====================================================
# Using stringr package
# =====================================================

?str_which
# syntax : str_which(string, pattern)
# Indexes of strings that contains a word or pattern

## Indexes of strings that contains the word "captain"
str_which(strings, "captain")
which(str_detect(strings, "captain"))

## Indexes of strings that contains the word "thor"
pattern = "thor"
str_which(strings, pattern)


# =====================================================
# Using Base R
# =====================================================
?grep
# syntax : grep(pattern, string)
# find indices of strings which contain "captain"
grep("captain", strings)

# find indices of strings which contain "thor"
grep("thor", strings)

# Summary
pattern="captain"
strings

# Using stringr package
str_which(strings, pattern)
which(str_detect(strings, pattern))

# Using Base R
grep(pattern, strings)

# Thanks You :)


