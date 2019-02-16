#matrices as a nested list
# def func():
mx = [[1, 2], [3, 4], [5, 6]]
print[mx[0][0], mx[0][1], mx[1][0], mx[1][1], mx[1][0], mx[2][1]]

def mergeList():
    m=[ ]
    l=[[1,2],[3,4],[5,6]]
    for x in l:
        for y in x:
            m.append(y)
    return m

print(mergeList())

