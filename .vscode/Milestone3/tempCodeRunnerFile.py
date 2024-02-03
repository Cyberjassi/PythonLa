menu = input("What you want to Do? Add List Find for that - respectively (a,l,f) And for Quit press q\n")

movies = []

while menu!='q':
    if menu == 'a':
        print("you Choose Add Movie-\n")
        title = input("Your movie title name-\n")
        name = input("Your movie  name-\n")
        director = input("Your movie director name-\n")
        print("\nYoure Movie is Added:\n")
        newdic = {
            "title":title,
            "name":name,
            "director":director
        }
        movies.append(newdic)
        

    elif menu == 'l':
        print("\nHere All Your Movies: ")
        print(f"\nYour all movies -\n{movies}")
    elif menu == 'f':
        print("You choose Find Your movie:\n")
        findbytitle = input("Give me your Movie title name:\n")
        print(f"Your movies-\n")
        for i in movies:
            if(findbytitle == i['title']):
                print(i)
            else:
                print("Sorry Your movies is not there in your movie list:\n")
    elif menu == 'q':
        exit()
    else:
        print("You Typed Wrong Operation! ")
    menu = input("\nWhat you want to Do? Add List Find for that - respectively (a,l,f)\n And for Quit press q\n")
        