from collections import Counter
from collections import defaultdict
from collections import deque
temperature = [14,13,14,15,13,14,15,12,13,14,12,15]
count = Counter(temperature)
print(count[14])

print(Counter({'hello':5,'hi':54})['hi'])

a = "aaabbbbccc"
count = Counter(a)
print(count)
print(count.most_common(1))


d = defaultdict(int)
d['1'] = 8
d['b']= 6
print(d['c'])

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.appendleft(1)
d.extend([1,2,3])
d.extendleft([1,2,3])
d.rotate(1)
d.rotate(-1)
print(d)

