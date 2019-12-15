#https://stackoverflow.com/questions/16325641/how-to-extract-the-first-n-rows-per-group
#https://stackoverflow.com/questions/34753050/data-table-select-first-n-rows-within-group

#How to extract the first n rows per group using R ?

library(data.table)
dt <- data.table(mtcars)
dt = dt[order(dt$cyl),]
head(dt)
dim(dt)

dt[,head(.SD,1), "cyl"]
dt[,head(.SD,1), cyl]

dt[,.SD[1], "cyl"]

dt[,.I[1], dt$cyl]
  

## Using dplyr
library(dplyr)
#iterage over sub-groups
dt %>% group_by(cyl) %>% do(head(.,1))
