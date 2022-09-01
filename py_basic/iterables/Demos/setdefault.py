grades = {
    "English": 97,
    "Math": 93,
    "Art": 74,
    "Music": 86
}

grades.setdefault("Art", 87) # Art key exists. No change.
print("Art grade:", grades["Art"])

grades["Math"] = 77
print("Math grade:", grades["Math"])

grades.setdefault("Gym", 97) # Gym key is new. Added and set.
print("Gym grade:", grades["Gym"])