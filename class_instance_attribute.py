class person:
    def __init__(self):
        self.bag = []

    def pub_bag(self, stuff):
        self.bag.append(stuff)
        self.bag.sort()

H = person()
H.pub_bag('노트북')
H.pub_bag('필통')

G = person()
G.pub_bag('책')
G.pub_bag('연필')

print(H.bag)
print(G.bag)