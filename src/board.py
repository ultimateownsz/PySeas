import random

from .validate_inputs import validate_inputs
from .inventory import Inventory
from .money import Money
from .selling import (
    chest_wealth,
    chest_ancient,
    chest_ashen,
    chest_captain,
    chest_cursed,
    chest_greg,
    chest_legend,
    chest_mermaid,
    chest_rage,
    chest_strong
)
from .buying import (
    basic_quest,
    medium_quest,
    hard_quest,
    drunken_quest
)


player_inventory = Inventory()
player_wallet = Money(currency="Gold", worth=0)

class Board:
    def __init__(self, players):

        # all the sea of thieves inspired locations you can visit on the board        
        self.locations = [
            "start", "isle", "event", "isle", "harbor", "pirate_king", "isle", 
            "captain_blazeheart", "harbor", "the_syndicate", "harbor", "change", "isle", 
            "isle", "pirate_king", "isle", "wreckage_isle", "harbor", "ghost_brig", 
            "harbor", "event", "isle", "isle", "pirate_king", "harbor", "captain_blazeheart", 
            "harbor", "the_syndicate", "isle", "chance", "harbor", "harbor", "pirate_king", 
            "wreckage_isle", "red_sea", "red_sea", "red_sea"
        ]

        # created a list with an index and locations in a dict to handle the game logic of landing on a tile on the board to call a function     
        self.locations_with_index = []
        for i, c in enumerate(self.locations):
            self.locations_with_index.append({
                "index": i, "location": c
            })
        self.current_position: int = self.locations_with_index[0]["index"]

        # when a player rolls the dice he/she lands on one of these tiles and a function gets called

        # we had the idea to color all the tiles later on but due to time constrains we did not had the time to implement this
        self.locations_actions = {
            "start": self.visit_start,  # yellow
            "isle": self.visit_isle,  # white
            "event": self.visit_event,  # green
            "harbor": self.visit_harbor,  # white
            "pirate_king": self.visit_pirate_king,  # grey
            "captain_blazeheart": self.visit_captain_blazeheart,  # grey
            "the_syndicate": self.visit_the_syndicate,  # red
            "change": self.visit_change,  # purple
            "wreckage_isle": self.visit_wreckage_isle,  # brown
            "ghost_brig": self.visit_ghost_brig,  # black
            "red_sea": self.visit_red_sea,  # white
        }
        self.players = {player.player_id: 0 for player in players}

    def visit_locations_by_index(self, index: int):
        '''
        This handles all the functions in self.locations_actions
        When a player lands on a tile the action variable gets called and via that logic a function gets called when it is in the self.locations list
        '''
        location = self.locations[index]
        action = self.locations_actions.get(location)
        if action:
            action()

    def update_player_position(self, player, total_roll):
        '''Logic of the game that updates the current player pos to a new player pos when the dices are throwed'''
        # current position of the player
        current_position = self.players[player.player_id]
        # new position after roll
        new_position = (current_position + total_roll) % len(self.locations_with_index)
        # update current position of the player
        self.players[player.player_id] = new_position
        return new_position

    def test(self):
        '''
        This is an old function cause before I was still busy by implementing the logic when you throw the dice, land on a tile, a function gets called
        '''
        pass
    #     print("Board is working!")

    def visit_start(self):
        print("You are at the start.")
        # self.test()

    # added a randomizer to call different isles you could visit as player
    def visit_isle(self):
        print("You arrived at an isle.")
        # isle = "Island"
        # isles = [can_cove, cres_isle, lone_cove, m_hide, s_bounty, smug_bay, wand_ref]
        # rand_isle = random.randrange(len(isles))
        # print(f"You arrived at {isles[rand_isle]}")
        # print("\nThere is a chest on the isle.")

    # we had events you could encounter like sea of thieves does
    def visit_event(self):
        # print("You encountered an event.\n")
        loc_1 = "Red Tornado"
        loc_2 = "Green Tornado"

        sea_events = [loc_1, loc_2]
        event = random.choice(sea_events)
        print(f"\nYou sail with your crew and on the horizon you see", event)

        if event == loc_1:
            player_inventory.extension(chest_rage)
            print("""You see a specific storming red tornado on a horizon and decide to sail and confront it! Uppon arrival you see the legendary Ashen Lord Red Ruth. 
                     You emmidiatly engage in a battle with the Ashen Lord. Its a truely hellish battle. She summons her troops to help her fight you off. 
                     It rains fire balls out of the red sky! Everywhere it shoots fire! You barely survive that fight but in the end you kill the ruthless Lord and het your reward...""")
            print("\nYou get a dangerous Doom Chest!")
        elif event == loc_2:
            player_inventory.extension(chest_cursed)
            print("""You see a specific storming green tornado on a horizon and decide to sail and confront it! 
                  You arrive and what you see is a frightening sight. Ghost ships come out of portals appearing on the sea! 
                  You fight them off. You fight them all off! Heaps and heaps of waves of ghos ships appear and you and your crew fight them until they're all sunk! 
                  You see your price on the see!""")
            print("\nYou get a dangerous Cursed Chest!")
        return event

    # just as sea of thieves you could visit the different sea posts in the game.
    def visit_harbor(self):
        '''I came up with some star constellation to name these harbors'''
        aquila = "The Aquila"
        north_star = "The North Star Constellation"
        great_har = "The Great Trade Harbor"
        steph_spoils = "Stephan's Spoils"
        great_bear = "The Great Bear"
        phoenix_store = "The Phoenix Store"
        orion = "Orion the Hunter"
        mermaid = "Mermaid Twins"

        harbors = [aquila, north_star, great_har, steph_spoils, great_bear, phoenix_store, orion, mermaid]
        rand_harbor = random.randrange(len(harbors))
        print(f"You arrived at {harbors[rand_harbor]}")

    # a randomizer of questions the pirate king could ask you if you landed on his tile
    def visit_pirate_king(self):
        print("You encountered the Pirate King.")
        q1 = """What is the main objective in PySeas?
                A. Collecting treasure
                B. Battling mythical creatures
                C. Exploring ancient ruins """
        pirate_king = [q1]

        question = random.choice(pirate_king)
        print(f"Let me ask ye a question, matey!", question)
        is_valid_choice = False
        while not is_valid_choice:
            inp_choice = validate_inputs("So what is it then? ", str).lower()
            is_valid_choice = inp_choice
            if not is_valid_choice:
                print("Didn't they learn you to read, fool? Try again! ")
        if question == q1:
            if inp_choice == "c":
                print("I've never heard that one in me life! Piss off! No gold for you...")
            elif inp_choice == "b":
                print("Mate, you'll walk the plank next time if ya give such a pathetic answer again!")
            elif inp_choice == "a":
                player_inventory.extension(chest_captain)
                print("Well done, privateer! I'll reward you good for this one.")
        # self.test()

    # just as the pirate lord tile, this logic was the same on here
    def visit_captain_blazeheart(self):
        print("You encountered Captain Blazeheart.")
        q1 = """Which of the following is not a type of ship available in PySeas?  
                A) Brigantine 
                B) Galleon 
                C) Sloop """

        cap_blaze = [q1]

        question = random.choice(cap_blaze)
        print(f"Let me ask ye a question, matey!", question)
        is_valid_choice = False
        while not is_valid_choice:
            inp_choice = validate_inputs("So what is it then? ", str).lower()
            is_valid_choice = inp_choice
            if not is_valid_choice:
                print("Didn't they learn you to read, sea dog? Try again! ")
        if question == q1:
            if inp_choice.lower() == "c":
                print("I've never heard that one in me life! Piss off! No gold for you...")
            elif inp_choice.lower() == "b":
                print("Mate, you'll walk the plank next time if ya give such a pathetic answer again!")
            elif inp_choice.lower() == "a":
                player_inventory.extension(chest_captain)
                print("Well done, privateer! I'll reward you good for this one.")

    def visit_the_syndicate(self):
        '''This is the shop where you could buy quests, sell chests you found or got via events etc'''

        print("You visit the Syndicate.")
        while True:
            print("""Welcome to the shop, privateer! There are a couple of actions you could do!:
            1. Choose and buy a quest for a chest!
            2. Check your inventory to see if you have enough gold!
            3. If you have something you'd like to sell, sell it here!
            4. Check how much gold you have!
            5. If you don't mean no bussiness, I'll welcome you another round! Farewell!
            """)
            choice = input("So, what are ya wating for? What is it?: ")

            if choice == "1":
                print("""Available Quests:
                1. Quest for the burried treasure - 200 gold
                2. Quest for the Lost Chest - 1000 gold
                3. Quest for the Drunken Sailor - 1250 gold
                4. Quest for the The Vault - 1750 gold
                """)
                quest_choice = input("Wich one would you like to buy, privateer? ")
                if quest_choice == "1":
                    player_wallet.buy_quest(basic_quest)
                    player_inventory.extension(chest_captain.name)
                    print("""You've got a map that leads to the burried treasure.  
                             You make your way all the way to Cutlass Cay and dig out a wonderfull Captain's Chest""")
                elif quest_choice == "2":
                    player_wallet.buy_quest(medium_quest)
                    player_inventory.extension(chest_strong.name)
                    print("""You got a misterious compass. Although your facing north, the compass doesnt point that way.  
                             It seems that the misterious compass shows you the way to the Lost Treasure!  
                             You quickly gather your crew and sail to the location given by the misterious compass.  
                             You arrive at a vulcanic isle and you see the treasure but its guarded by skeletons.  
                             You and your crew quickly fight them of and take whats yours! """)
                elif quest_choice == "3":
                    player_wallet.buy_quest(hard_quest)
                    player_inventory.extension(chest_ancient.name)
                    print("""The Pirate gives you a location of the Drunken Sailor. The Hoarder adds that he is in a possession of a great price! 
                             You sail forth to the location and you find a port. You ask the locals of they know about the Drunken Sailor and they tell you about the local tavern. There you find the drunken bastard sleeping with a barrel under his foot. 
                             You slowly but quietly take the barrel out of his possession and you take it onto your ship. You notice that when holding the treasure your view is distorted and you can’t walk straight. You’re drunk!
                             It seems to be the effect of holding the barrel. You also hear in your head the famous sea shanty “Drunken Sailor”... Great! Now you have the chest of thousands Grogs and a shanty in your head...""")
                elif quest_choice == "4":
                    player_wallet.buy_quest(drunken_quest)
                    player_inventory.extension(chest_greg.name)
                    print("""You raise your sails and sail forth to the location.  
                             Uppon arrival it seems that there is no treasure but only another map that leads to a new locations.  
                             You sail to a couple isles with your new maps you keep finding and you arrive at a fort where you find a burned compas.  
                             It leeds you to a isle and the vault on it. You open the vault and see all the treasure it contains.  
                             You take the first chest and suddenly the vault starts to close. You panic and run away with only one chest. """)
                else:
                    print("I don't have that quest in me shop! Try again!")

            elif choice == "2":
                player_inventory.show_eq()

            elif choice == "3":
                print("This is what you can sell: ")
                player_inventory.show_eq()
                print("""Chest's overwiev:
                    1. Chest of Fortune - 9500 gold
                    2. Legendary Chest - 8600 gold
                    3. Captain's Chest - 560 gold
                    4. Chest of the Damned - 1160 gold
                    5. Chest of a Thousand Grogs - 2500 gold
                    6. Coral Marauder's Chest - 910 gold
                    7. Ashen Seafarer's Chest - 520 gold
                    8. Stronghold's Chest - 2000 gold
                    9. Chest of Rage - 3500 gold
                    10. Chest of Ancient Tributes - 3000 gold
                    """)

                while True:
                    chest_choice = input("What would you like to sell? (Press q to quit selling): ").lower().isnumeric()
                    if chest_choice == "q":
                        break
                    if chest_choice == "1":
                        player_wallet.sell_chest(chest_wealth)
                        player_inventory.remove_item(chest_wealth.name)
                    elif chest_choice == "2":
                        player_wallet.sell_chest(chest_legend)
                        player_inventory.remove_item(chest_legend.name)  
                    elif chest_choice == "3":
                        player_wallet.sell_chest(chest_captain)
                        player_inventory.remove_item(chest_captain.name)
                    elif chest_choice == "4":
                        player_wallet.sell_chest(chest_cursed)
                        player_inventory.remove_item(chest_cursed.name)                       
                    elif chest_choice == "5":
                        player_wallet.sell_chest(chest_greg)
                        player_inventory.remove_item(chest_greg.name)                      
                    elif chest_choice == "6":
                        player_wallet.sell_chest(chest_mermaid)
                        player_inventory.remove_item(chest_mermaid.name)                   
                    elif chest_choice == "7":
                        player_wallet.sell_chest(chest_ashen)
                        player_inventory.remove_item(chest_ashen.name)                     
                    elif chest_choice == "8":
                        player_wallet.sell_chest(chest_strong)
                        player_inventory.remove_item(chest_strong.name)
                    elif chest_choice == "9":
                        player_wallet.sell_chest(chest_rage)
                        player_inventory.remove_item(chest_rage.name)
                    elif chest_choice == "10":
                        player_wallet.sell_chest(chest_ancient)
                        player_inventory.remove_item(chest_ancient.name)
                    print("Something else you'd like to sell? (Press q to quit selling) ")

            elif choice == "4":
                player_wallet.show_money()
            elif choice == "5":
                print("Farewell, bloody Pirate!")
            else:
                print("There is no choice like that, try again!")
            break
        # self.test()

    # just like monopoly you could get a change card, because of time constraints couldn't we get this finished in time
    def visit_change(self):
        print("You landed on change.")
        # self.test()

    # on the board you can land on shipwreck isles, these are also randomized
    def visit_wreckage_isle(self):
        # print(f"You found {wreck_land[rand_land]}")
        wreck_1 = "La Dama Negra"
        wreck_2 = "El Impulto"
        wreck_3 = "The Black Pearl"
        land = "Nassau"

        wreck_land = [wreck_1, wreck_2, wreck_3, land]
        # rand_land = random.randrange(len(wreck_land))
        random_item = random.choice(wreck_land)
        print("You dwell with your crew through the sea and find", random_item)

        if random_item == wreck_1:
            player_inventory.extension(chest_mermaid)
            print("""A great man'o'war galleon that once was feared on the seas... Now, its just a wreck. It seems a Pirate Legend has defeated the Legendary ship. 
                     You dive into the water and swim into the shipwreck.!""")
            print("\nYou find a Coral Marauder's Chest!")
        elif random_item == wreck_2:
            player_inventory.extension(chest_strong)
            print("""Once the most powerfull ship that these seas have ever seen. Fast, a strong fire power and mighty ram attack. 
                     Now it's just shipwreck with many others, but its legend goes on...
                     You dive into the water and swim into the shipwreck.""")
            print("\nYou find a Stronghold chest!")
        elif random_item == wreck_3:
            player_inventory.extension(chest_legend)
            print("""Every Pirate knows the legend of the Black Pearl! Once the fastest ship on the seas, a ghost ship, with black sails, a damned crew and a Captain so evil that hell itself spat him back out... 
                     It has been told that people entering the black pearl never came back, but then, where are the stories comming from? You dive into the water and swim into the shipwreck.""")
            print("\n You find a Chest of the Damned!")

    # we wanted to have this as a jail, we could not get to this and hope we may get it later if we refactor the game to pygame for instance
    def visit_ghost_brig(self):
        print("You are visting the Ghost Brig.")
        # self.test()

    # in sea of thieves you have boundaries, we made some tiles the red sea, maybe redundant but in practice it is okay for what you do with it
    def visit_red_sea(self):
        '''We need another name for red sea.'''
        print("You are sailing in the dangerous sea.")
        # self.test()

    # this is an higher order function that calls the other functions to print out the board
    def print(self):
        self.print_header_board()
        self.print_left_right_board()
        self.print_footer_board()

    def print_header_board(self) -> None:
        '''Prints out the header of the board'''

        row_c = self.locations_with_index[18:28]
        print(" ._________________________________________________. ")

        # creates a new list with all the index numbers
        new_row_c = [str(cell["index"]) for cell in row_c]
        # print(new_row_c)

        # print a '|' between every index number
        header = " | ".join(new_row_c)

        # print the header with a '|' on both ends
        print(" | " + header + " | ")
    
    def print_left_right_board(self) -> None:
        '''Prints the left/right border of the board'''

         # haal de rijen met indexnummers op
        row_b = self.locations_with_index[10:18]
        row_d = self.locations_with_index[28:36]

        # for row_b we had to make it reverse, because of in the assignment we had to make the board clockwise, otherwise it could not work.
        # reverse de list
        row_b.reverse()

        # loops through all the index numbers
        for i in range(len(row_b)):
            cell_column_b = row_b[i]["index"]
            cell_column_d = row_d[i]["index"]

            board_row = f" | {cell_column_b} |                                       | {cell_column_d} |"
            print(board_row)
    
    def print_footer_board(self) -> None:
        '''Prints the footer of the board'''

        # gets the first row of all index numbers
        row_a = self.locations_with_index[0:10]

        row_a.reverse()

        # new list with index numbers only
        new_row_a = []

        # format the index numbers and append them to the list
        for cell in row_a:
            new_row_a.append("{i:>02}".format(i=cell["index"]))

        # create a formatted str from the formatted index numbers
        formatted_row = " | ".join(new_row_a)
        print(f" | {formatted_row} | ")
