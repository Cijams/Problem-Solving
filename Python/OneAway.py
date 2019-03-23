x1 = 'pale'  # insertion
x2 = 'ple'

t1 = 'pales'  # removal
t2 = 'pale'

y1 = 'pale'  # alteration
y2 = 'bale'

r1 = 'pale'
r2 = 'bake'  # 2 away, fake news.


def one_away(s1, s2):
    dict1 = {}
    dict2 = {}

    for _ in s1:
        if dict1.get(_) is None:
            dict1[_] = 1
        else:
            dict1[_] = dict1[_] + 1

    for _ in s2:
        if dict2.get(_) is None:
            dict2[_] = 1
        else:
            dict2[_] = dict2[_] + 1

    sum1 = sum2 = 0

    for e in dict1:
        if e in dict2:
            dict2[e] = dict2[e] - 1
            dict1[e] = dict1[e] - 1

    for e in dict1:
        sum1 += dict1[e]
    for e in dict2:
        sum2 += dict2[e]

    return sum1 <= 1 or sum2 <= 1


print(one_away(x1, x2))
print(one_away(t1, t2))
print(one_away(y1, y2))
print(one_away(r1, r2))
