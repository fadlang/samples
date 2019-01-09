# function arguments and return values
# are both from right side
# assume fucntion add(a, b, a + b)

add(2, 2, 4)
add(1, 2, 3)

# using sith variables
add(2, 2, S)
> S = 4

# Special operator @ - sets the
# value of function call
add(2, 2, @)
> 4

add(2, @, 4)
> 2

# Assume  two function defined
# add - add two numbers
# cons - concatenate list

# next lines will just compile
add(2, 2, 4)
cons(1, [2, 3], [1, 2, 3])

cons(H, T, [1, 2, 3])
print(H) # 1
print(T) # [1, 2]

# We want to write funtion that
# returns summ of list
# summ of empty list = 0
def summ(
    [],
    0
)

# summ(L, S)
def summ(
    cons(H, T, @), # cons(H, T, L)
    add(H, summ(T, @), @) # S = summ(T, S2), add(H, S2, S)
)

summ([1, 2], 3)
