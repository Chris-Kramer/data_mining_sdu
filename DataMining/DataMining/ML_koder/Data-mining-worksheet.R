

one_dim <- function(x,y)
	abs(x-y)^2

two_dim <- function(x,y,z,d)
	(abs(x-y)^2)+(abs(z-d)^2)

# CALCULATE TD2 OF S(1)
x1 <- one_dim(3,1) # 3 and 1
x2 <- one_dim(3,3) # 3 with itself
x3 <- one_dim(3,5) # 3 and 5

x4 <- one_dim(10,7) # 10 and 7
x5 <- one_dim(10,10) # 10 and 10
x6 <- one_dim(10,11) # 10 and 11
x7 <- one_dim (10,12) # 10 and 12

s1 <- sum(x1,x2,x3,x4,x5,x6,x7)

# CALCULATE TD2 FOR S(2)


