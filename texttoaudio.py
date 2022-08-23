# Week 2 Assignment


def primeproduct(m):
    primelist = []
    if m < 0:
        return False
    else:
        for i in range(2, m + 1):
            for p in range(2, i):
                if (i % p) == 0:
                    break
                else:
                    primelist.append(i)
            for x in primelist:
                y = m / x
                if y in primelist:
                    return True
            return False


def delchar(s, c):
    if len(c) > 1:
        return s
    else:
        return s.replace(c, '')


def shuffle(l1, l2):
    list_length = min(len(l1), len(l2))
    new_list = []
    for i in range(list_length):
        new_list.extend([l1[i], l2[i]])
    if len(l1) > list_length:
        new_list.extend(l1[list_length:])
    if len(l2) > list_length:
        new_list.extend(l2[list_length:])
    return new_list


#Week 3 Assisgnment


def contracting(l):
    result = 'True'
    if len(l) > 2:
        for v in range(len(l) - 2):
            abs_diff = abs(l[v] - l[v + 1])
            abs_diff_2 = abs(l[v + 1] - l[v + 2])
            if abs_diff <= abs_diff_2:
                result = 'False'
                break
    return result


def counthv(list):
    result = [0, 0]  #first is hc(hill_count) and second is vc(valley_count)
    if len(list) > 2:
        for v in range(1, len(list) - 1):
            if max(list[v], list[v + 1], list[v - 1]) == list[v]:
                result[0] = result[0] + 1
            elif min(list[v], list[v + 1], list[v - 1]) == list[v]:
                result[1] = result[1] + 1
    return result


def leftrotate(m):
    new_matrix = [[m[j][i] for j in range(len(m))]
                  for i in range(len(m[0]) - 1, -1, -1)]
    return new_matrix


def frequency(l):
    unique_l = list(set(l))
    freq_list = [l.count(x) for x in unique_l]
    min_freq_list = [
        unique_l[x] for x in range(len(freq_list))
        if freq_list[x] == min(freq_list)
    ]
    max_freq_list = [
        unique_l[x] for x in range(len(freq_list))
        if freq_list[x] == max(freq_list)
    ]
    min_freq_list.sort()
    max_freq_list.sort()
    return (min_freq_list, max_freq_list)


def onehop(list):
    new = []
    for i in range(len(list)):
        for j in range(len(list)):
            if i != j and list[i][1] == list[j][0]:
                q = list[i][0]
                w = list[j][1]
                if q != w:
                    t = (q, w)
                    if t not in new:
                        new.append(tuple(t))
    new.sort()
    return (new)


courses = []
students = {}
grades = {}
while True:
    s = input()
    if s == "Courses":
        d = 1
    elif s == "Students":
        d = 2
    elif s == "Grades":
        d = 3
    elif s == "EndOfInput":
        break

    else:
        s = s.split("~")
        if d == 1:
            courses.append(s)
        elif d == 2:
            students[s[0]] = s[1]
            grades[s[0]] = []
        elif d == 3:
            grades[s[-2]].append(s[-1])

points = {"A": 10, "AB": 9, "B": 8, "BC": 7, "C": 6, "CD": 5, "D": 4}

for idx in sorted(grades):
    p = [points[x] for x in grades[idx]]
    n = len(p) or 1
    marks = str(round(sum(p) / n, 2)) if p else "0"
    d = [idx, students[idx], marks]
    print("~".join(d))