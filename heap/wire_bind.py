# Given N gold wires, each wire has a length associated with it. At a time, only two adjacent small wires are assembled at 
# the end of a large wire and the cost of forming is the sum of their length. Find the minimum cost when all wires are 
# assembled to form a single wire.

# Suppose, Arr[]={7,6,8,6,1,1,}

# {7,6,8,6,1,1}-{7,6,8,6,2} , cost =2

# {7,6,8,6,2}- {7,6,8,8}, cost = 8

# {7,6,8,8} – {13,8,8}, cost=13

# {13,8,8} -{13,16}, cost=16

# {13, 16} – {29}, cost =29

# 2+8+13+16+29=68
# link: https://prepinsta.com/tcs-ninja/coding-questions/
# TODO: 