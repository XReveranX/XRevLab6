def perevod(x):
    M = []
    while x != 0:
        M.append(x % 6)
        x //= 6
    M.reverse()
    return(len(set(M)))



#216^6 + 216^4 + 36^6 - 6^14 - 24^10
x = int(216**6 + 216**4 + 36**6 - 6**14 - 24**10)
print(perevod(x), " различных чисел в получившемся числе")
