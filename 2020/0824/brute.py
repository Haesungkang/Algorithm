def brute(t, p):
     i, j = 0, 0
     while j < len(p) and i len(t):
         if t[i] != p[j]:
             i = i - j
             j  = -1
        i += 1
        j += 1
     if j == len(p):
         return i - len(p)
     return -1



text.find(pattern)