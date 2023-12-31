from hw03 import *
t, u, v = examples()
w = mobile(arm(3, t), arm(2, u))
weight = total_weight(w)
print(weight)
balanced(mobile(arm(1, v), arm(1, w)))