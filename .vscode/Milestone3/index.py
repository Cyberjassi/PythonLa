menu = input("What you want to Do? Add List Find for that - respectively (a,l,f)\n And for Quit press q\n")

movies = []

while menu!='q':
    if menu == 'a':
        title = input("Your movie title name-\n")
        name = input("Your movie  name-\n")
        director = input("Your movie director name-\n")
        
        newdic = {
            "title":title,
            "name":name,
            "director":director
        }
        movies.append(newdic)
        break

    elif menu == 'l':
        pass
    elif menu == 'f':
        pass
    elif menu == 'q':
        exit()
    else:
        print("You Typed Wrong Operation! ")

