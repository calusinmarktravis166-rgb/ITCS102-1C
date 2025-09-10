print("Welcome to Manga Reader Recommender!")
print("Answer a few questions to find your next read.")

genre = input("What genre do you like? (action, romance, horror): ").lower()
duration = input("How long should the manga be? (long, medium, short): ").lower()
time = input("From which decade? (2000s, 2010s): ").lower()

if genre == "action":
    if duration == "long" and time == "2000s":
        print("The available mangas are: Naruto, Bleach")
    elif duration == "long" and time == "2010s":
        print("The available mangas are: Attack on Titan, My Hero Academia")
    elif duration == "medium" and time == "2000s":
        print("The available mangas are: Fullmetal Alchemist")
    elif duration == "medium" and time == "2010s":
        print("The available mangas are: Tokyo Ghoul")
    elif duration == "short" and time == "2000s":
        print("The available mangas are: Trigun")
    elif duration == "short" and time == "2010s":
        print("The available mangas are: One Punch Man")

elif genre == "romance":
    if duration == "long" and time == "2000s":
        print("The available mangas are: Fruits Basket")
    elif duration == "long" and time == "2010s":
        print("The available mangas are: Ao Haru Ride")
    elif duration == "medium" and time == "2000s":
        print("The available mangas are: Lovely★Complex")
    elif duration == "medium" and time == "2010s":
        print("The available mangas are: Horimiya")
    elif duration == "short" and time == "2000s":
        print("The available mangas are: Kare Kano")
    elif duration == "short" and time == "2010s":
        print("The available mangas are: Daytime Shooting Star")

elif genre == "horror":
    if duration == "long" and time == "2000s":
        print("The available mangas are: Monster")
    elif duration == "long" and time == "2010s":
        print("The available mangas are: Ajin")
    elif duration == "medium" and time == "2000s":
        print("The available mangas are: Gantz")
    elif duration == "medium" and time == "2010s":
        print("The available mangas are: Parasyte")
    elif duration == "short" and time == "2000s":
        print("The available mangas are: Uzumaki")
    elif duration == "short" and time == "2010s":
        print("The available mangas are: I Am a Hero")

else:
    print("Sorry, no mangas found for your choices.")
