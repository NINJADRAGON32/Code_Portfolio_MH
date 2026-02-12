import os
from dotenv import load_dotenv
import discord
import random
import re


#--------------------------------------------------------------------------------------------------------------------
"""
    This is A discord application meant to be used in an asynchronous settings so that long distance friends can play DND together easily and accesibly.
    Note: This was made with help of AI software.

"""
#  security for github
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents setup
intents = discord.Intents.default()
intents.message_content = True

# Bot setup
bot = discord.Client(intents=intents)

# Libraries-----------------------------------------------------------------------------------------------------------
#status
status = {}
# concentration
concentration = {}


# NPC name generator lists
first_names = ["Karlach","shadowheart","Astarion","Abasolo","Abbas","Abdin","Thalorin", "Brynna", "Kaelen", "Zanros", "Elyra", "Morthos",
    "Anira", "Garrick", "Lorana", "Tovak", "Seraphine", "Durgan","Ace", "Addie", "Addison", "Adi", "Adrean", 
    "Adrian", "Aiden", "Ainsleigh", "Ainsley", "Ainslie","Brady","Evan","Austin"
    "Alex", "Alexis", "Allie", "Ally", "Alta", "Amari", "Andee", "Andi", "Andie", "Andy", "Angel",
    "Arden", "Ari", "Ariel", "Armani", "Ash", "Asta","Ashe", "Ashley", "Ashton", "Aspen", "Aubrey", "Auburn",
    "Aude", "Audie", "Audy", "August", "Averi", "Avery", "Ayden", "Bailee", "Bailey", "Baylee",
    "Billie", "Billy", "Blair", "Bobbie", "Bobby", "Brayden", "Briggs", "Brook", "Brooklyn", "Brynn",
    "Cacey", "Caden", "Cadence", "Cady", "Caelin", "Caiden", "Cam", "Camden", "Camdyn", "Cameron",
    "Campbell", "Camron", "Camryn", "Carlen", "Carmen", "Carson", "Carter", "Casey", "Cassidy",
    "Cayden", "Caylin", "Cedar", "Charlie", "Chey", "Chris", "Christan", "Cobie", "Coby", "Codie",
    "Cody", "Coren", "Corey", "Corrie", "Cory", "Cyan", "Cyd", "Cypress", "Cyprus", "Dakota", "Dale",
    "Dallas", "Dana", "Dani", "Dannie", "Danny", "Darci", "Darcy", "Darrell", "Darryl", "Dayrl",
    "Delaney", "Demi", "Demy", "Devan", "Devin", "Devyn", "Diamond", "Dominique", "Dorian", "Drew",
    "Dusty", "Dylan", "Easton", "Eden", "Elisha", "Ellery", "Elliot", "Ellis", "Ellory", "Elly",
    "Ember", "Embry", "Embyr", "Emerson", "Emery", "Emory", "Eris", "Esme", "Esmé", "Fae", "Fen",
    "Fenn", "Fin", "Finley", "Finn", "Florence", "Forrest", "Fox", "Fran", "Frances", "Gabbi",
    "Gabby", "Genesis", "Gerrie", "Gerry", "Gris", "Griz", "Grizz", "Hailey", "Haley", "Halie",
    "Halley", "Harlen", "Harlow", "Harlyn", "Harper", "Hartley", "Hayden", "Haylee", "Hayley",
    "Hilary", "Hollis", "Hunter", "Idgie", "Iggie", "Iggy", "Indigo", "Ira", "Izzy", "Jackie",
    "Jade", "Jaidan", "Jaiden", "Jaidin", "Jaidyn", "Jaime", "Jaimie", "Jamie", "Jan", "Jay",
    "Jaydan", "Jayden", "Jaydin", "Jaydyn", "Jaylin", "Jayme", "Jean", "Jerrie", "Jerry", "Jess",
    "Jesse", "Jessie", "Jett", "Jo", "Jody", "Joe", "Joey", "Jonni", "Jonnie", "Jude", "Juniper",
    "Justice", "Kacey", "Kacie", "Kaden", "Kai", "Kaiden", "Kam", "Kameron", "Kamron", "Karter",
    "Kasey", "Kay", "Kayden", "Kaylin", "Kelly", "Kelsey", "Kelsie", "Kendall", "Kerri", "Kerry",
    "Kirby", "Kit", "Kodi", "Koree", "Koren", "Kory", "Kris", "Krishna", "Kristen", "Ky", "Kye",
    "Kyle", "Kyrie", "Lacy", "Lain", "Landry", "Lane", "Larkin", "Laurel", "Lauren", "Lauris",
    "Leaf", "Lee", "Leighton", "Lennon", "Lennox", "Lesley", "Leslie", "Lin", "Lindsay", "Linn",
    "Logan", "London", "Londyn", "Lonnie", "Loren", "Lorin", "Lou", "Lowe", "Luan", "Luca", "Lyn",
    "Lynn", "Mackenzie", "Mackinley", "Madison", "Madox", "Mallory", "Marin", "Marion", "Marley",
    "Marlowe", "Mars", "Mason", "Mckinley", "Meadow", "Mel", "Meredith", "Merrill", "Micah", "Micki",
    "Mika", "Mischa", "Misha", "Morgan", "Neely", "Nicki", "Nico", "Nikko", "Niko", "Nova", "Paige",
    "Paisley", "Parker", "Pat", "Pax", "Payton", "Peyton", "Phoenix", "Piper", "Presley", "Quinn",
    "Rae", "Rain", "Raine", "Rainn", "Raven", "Ray", "Reagan", "Reese", "Reilly", "Remi", "Rémi",
    "Remington", "Remy", "Rémy", "Rey", "Riley", "River", "Robbie", "Robin", "Rogue", "Rori", "Rory",
    "Russi", "Ryan", "Rylan", "Rylee", "Ryley", "Sage", "Salix", "Sam", "Sammie", "Sammy", "Sandi",
    "Sandy", "Santana", "Sasha", "Sawyer", "Scout", "Seneca", "Shannon", "Shay", "Shea", "Shelley",
    "Siban", "Sibán", "Sky", "Skylar", "Skyler", "Slater", "Spencer", "Stacy", "Stevie", "Storm",
    "Syd", "Sydney", "Tash", "Tate", "Tatum", "Tay", "Tayler", "Taylor", "Teagen", "Teal", "Teegan",
    "Terra", "Terry", "Tobin", "Tommie", "Toni", "Tony", "Tori", "Torrey", "Tory", "Tracey", "Traci",
    "Tracy", "Tristen", "Tristyn", "Tyler", "Val", "Valentine", "Viv", "Vivian", "Whitney", "Willow",
    "Xan", "Xander", "Yael", "Zan", "Zane", "Zephyr", "Zoe", "Zoé", "Zoë", "Zoey", "Mitchell","Caden"]

