print("Welcome to Manga Adventure Recommender! ")
print("Let’s go on a journey to find your next manga...\n")

print("First, choose your path:")
print("1.  Action")
print("2.  Romance")
print("3.  Horror")
choice1 = input("Enter 1, 2, or 3: ")

print("\nNow, how long should the journey be?")
print("1. Long (100+ chapters)")
print("2. Medium (50-100 chapters)")
print("3. Short (under 50 chapters)")
choice2 = input("Enter 1, 2, or 3: ")

print("\nFinally, which era will you explore?")
print("1. 2000s")
print("2. 2010s")
choice3 = input("Enter 1 or 2: ")

genre_map = {"1": "Action", "2": "Romance", "3": "Horror"}
duration_map = {"1": "Long", "2": "Medium", "3": "Short"}
decade_map = {"1": "2000s", "2": "2010s"}

genre = genre_map.get(choice1)
duration = duration_map.get(choice2)
decade = decade_map.get(choice3)

mangas = {
    ("Action", "Long", "2000s"):
