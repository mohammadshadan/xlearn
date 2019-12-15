#In R how to extract a single column from a data.frame as a data.frame ?

head(mtcars)
mtcars[, c("mpg", "cyl")]
mtcars[, c("mpg")]
mtcars[, c("mpg"), drop=FALSE]
mtcars[1:6, c("mpg"), drop=FALSE]
col_names = c("mpg")
col_names = c("mpg", "cyl", "hp")
mtcars[1:6, col_names, drop=FALSE]

mtcars["mpg"]

#Summary
df[1:now, col_names, drop=FALSE]
mtcars[1:7, "mpg", drop=FALSE]
