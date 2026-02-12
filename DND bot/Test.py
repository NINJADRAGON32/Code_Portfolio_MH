# player_dict={("","")}
# idea here is to use parallel lists to act as a mutable "dict"
# init_players=[]
# init_rolls =[]
# def init_add_player(player, roll):
#     # first we add the players and rolls to the listat the same time
#     init_players.append[player]
#     init_rolls.append[roll]
#     # then we want to sort the two lists based off of the value of the rolls
#     #  so anything we do to one list we *MUST* do to the other
#     for i in range(len(init_rolls)):
#         for j in range(0, len(init_rolls) - i - 1):
#             if init_rolls[j] < init_rolls[j + 1]:
#                 # Swap if the next number is larger
#                 init_rolls[j], init_rolls[j + 1] = init_rolls[j + 1], init_rolls[j]
#                 init_players[j], init_players[j + 1] = init_players[j + 1], init_players[j]
#     return(init_players,init_rolls)





# UIP = ""
# while UIP!="stop":
#     UIP = str(input("what player would you like to add: "))
#     UIR = int(input("what roll did this player have: "))
#     print(init_add_player(UIP,UIR))

# con testing 
# ui = str(input("enter (con set) _[player]_[spell]"))
# concentration={}
# while ui != "stop":
#     try:
#         _,_, player, spell = ui.strip().split()
#         if player in concentration:
#             ui= str(input(f"{player} is already concentrating on a spell do you still wish to change concentrations (y/n):"))
#             if ui == "y":
#                 print(f"{player} is now concentrating on {spell}")
#                 concentration[player]= spell
#     except ValueError:
#         None

# concentration = {}
# print (type(concentration))

