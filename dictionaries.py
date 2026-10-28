import time
print("*you enter Miraziz's shop that is better than hank and terren shop*")
print("cashier/owner: hi i have good tings, plz buy I try to make look pretty but I lazy")
better_local_corner_store_than_hank_and_terren_items = [
    {
        "name": "anti-matter/1 gram",
        "price": 7.99,
        "department": "Back pocket",
        "description": "Anti-matter that my 2 week old son made in the womb, I got alot more than you think :wink:"
    },
    {
        "name": "Banana Anti-matter/1 gram",
        "price": 10.99,
        "department": "Back pocket",
        "description": "Anti-matter my son made, but from a banana, tastes yummy"
    },
    {
        "name": "Colision Anti-matter/1 gram",
        "price": 9.49,
        "department": "Back pocket",
        "description": "Anti matter from colision, is kinda stinky but still good."
    },
    {
        "name": "Doge",
        "price": 19.99,
        "department": "Pet",
        "description": "Funny dog, let you play doge miner :D, make good money but lot of mining."
    },
    {
        "name": "e-",
        "price": .99,
        "department": "Back pocket",
        "description": "electron, is smol, I lost some one time, but i found them :D."
    },
    {
        "name": "fanta",
        "price": 328871247.99,
        "department": "juice",
        "description": "yummy."
    },
    {
        "name": "god",
        "price": 499.99,
        "department": "Back pocket",
        "description": "He's me bro."
    },
    {
        "name": "Harvard",
        "price": 2.99,
        "department": "Make mom proud",
        "description": "we like harvard, you want harvard, you got it. what a 'degree'? "
    },
    {
        "name": "Indestructable sift-ite tools, armor, weapons, food, and other stuff max enchant",
        "price": 9.99,
        "department": "Game",
        "description": "minecaft is good, i got you all the good enchantmewnts on all the armor, even a secret one to keep after death, smth like prot 255, sharp 255, unb 255, eff 255, looting 255, elytra+chestplate. and anything else you want :D, includes free creative mode tooo, i like this, i recomend"
    },
    {
        "name": "j*b/1 hour",
        "price": -18.99,
        "department": "Game",
        "description": "Is fun like a game."
    },
    {
        "name": "food",
        "price": .99,
        "department": "food",
        "description": "any food you want."
    },
    {
        "name": "ting",
        "price": 4.99,
        "department": "thing",
        "description": "anyting for u."
    },
    {
        "name": "1 money",
        "price": 0.01,
        "department": "thing",
        "description": "money :drool:."
    },
    {
        "name": "ownership of everything",
        "price": 67.69,
        "department": "Thing",
        "description": "lol 67.69."
    },
    {
        "name": "Verity",
        "price": 6.70,
        "department": "Thing",
        "description": "Hey, it's me Verity, your personal helper friend. Ask me anything, I know everything/ Hey it's me, it's Verity, ask me anything. I know about a million things, ill do anything. (blah blah blah) What is the capital ofd framce? oui ui ui, it is paris, merci. What does the cow say? Oh moo moo moo, I speak that too, all day"
    },
    {
        "name": "Hank's shop",
        "price": .67,
        "department": "Thing",
        "description": "you buy hank shop :O, do yes, is very bad shop, too expensive"
    },
    {
        "name": "everyting fom Hank's shop",
        "price": .01,
        "department": "Thing",
        "description": "you buy ting hank shop :O fom me 0_0, do yes, is very bad shop, too expensive tis cheap"
    },
    {
        "name": "\"Hank\"",
        "price": -1000.00,
        "department": "Pet",
        "description": "you buy hank please?"
    },
    {
        "name": "everyting fom Terren's shop",
        "price": 0,
        "department": "Thing",
        "description": "you buy ting Terren shop :O fom me 0_0, do yes, is very bad shop, too expensive tis cheap"
    },
    {
        "name": "\"Terren\"",
        "price": -1000.00,
        "department": "Pet",
        "description": "you buy Terren please?"
    },
    {
        "name": "msic ting",
        "price": 1.99,
        "department": "Thing",
        "description": "music yes buy?"
    },
    {
        "name": "everything class/2 weeks",
        "price": -10000,
        "department": "Thing",
        "description": "class"
    }
    
]
your_cart = []
while True:
    print(" ")
    action = int(input("what would you like to do\n1. see stock\n2. leave"))
    if action == 2:
        print("*you sadly leave my shop*")
        break
    elif action == 1:
        print("0: leave")
        time.sleep(.1)
        for index, item in enumerate(better_local_corner_store_than_hank_and_terren_items):
            time.sleep(.1)
            print(index+1 , ":" , item["name"])
        view = int(input("what do you want to see? "))
        print(" ")
        print(better_local_corner_store_than_hank_and_terren_items[view-1]["name"])
        print(better_local_corner_store_than_hank_and_terren_items[view-1]["price"])
        print(better_local_corner_store_than_hank_and_terren_items[view-1]["department"])
        print(better_local_corner_store_than_hank_and_terren_items[view-1]["description"])
        input(" \n so what would you like to do?\n 1. put in cart\2. put back")