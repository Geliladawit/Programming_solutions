# Problem: Recursively remove all adjacent duplicates - https://www.geeksforgeeks.org/recursively-remove-adjacent-duplicates-given-string/

def remove_(st):
    s = list(st)
    n = len(s)
    k = 0
    i = 0
    result = []
    while i < n:
        if i < n - 1 and s[i] == s[i + 1]:
            while i < n - 1 and s[i] == s[i + 1]:
                i += 1
        else:
            result.append(s[i])
        i += 1

    return "".join(result)