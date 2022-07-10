
list.files("../datasets")
setwd("../datasets")
mcr = zip.file.extract("multipleChoiceResponses.csv", zipname = "kaggle-survey-2017.zip", unzip = getOption("unzip"))

?zip.file.extract
list.files()
library(data.table)
mcr = read.table(zipfile("kaggle-survey-2017.zip"))

mcr =read_csv("kaggle-survey-2017.zip")
attributes(mcr)
?read_csv

####
#https://www.youtube.com/watch?v=ax4LXQ5t38k
library(dplyr)
library(readr)
library(stringr)
library(tidyr)
rm(mcr)
mcr = read_csv("D:/Github/datasets/kaggle-survey-2017/multipleChoiceResponses.csv")
mcr = head(mcr, 30) %>% filter(!is.na(Country) & !is.na(WorkMethodsSelect))
names(mcr)

mcr %>% 
filter(!is.na(Country) & !is.na(WorkMethodsSelect)) %>%
mutate(work_method = str_split(WorkMethodsSelect, ",")) %>% 
select(Country,work_method) %>% 
  unnest()

mcr_lean_method = mcr %>% 
filter(!is.na(Country) & !is.na(LearningPlatformSelect)) %>%
mutate(learn_method = str_split(LearningPlatformSelect, ",")) %>% 
select(Country,learn_method) %>% 
  unnest()
mcr_lean_method
mcr_lean_method %>% count(learn_method, sort=TRUE)



# =============================================================================
# Merging (joining) multiple dataframe using Base R
# =============================================================================
# https://stackoverflow.com/questions/8091303/simultaneously-merge-multiple-data-frames-in-a-list
# https://stackoverflow.com/questions/14096814/merging-a-lot-of-data-frames

d1 = data.frame(id=1:3, x=1)
d2 = data.frame(id=1:4, q=2)
d3 = data.frame(id=1:3, z=3)
d1
d2
d3

# Inner Join
f = function(a,b){merge(a,b, by='id')}

# Full Join (Outer Join)
f = function(a,b){merge(a,b, by='id', all.x = TRUE, all.y = TRUE)}
Reduce(f, list(d1,d2,d3))
?merge
library(purr)


# Plotting mulitple columns of a dataframe
library(ggplot2)
head(mtcars)
m = mtcars
m["s_no"] = 1:dim(m)[1]
names(m)
ggplot(m) +
  geom_point(aes(x=s_no, y=drat, color="red")) +
  geom_point(aes(x=s_no, y=wt, color="blue")) +
  geom_line(aes(x=s_no, y=cyl, color="pink"))

ggplot(m) +
  geom_point(aes(x=s_no, y=drat)) +
  geom_point(aes(x=s_no, y=wt))

paste(c("Here", "There", "Everywhere"), collapse = "-")
# String Manipulation
library(stringr)

# How to detect a pattern in 
string <- c("Hiphopopotamus", "Rhymenoceros", "time for bottomless lyrics")
pattern <- "t.m"
grep(pattern, string)

str_detect(string, pattern)
str_subset(string, pattern)

#How to find if a word is present in a vector of strings/sentences ?
#How to check if a string includes a specific word in R
strings <- c("instance", 
             "percentage", 
             "n", 
             "instance percentage", 
             "percentage instance")

str_detect(strings, "instance")
str_detect(strings, "percentage")


# How to find if two or more words are present in a sentence ?
#https://stackoverflow.com/questions/44152970/r-grepl-to-find-multiple-strings-exists

str_detect(strings, "instance")
str_detect(strings, "percentage")

strings <- c("instance", "percentage", "n", 
          "instance percentage", "percentage instance")
pattern = "instance|percentage"
# 
str_c(pattern, collapse = "|")
pattern = "instance&percentage"
str_detect(strings, pattern)

str_detect(strings, "instance") & str_detect(strings, "percentage")
pattern = c("instance","percentage")
unlist(lapply(strings, function(x) {all(str_detect(x,pattern))}))
stringr::sentences[1:5]

#https://stackoverflow.com/questions/46260080/r-and-operator-in-regex
pos <- ("She sold seashells by the seashore, and she had a great time while doing so.") # contains sold and great
neg <- ("She bought seashells by the seashore, and she had a great time while doing so.") # contains great
strings = c(pos, neg)
pattern <- c("sold", "great")
str_detect(pos, pattern)
str_detect(neg, pattern)
str_detect(strings, pattern)
?str_detect
#One Sentence at a time
str_detect(pos, pattern)
all(str_detect(pos, pattern))
all(str_detect(strings, pattern))
#Below code works fine
unlist(lapply(strings, function(x) {all(str_detect(x,pattern))}))
lapply(strings, str_detect(pattern))

unlist(lapply(strings, function(x) {all(grep(pattern,x))}))
library(purr)
str_locate_all(strings, pattern)

lapply(strings, str_detect(pattern))

political <- c("Clinton", "Obama")
str_detect("Clinton", fixed(political, ignore_case = TRUE))

library(stringi)
stri_detect_fixed("test",c("et","es"))

stri_detect_fixed(c("test","testet"),c("et","es"))

## Steve Jobs Quotes
list.files("../datasets/")
sj_quotes = readLines("../datasets/steve_jobs_quotes.txt")
length(sj_quotes)
string = tolower(sj_quotes)
pattern = "vision"
library(dplyr)
str_detect(string, pattern) %>% table()
str_detect(string, pattern)
str_subset(string, pattern)


df = readClipboard()
?readClipboard
df

marvel_movies = read.csv("../datasets/marvel_movies.csv", stringsAsFactors = FALSE)
string = tolower(marvel_movies$Film)
str_detect(string, "Iron")
str_subset(string, "Iron")
str_subset(string, "Avenger")
str_subset(string, "the")
str_subset(string, "Avenger\\b")
str_subset(string, "ant\\b")
How to find if a word is present in a string