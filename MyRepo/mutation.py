t = [1, 2, 3]
t[1 : 3] = [t]
t.extend(t)
print(t)
# [...] means the whole process is keep going ...

t = [[1, 2], [3, 4]]
print(t[1])
t[0].append(t[1 : 2])
print(t)