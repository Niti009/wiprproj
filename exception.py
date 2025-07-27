f = input("Enter the file name: ")
p = f_ = t = d = 0

try:
    for l in open(f):
        l = l.strip()
        if not l: continue
        x = l.split(' ', 1)
        if len(x) < 2: continue
        a, b = x[0], x[1].strip()
        if a.lower() == "discount":
            try: d = int(b)
            except: d = 0
        elif b.lower() == "free":
            f_ += 1
        else:
            try:
                t += int(b)
                p += 1
            except: continue
except:
    print("File not found")
    exit()

print("No of items purchased:", p)
print("No of free items:", f_)
print("Amount to pay:", t)
print("Discount given:", d)
print("Final amount paid:", max(0, t - d))
