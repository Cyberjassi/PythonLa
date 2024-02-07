def start_with_r(friend):
    return friend.startswith('R')

friends = ['Rolf','Jose','Randy','Anna']
start_with_r = filter(start_with_r,friends)

print(next(start_with_r))
print(next(start_with_r))
# print(next(start_with_r))

another_starts_with_r = (f 
                                                    for f in friends
                                                    if f.startswith('R'))

print(next(another_starts_with_r))
print(next(another_starts_with_r))