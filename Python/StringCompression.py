# Returns the compressed string if it is smaller than the original

t1 = "aabcccccaaa"
t2 = "abcdef"


def compress(s1):
    index = 0
    count = 1
    slist = []
    nlist = []
    while index < len(s1):
        if index+1 < len(s1) and s1[index] == s1[index+1]:
            count += 1
        else:
            slist.append(s1[index])
            nlist.append(count)
            count = 1
        index += 1
    answer = ""
    for i in range(len(slist)):
        answer += str(slist[i]) + str(nlist[i])
    return answer if len(answer) < len(s1) else s1


print(compress(t1))
print(compress(t2))
