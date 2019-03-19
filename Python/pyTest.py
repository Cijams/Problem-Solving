s = 'Truck'
t = 'Truck'
o = 'Brick'


def is_perm(s1, s2):
    hm = {}
    # Ensure they are the same length.
    if len(s1) != len(s2):
        return False
    # Add each le
    for each in s1:
        if hm.get(each) is None:
            hm[each] = 1
        else:
            hm[each] = hm[each]+1
    # Check to make sure all of s2 is in s1, the same number of times.
    for each in s2:
        if hm.get(each) is None or hm.get(each) < 1:
            return False
    return True


print(is_perm(s, t))  # True
print(is_perm(t, o))  # False
