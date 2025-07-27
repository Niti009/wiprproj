facts = {
    "Jeff": "is afraid of dogs",
    "David": "plays the piano",
    "Jason": "can fly an airplane"
}

for person, fact in facts.items():
    print(f"{person} {fact}.")

print()  

facts["Jeff"] = "is afraid of heights"

facts["Jill"] = "can hula dance"

for person, fact in facts.items():
    print(f"{person}: {fact}.")
