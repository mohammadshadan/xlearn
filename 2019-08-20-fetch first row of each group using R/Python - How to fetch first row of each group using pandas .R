# How to fetch first row of each group using R ?

#https://stackoverflow.com/questions/31528981/select-first-and-last-row-from-grouped-data/31529043


## Creating Scenario
df = data.frame("Year"=c('2019', '2019', '2019', '2019', 
                           '2018', '2018', '2018', '2018', 
                           '2017','2017', '2017', '2017'),
                "Quarter"=c(1,2,3,4,
                            1,2,3,4,
                            1,2,3,4),
                "Sales"=c(5000, 6000, 2000, 3000, 
                          2300, 1400, 5400, 6200,
                          7230, 5600, 3200, 1600))
df
library(dplyr)

# Method 1
# First
df %>% group_by(Year) %>% do(head(.,1))
# Last
df %>% group_by(Year) %>% do(tail(.,1))
# Method 2
# First
df %>% group_by(Year) %>% slice(3)
# Last
df %>% group_by(Year) %>% slice(n())

# Method 3 using data.table
library(data.table)
# First
as.data.table(df)[, .SD[c(1)], by=Year]
# Last
as.data.table(df)[, .SD[c(.N)], by=Year]

   