import discord
import random
import re


#--------------------------------------------------------------------------------------------------------------------
"""
this is my dnd discord bot just sort of a project i chose to partake in to challenge myself.

"""
# Intents setup
intents = discord.Intents.default()
intents.message_content = True

# Bot setup
bot = discord.Client(intents=intents)

# Libraries-----------------------------------------------------------------------------------------------------------
# initiative list S
initiative_list =[]
#initiative turn counter
round_count=1


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
    !npc : to generate a rndom name \n 
    !init (arg): \n
    \t\t !init (add) [name] [roll]; to add  someone to the initiative tracker\n
    \t\t !init (show); to show the initiative turn order\n
    \t\t !init (next); to move to signify a turn end and move to the next turn in the turn order\n
    \t\t !init (end); to reset the initiative list and end combat\n

"""

# main----------------------------------------------------------------------------------------------------------------
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):

    # This is here just incase so that the bot doesn't respond to itself
    if message.author == bot.user:
        return
    
    # Seperates the content of the message from the parent and formats it
    content = message.content.strip()

    
    # HELP!!!!!!!!!!!!!! ----------
    if message.content.startswith("!help"):
        await message.channel.send(help)

    # Easter eggs!!! ----------
    if message.content.startswith("!hello there") or message.content.startswith("!hellothere") :
        await message.channel.send("General Kenobi")
        return
    
    # NPC name generator ----------
    if message.content.startswith("!npc"):
        first = random.choice(first_names)
        last = random.choice(last_names)
        await message.channel.send(f" *{first} {last}.*")
        return
    
    # initiative roller and tracker ----------
    ## ADD to initiative 
    if message.content.startswith("!init add"):
        try:
            _, _, name, roll = message.content.strip().split()
            roll = int(roll)
            new_entry = {"name": name, "roll": roll}

            # Store current active player (at front of list)
            current = initiative_list[0] if initiative_list else None

            # Add new entry and sort
            initiative_list.append(new_entry)
            initiative_list.sort(key=lambda x: x['roll'], reverse=True)

            # Rotate list back so current player is still at front
            if current:
                while initiative_list[0] != current:
                    initiative_list.append(initiative_list.pop(0))

            await message.channel.send(f"Added **{name}** with initiative **{roll}** to the turn order.")
        except ValueError:
            await message.channel.send("Usage: `!init add [name] [roll]` (e.g. `!init add Bob 13`)")
        return  
        

    
    ## SHOW the initiative order
    if message.content.startswith("!init show"):
        global round_count
        if not initiative_list:
            await message.channel.send("Initiative order empty. :(")
            return
        msg = f"**Initiative Order (Round {round_count}):**\n"
        for i, entry in enumerate(initiative_list):
            marker = "➡️ " if i == 0 else ""
            msg += f"{marker}{entry['name']} (init {entry['roll']})\n"
        await message.channel.send(msg)
        return

    
    ## NEXT turn in the order
    if message.content.startswith("!init next"):
        if not initiative_list:
            await message.channel.send("No one is in the initiative tracker.")
            return

        original = initiative_list[0]  # remember whose turn it was
        skipped_delayed = []

        while True:
            current = initiative_list.pop(0)  
            if current.get("delayed", False):
                current["delayed"] = False
                initiative_list.append(current)  
                skipped_delayed.append(current["name"])
            else:
                initiative_list.append(current)  
                break  

            # If we've gone full circle, stop
            if initiative_list[0] == original:
                break

        await message.channel.send(f"It's now **{initiative_list[0]['name']}**'s turn!")

        if skipped_delayed:
            await message.channel.send(
                f"Skipped delayed turn(s) for: {', '.join(skipped_delayed)}"
            )

        # Display updated initiative
        msg = "**Updated Initiative Order:**\n"
        for i, entry in enumerate(initiative_list):
            marker = "➡️ " if i == 0 else ""
            delayed_note = " (delayed)" if entry.get("delayed") else ""
            msg += f"{marker}{entry['name']} (init {entry['roll']}){delayed_note}\n"

        await message.channel.send(msg)
        return

        
    ## END initiative
    if message.content.startswith("!init end"):
        initiative_list.clear()
        round_count = 1
        await message.channel.send("Initiative has ended. Combat is now finished.")
        return


    # Roll command, e.g., !roll d6 or !roll d20 ----------
    if message.content.startswith('!roll'):
        match = re.match(r'!roll (\d*)d(\d+)', message.content)
        if match:
            num_dice = int(match.group(1)) if match.group(1) else 1
            sides = int(match.group(2))
            if num_dice <= 100:
                rolls = [random.randint(1, sides) for _ in range(num_dice)]
                total = sum(rolls)
                await message.channel.send(f'{message.author} rolled {num_dice}d{sides} 🎲 That rolls: {rolls} → Total: {total}')
            else:
                await message.channel.send("🚫 Too many dice (max 100).")
        else:
            await message.channel.send("Usage: `!roll 2d6`, `!roll d20`, etc.")
# Run the bot
bot.run('MTM3NDk2Mjg3Nzk5MTA5NjM2MQ.GF40Cb.NCHi2Pg2_DpAh9Eg2RvE8qD7KkRfeIoEpzooAc')