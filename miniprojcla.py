liked_str = input()
disliked_str = input()
given_str = input()

liked = set(map(int, liked_str.split('-')))
disliked = set(map(int, disliked_str.split('-')))
given = list(map(int, given_str.split('-')))

happiness = 0

for num in given:
    if num in liked:
        happiness += 1
    elif num in disliked:
        happiness -= 1

print(happiness)
