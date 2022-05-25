<<<<<<< HEAD
class FourCal():
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal()
a.setdata(4, 2)

print(a.first)
print(a.second)
=======

def reverse(a: str) ->any:
    alist = list()
    for i in range(len(a)):
        alist.append(a[i])

    for i in range(len(alist)-1, -1, -1):
        print(alist[i], end="")
    return ''
print(reverse("ABCD"))
>>>>>>> 5d8f17be2046b57a1a2e82c673f3f2511a8ff54b
