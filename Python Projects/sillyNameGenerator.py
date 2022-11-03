#import sys to access system specific error message
#import random to pick random items from list
import sys, random
#introduce user to program, '\n' forces a new line
print("Welcome to the Psych 'Sidekick Name Picker.'\n")
print("A name just like Sean would pick for Gus:\n\n")

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'","Bob 'Stinkbug'", 'Bowel Noises',
                 'Boxelder', "Bud 'Lite' ", 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield', 'Chewy',
                 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer',
                 'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry', 'Huggy',
                 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny', 'Lemongrass', 'Lil Debil', 'Longbranch',
                 '"Lunch Money"', 'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
                 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff',
                 'Scut',"Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam',
                 'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
                 "Winston 'Jazz Hands'", 'Worms')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout', 'Butterbaugh', 'Clovenhoof',
        'Clutterbuck', 'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith', 'Goodpasture',
        'Guster', 'Henderson', 'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt',
        'Johnson','Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti',
        'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
        'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins', 'Sackrider',
        'Snuggleshine','Splern', 'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed',
        'Vinaigrette','Walkingstick', 'Wallbanger', 'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch',
        'Winterkorn','Woolysocks')
#while loop allows to continue running until told to stop in 'break' statement
while True:
    firstName = random.choice(first) #return random element from list
    lastName = random.choice(last)

    print("\n\n")
    print("{} {}".format(firstName, lastName), file=sys.stderr)
    print("\n\n")

    try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
    if try_again.lower() == "n":
        break

    input("\nPress Enter to exit.")
