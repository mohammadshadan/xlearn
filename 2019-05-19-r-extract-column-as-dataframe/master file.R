head(mtcars)

mtcars$mpg
mtcars[,c("mpg", "cyl"), drop=FALSE]
mtcars[1:14,c("mpg"), drop=FALSE]

mtcars[c("mpg", "cyl")]
mtcars[c("mpg")]
mtcars[,"mpg",drop=FALSE]
mtcars["mpg"]

library(dplyr)
mtcars_tbl = as_tibble(mtcars)
mtcars_tbl$mpg
mtcars_tbl[,"mpg", drop=TRUE]
select(mtcars,mpg)
library(ggplot2)
head(diamonds)
diamonds$carat
diamonds[, "carat", drop=FALSE]
diamonds["carat"]


mtcars[,"mpg"]