last_names = ["Alarwynn", "Azurith", "Aethelnoth", "Arnoria", "Aurielis", "Anvindr", "Arquenya", "Aldravia", "Aerendyl", "Astryx",
    "Baeloria", "Brystion", "Beltharum", "Byrandir", "Bladewyn", "Briarquen", "Berynth", "Bronithar", "Belloria", "Baxtalion",
    "Caelumis", "Corvynia", "Crythandor", "Caladrex", "Cerindel", "Cynoria", "Chrysolarn", "Cindarion", "Calithen", "Carvahl",
    "Darnathil", "Dravynor", "Dalquor", "Dyrindale", "Dathemir", "Drisella", "Dorneval", "Dyrenoth", "Delmira", "Daxion",
    "Elyrion", "Ethandor", "Evindale", "Eragoth", "Eldrith", "Evaris", "Elyndra", "Exorian", "Elcarus", "Eronoth",
    "Faelwen", "Ferindar", "Fyrinth", "Feloria", "Fendrel", "Faervel", "Frosthelm", "Findariel", "Falcryn", "Faelar",
    "Galdorin", "Grivale", "Gharnost", "Galenthia", "Gryndoll", "Gwyrveth", "Ghorum", "Glorindel", "Gaerwyn", "Grendar",
    "Halendil", "Harnoth", "Hyrindale", "Haelora", "Harvion", "Helsarin", "Haldren", "Herimoth", "Hystoria", "Hylexan",
    "Illyrion", "Ivrindel", "Isendur", "Ithelis", "Ildoran", "Ivren", "Ixian", "Ilmarith", "Ithren", "Iskaral",
    "Jorathil", "Jenvor", "Jalendu", "Jirelia", "Jynthor", "Jaldan", "Jervion", "Jolara", "Juskar", "Jaxenel",
    "Kaelith", "Kyrendor", "Kiravia", "Kaldwen", "Korvael", "Kyrnath", "Kethriel", "Kolvir", "Kasirel", "Kyrion",
    "Lyrandar", "Lathrendis", "Luminar", "Lorveth", "Lytherion", "Lysirel", "Lendrak", "Levindor", "Larcath", "Lyrasol",
    "Myrthalian", "Morvendir", "Malendith", "Meriloth", "Myrandor", "Mirevael", "Malthorin", "Myliar", "Melthar", "Morithal",
    "Nyrandel", "Norvith", "Neltharion", "Nythoria", "Nalvendil", "Nevrim", "Narithus", "Nirefal", "Nyxalinth", "Nolendur",
    "Othendal", "Orivir", "Olyndir", "Orendar", "Ormathil", "Olvarin", "Ovrion", "Othmiral", "Ondolyn", "Orilam",
    "Pyrandel", "Pellinor", "Phirendale", "Parvion", "Pyrathen", "Palendria", "Prisandor", "Phaelara", "Penthriel", "Pyrovar",
    "Quilendil", "Qyrvanth", "Quorinthal", "Qyndarion", "Quilmaras", "Qarvex", "Quelindor", "Qynorel", "Quorven", "Quilthar",
    "Ryntharion", "Ravendel", "Rhovaril", "Raelith", "Rendalin", "Rythorin", "Relmaras", "Rithandor", "Ranethil", "Raxion",
    "Sylvendil", "Sarnorith", "Serindar", "Soltharion", "Syraveth", "Skorvix", "Stelmaria", "Sylrak", "Sendoril", "Sylithen",
    "Thalrendir", "Tervaleth", "Tyroth", "Trisendel", "Tarnolir", "Thyrindor", "Telmaran", "Tolvir", "Threndil", "Torvael",
    "Ultharion", "Urvendil", "Uthrendar", "Uldoria","Renfro","Pillow","Gardner","Seaton","Sims","Gillet","Lamey"]

