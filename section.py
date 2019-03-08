
def trims(s):
    while s[:1] != ' 'and s[-1:] != ' ':
        return s
    while s[:1] == ' ':
        return s[1:]
    while s[-1:] == ' ':
        return s[:-1]


s = trims(' hello ')
for i in range(len(s)):
    print(s[i])

