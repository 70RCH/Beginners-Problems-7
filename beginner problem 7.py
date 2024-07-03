#Have you seen this number before?
n = input().split()
s = set()
for i in n:
    if i in s:
        print('YES')
    else:
        print('NO')
        s.add(i)

#Special Words
s = input().split()
d = set(s)
a = sum(w.count('a') for w in d)
print(len(d))
print(a)

#Special Numbers
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = sorted(set(a) & set(b))
for i in c:
    print(i)

#Multilingual
n = int(input("How many people are there? "))
al = set()
cl = None
for i in range(n):
    m = int(input(f"(To person {i + 1}) How many languages can you speak? "))
    print("What languages can you speak in?")
    l = set(input().strip() for _ in range(m))
    al.update(l)
    if cl is None:
        cl = l
    else:
        cl.intersection_update(l)
print("\nNumber of languages everyone speaks:", len(cl))
print("Spoken language(s) everyone speaks:", ", ".join(cl))
print("Total languages spoken in the group:", len(al))
print("Languages spoken:", ", ".join(al))