help = """
    f"Hello {message.author}, to use DiceBot3000 simply type the following commands into the chat: \n 
    !roll : followed by how many of a type of dice you wish to roll\n 
    !npc : to generate a random name \n 
    !con set : to create a set a concentration spell for a player of choice
    !con break : to break a concentration on a certain player.
    !con show : to show who is concentrating on what
    !con clear : to clear all concentrations
    !stats [name] [race] to roll for stats for a character

"""

# main----------------------------------------------------------------------------------------------------------------
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):

    # This is here just incase so that the bot doesn't respond to itself
    if message.author == bot.user:
        return
    

    content = message.content.lower()


    
    # HELP!!!!!!!!!!!!!! ----------
    if content.startswith("!help"):
        await message.channel.send(help)

    # Easter eggs!!! ----------
    elif content.startswith("!hello there") or content.startswith("!hellothere") :
        await message.channel.send("General Kenobi")
        return
    
    # NPC name generator ----------
    elif content.startswith("!npc"):
        first = random.choice(first_names)
        last = random.choice(last_names)
        await message.channel.send(f" *{first} {last}.*")
        return
    
    # initiative roller and tracker ------------------------------------------------------------------------
    '''
        for the initiative roller and tracker im thinking of making a copy of every tracker so that i can integrate it into the turn counter. 
        Maybe I could use a variable called combat and set combat equal to false by default and true after the initiative tracker has been set.
    '''




    #Status tracker ----------------------------------------------------------------------------------------
    # add a status
    if content.startswith("!status add"):
        try:
            _,_,player,condition = message.content.strip().split()
            if player not in status:
                status[player] = []
            
            if condition.lower() in status[player]:
                await message.channel.send(f" {player} already has the **{condition}** condition.")
            else: 
                status[player].append(condition.lower())
                await message.channel.send(f" {player} is now **{condition}**.")
        except ValueError:
            await message.channel.send("to use status add type: !status add [player] [condition]")
    
    # remove status
    elif content.startswith("!status remove"):
        try:
            _,_,player,condition = message.content.strip().split()
            if player not in status:
                await message.channel.send(f"{player} is not afflicted by any condition.")
            
            elif condition.lower() in status[player]:
                status[player].remove(condition.lower())
                if not status[player]:
                    del status[player] 
                await message.channel.send(f" {player} is no longer afflicted by **{condition}**.")
            else:
                if not status[player]:
                    del status[player] 
                await message.channel.send(f" {player} is not afflicted by **{condition}**.")

        except ValueError:
            await message.channel.send("to use status remove type: !status remove [player] [condition]")
    
    # show all satuses
    elif content.startswith("!status show"):
        if not status:
            await message.channel.send("no one is afflicted with any condition")
        else:
            msg = "** Status Tracker:**\n"
            for player, conditions in status.items():
                msg += f"• {player}: {', '.join(conditions)}\n"
            await message.channel.send(msg)
    
    #status clear
    elif content.startswith("!status clear"):
        status.clear()
        await message.channel.send("All status conditions have been cleared.")


        

   
    ## Concentration checker -------------------------------------------------------------------------------
    # setting the concentration
    if content.startswith("!con set"):
        # needs to attach a con spell to a player
        try:
            _,_, player, spell = message.content.strip().split()
            if player in concentration:
                await message.channel.send(f"{player} is already concentrating on a spell, if you would like to break this concentration for a new spell use !con break first.")
            else: 
                await message.channel.send(f"{player} is now concentrating on {spell}")
                concentration[player]= spell
        except ValueError:
            await message.channel.send("please input the spell, player such that !con [player] [spell] ") 

    # breaking the concentraion

    elif content.startswith("!con break"):
        try:
            _,_, player = message.content.strip().split()
            if player in concentration:
                await message.channel.send(f"{player} is no longer concentrating on {concentration[player]}")
                del concentration[player]
            else: 
                await message.channel.send(f"{player} is not concentrating on a spell")
        except ValueError:
            await message.channel.send("to use con break type (!con break [player])") 
    
    #showing concentration

    elif content.startswith("!con show"):
        if not concentration:
            await message.channel.send("No one is currently concentrating on a spell.")
        else:
            msg = "** Concentration Tracker:**\n"
            for player, spell in concentration.items():
                msg += f"• {player} → {spell}\n"

            await message.channel.send(msg)
    
    elif content.startswith("!con clear"):
        concentration.clear()
        await message.channel.send ("All concentrations have been cleared")

    # roll for stats ---------------------------------------------------------------------------------------------
    
    elif content.startswith('!stats'):
        try:
            _, name, race = message.content.strip().split()
            stat_names = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
            msg = f"**{name},({race}) Stat Rolls (4d6 drop lowest)**\n\n"

            for i in range(6):
                rolls = [random.randint(1, 6) for _ in range(4)]
                rolls_sorted = sorted(rolls)
                total = sum(rolls_sorted[1:]) 
                dropped = rolls_sorted[0]

                msg += f"{stat_names[i]}: {total}  (rolled {rolls}, dropped {dropped})\n"

            await message.channel.send(msg)
        except ValueError:
            await message.channel.send("to use stat roller type: !stats (character name) (character race) ")


    # Roll command, e.g., !roll d6 or !roll d20 ------------------------------------------------------------------------
    elif content.startswith('!roll'):
        match = re.match(r'!roll (\d*)d(\d+)', content)
        if match:
            num_dice = int(match.group(1)) if match.group(1) else 1
            sides = int(match.group(2))
            if num_dice <= 100:
                rolls = [random.randint(1, sides) for _ in range(num_dice)]
                total = sum(rolls)
                await message.channel.send(f'{message.author} rolled {num_dice}d{sides}  That rolls: {rolls} → Total: {total}')
            else:
                await message.channel.send(" Too many dice (max 100).")
        else:
            await message.channel.send("Usage: `!roll 2d6`, `!roll d20`, etc.")
# Run the bot
if TOKEN is None:
    print("ERROR: Bot token not found. Check your .env file")
bot.run(TOKEN)