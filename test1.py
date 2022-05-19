
def reverse(a: str) ->any:
    alist = list()
    for i in range(len(a)):
        alist.append(a[i])

    for i in range(len(alist)-1, -1, -1):
        print(alist[i], end="")
    return ''
print(reverse("ABCD"))