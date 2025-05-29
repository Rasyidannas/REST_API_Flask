friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

uni = friends.union(abroad)
print(uni)

both = friends.intersection(abroad)
print(both)
