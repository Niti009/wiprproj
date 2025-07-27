f = input()
c = 0
d = {}

with open(f) as file:
    for line in file:
        c += 1
        for w in line.lower().split():
            w = ''.join(ch for ch in w if ch.isalnum())
            if w:
                d[w] = d.get(w, 0) + 1

t = f"{c} AM" if c <= 12 else f"{c - 12} PM"
p = max(d, key=d.get).capitalize() + " Street"

print("Meeting Time:", t)
print("Meeting Place:", p)


#2nd

import re

filename = input()

line_count = 0
word_freq = {}

with open(filename, 'r') as file:
    for line in file:
        line_count += 1
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1


if 1 <= line_count <= 24:
    if line_count == 12 or line_count == 24:
        meeting_time = "12 PM"
    elif line_count < 12:
        meeting_time = f"{line_count} AM"
    else:
        meeting_time = f"{line_count - 12} PM"
else:
    meeting_time = "Invalid time"

meeting_place = max(word_freq, key=word_freq.get).capitalize() + " Street"

print("Meeting Time:", meeting_time)
print("Meeting Place:", meeting_place)
