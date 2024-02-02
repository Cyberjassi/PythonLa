
movies = []
while True:
    menu = input("What do you want to do? Add, List, Find, or Quit - respectively (a, l, f, q)\n")

    if menu == 'a':
        print("You chose to Add a Movie:\n")
        title = input("Your movie title name:\n")
        name = input("Your movie name:\n")
        director = input("Your movie director name:\n")
        print("\nYour Movie is Added:\n")
        newdic = {
            "title": title,
            "name": name,
            "director": director
        }
        movies.append(newdic)

    elif menu == 'l':
        print("\nHere are all your movies:")
        print(f"\nYour all movies -\n{movies}")

    elif menu == 'f':
        print("You chose to Find Your Movie:\n")
        findbytitle = input("Give me your Movie title name:\n")
        found = False
        for i in movies:
            if findbytitle == i['title']:
                print(i)
                found = True
                break

        if not found:
            print("Sorry, your movie is not in your movie list.\n")

    elif menu == 'q':
        exit()

    else:
        menu = input("\nWhat do you want to do? Add, List, Find - respectively (a, l, f)\n Or Quit by pressing q\n")
       

   
