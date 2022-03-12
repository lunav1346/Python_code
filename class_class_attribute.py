class person:
    bag = []

    def put_bag(self, stuff):
        person.bag.append(stuff)
        person.bag.sort()

h = person()
g = person()
h.put_bag('필통')
h.put_bag('노트북')
g.put_bag('보조배터리')
g.put_bag('책')

print(h.bag)
print(g.bag)