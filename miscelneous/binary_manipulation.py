# Joseph is learning digital logic subject which will be for his next semester. 
# He usually tries to solve unit assignment problems before the lecture. Today he got one tricky question. 
# The problem statement is “A positive integer has been given as an input. Convert decimal value to binary representation. 
# Toggle all bits of it after the most significant bit including the most significant bit. 
# Print the positive integer value after toggling all bits”.
# link: https://prepinsta.com/tcs-ninja/coding-questions/

def get_bin(val):
    bin = ""
    while val != 0:
        rem = val % 2
        bin = str(rem) + bin
        val = val // 2
    return bin

def get_decimal(bin):
    l, dec = len(bin), 0
    for i in range(l):
        dec += (2 ** (l-i-1) * int(bin[i]))
    # print(dec)
    return dec

def get_toggle_bin(bin):
    return "".join(["0" if b == "1" else "1" for b in bin])

def get_final_result(val):
    bin = get_bin(val)
    bin = get_toggle_bin(bin)
    return get_decimal(bin)

print(get_final_result(5))
print(get_final_result(4))
print(get_final_result(7))
print(get_final_result(10))