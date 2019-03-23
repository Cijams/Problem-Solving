s1 = "Mr John Smith    "
s2 = "  Tes ting  "


def URLify(s):
    s = s.strip()
    s = s.split(" ")
    answer = ""
    for _ in s:
        answer += _
        answer += "%20"
    return answer[:-3]


s1 = URLify(s1)
s2 = URLify(s2)


assert(s1 == "Mr%20John%20Smith")
assert(s2 == "Tes%20ting")
print(s1)
print(s2)
