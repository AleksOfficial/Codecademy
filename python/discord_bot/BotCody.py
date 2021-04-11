import discord
import random
import datetime
import time
import asyncio

try:
    with open("users.txt","r") as users_file:
        users = users_file.readlines()
except FileNotFoundError:
    users = []
f = open("users.txt", "a")

#für role_bot
welcome_channel_id = 706223786604757002

def add_user(user):
    if user not in users:
        f.writelines(user+"\n")
        users.append(user)
        f.flush()

async def add_senior_role():
    while True:
        try:
            guild = discord.utils.get(client.guilds,name ="Bot_Test Server")
            members = guild.members
            senior_role = discord.utils.get(guild.roles, name = "cunts")
            members = [i for i in members if not i.bot and not senior_role in i.roles]
            print(members)
            for i in members:
                if datetime.datetime.now() - i.joined_at > datetime.timedelta(days=3):
                    await i.add_roles(senior_role)
                    print("Added Senior Role to "+ i.name +"#"+ i.discriminator)
            
        except:
            pass
        await asyncio.sleep(60)
    

class MyClient(discord.Client):

    #Einloggen
    async def on_ready(self):
        print('''Reactor Online. Sensors Online.
        \n\n --- All Systems nominal. ---''')
        self.prefix = "!"
        welcome_channel = client.get_channel(welcome_channel_id)
        await welcome_channel.send("Hello there. React to this message to assign your role!")



    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        if message.author == client.user:
            return
        print("Message:" +str(message.content))
        print("Channel: "+ str(message.channel.id))

        if message.content == "SeniorBot Go":
            await add_senior_role()
        
        if message.content.startswith(self.prefix+"play"):
            where = message.content.split(" ")[1]
            channel = discord.utils.get(message.guild.channels, name = where)
            voicechannel = await channel.connect()
            voicechannel.play(discord.FFmpegPCMAudio("your_music_file.mp3"))
            while voicechannel.is_playing():
                time.sleep(5)
            if voicechannel.is_paused():
                pass
            voicechannel.stop()
            voicechannel.pause()
            voicechannel.resume()
            

                
        if message.content.startswith(self.prefix + "wichteln"):
            await message.delete()
            msg = "Bist du wirklich beim Wichteln dabei? falls ja, sende !confirm"
            await message.author.send(msg)

        if message.content.lower() == self.prefix + "confirm" and str(message.channel.type) == "private":
            await message.author.send("Teilnahme bestätigt! viel Spaß beim Wichteln! :) ")
            name = str((message.author)).split(" ")
            add_user(name[0]+ " " + name[1])

        #JEDER USER KANN DAS STARTEN! -> gotta do that differently. 
        '''
        if message.content.lower() == self.prefix +"finish_wichteln":
            receivers = users[:]
            senders = users[:]
            while is self_sender(receivers,senders):
                print("recalculating")
                random.shuffle(receivers)
                random.shuffle(senders)
            for i,u in enumerate(senders):
                user = discord.utils.get(message.guild.members, name=u,)
'''


        if message.content.startswith(self.prefix+"hello bot"):
            await message.channel.send("Hello There ( ͡° ͜ʖ ͡°) ")
            await message.channel.send("What do you want from me? ")
            await message.channel.send("What do you want from me? ", tts = True,delete_after=3.1)
        
        if message.content.startswith(self.prefix+"help"):
            await message.channel.send('''Hello there! I see you need somehelp here: lemme school you in boy.
            
            Send !roulette <bet> to the chat to play roulette. you can bet the following way:
                "vdz" = voisins_du_zero = [0, 2, 3, 4, 7, 12, 15, 18, 19, 21, 22, 25, 26, 28, 29, 32, 35]
                "jeu" = jeu= [0, 3, 12, 15, 26, 32, 35]
                "orp" = orphelins = [1, 6, 9, 14, 17, 20, 31, 34]
                tdc = tiers_du_cylindre=[5, 8, 10, 11, 13, 16, 23, 24, 27, 30, 33, 36]
                black = black = [ 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
                red = red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
                ''')
        
        if message.content.startswith(self.prefix+"stats"):
            messages = await message.channel.history(limit = 50).flatten()
            for i in messages:
                print(i.content)
            counter = 0
            async for m in message.channel.history():
                if m.author == client.user and m.content.startswith("nope. that was wrong m8"):
                    counter+=1
            print(counter)
        
        if message.content.startswith(self.prefix + "onlinemembers"):
            members = client.guilds[0].members
            for i in members:
                if i.status == discord.Status.offline:
                    members.remove(i)
            for i in members:
                print(str(i))
        
        #Roulette:
        if message.content.lower().startswith(self.prefix+"roulette "):
            bid = message.content.split(" ")[1]
            jeu_c = False
            vdz_c = False
            zero_c = False
            orp_c = False
            tdc_c = False
            black_c = False
            red_c = False
            lower_c = False
            higher_c = False
            number = None
            even_c=False
            uneven_c=False
            if bid =="jeu":
                jeu_c=True
            elif bid =="vdz":
                vdz_c=True
            elif bid =="0":
                zero_c=True
            elif bid =="orp":
                orp_c=True
            elif bid =="tdc":
                tdc_c=True
            elif bid =="black":
                black_c=True
            elif bid =="red":
                red_c=True
            elif bid =="lower":
                lower_c=True
            elif bid =="higher":
                higher_c=True
            elif bid =="uneven":
                uneven_c=True
            elif bid == "even":
                even_c=True
            else:
                try:
                    number = int(bid)
                except:
                    message.channel.send("Invalid command. to view how to play this game u cuk, type \"!help\"")
                    

            voisins_du_zero = [0, 2, 3, 4, 7, 12, 15, 18, 19, 21, 22, 25, 26, 28, 29, 32, 35]
            jeu= [0, 3, 12, 15, 26, 32, 35]
            orphelins = [1, 6, 9, 14, 17, 20, 31, 34]
            tiers_du_cylindre=[5, 8, 10, 11, 13, 16, 23, 24, 27, 30, 33, 36]
            black = [ 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
            red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
            zero_w = False
            result = random.randint(0,36)
            message_ = "Congrats {a}, you won! the winning number was {b}! \n You won with: ".format(a=message.author,b=result)
            if result == 0:
                if self.win_check([jeu_c,vdz_c,zero_c]):
                    await message.channel.send(message_+"Zero!")
                    return
            if self.binary_search(jeu,result):
                if self.win_check([jeu_c]):
                    await message.channel.send(message_+"Jeu!")
                    return
            if self.binary_search(voisins_du_zero,result):
                if self.win_check([vdz_c],):
                    await message.channel.send(message_+"Voisins_du_zero!")
                    return
            if self.binary_search(orphelins,result):
                if self.win_check([orp_c]):
                    await message.channel.send(message_+"Orphelins!")
                    return
            if self.binary_search(tiers_du_cylindre,result):
                if self.win_check([tdc_c]):
                    await message.channel.send(message_+"Tiers du Cylindre!")
                    return
            if self.binary_search(black,result):
                if self.win_check([black_c]):
                    await message.channel.send(message_+"black numbers!")
                    return
            if self.binary_search(red,result):
                if self.win_check([red_c]):
                    await message.channel.send(message_+"red numbers!")
                    return 
            if result < 19:
                if self.win_check([lower_c]):
                    await message.channel.send(message_+"lower numbers!")
                    return 
            if result > 17: 
                if self.win_check([higher_c]):
                    await message.channel.send(message_+"higher numbers!")
                    return 
            if result%2:
                if self.win_check([even_c]):
                    await message.channel.send(message_+"even numbers!")
                    return
            if result%2 == 1:
                if self.win_check([uneven_c]):
                    await message.channel.send(message_+"uneven numbers!")
                    return
            if result == number:
                self.win_check([True])
                await message.channel.send(message_+"Hitting the right number!")
                return
            else:
                await message.channel.send("nope. that was wrong m8.\n- Result: {}\n- Your Choice: {}".format(result,bid))
                return

    def win_check(self,some_list):
        for x in some_list:
            if x:
                return True

    def binary_search(self,list,x):
        
        if(len(list)==1):
            if list[0] == x:
                return True 
            else:
                return False
        if len(list)==2:
            if list[0] == x:
                return True
            elif list[1] == x:
                return True
            else:
                return False
        midindex=len(list)//2
        mid_value = list[midindex]
        if x == mid_value:
            return True
        elif x<mid_value:
            return self.binary_search(list[0:midindex],x)
        else:
            return self.binary_search(list[midindex+1:],x)

    async def on_typing(self,channel,user,when):
        print(str()+ "is typing in channel " + str(channel) +" since " +str(when))

    async def on_message_delete(self,message):
        print("Deleted Message: "+ str(message.content))
    
    async def on_message_edit(self,before,after):
        print("Changed message "+ before.content + " to " + after.content)
    
    async def on_reaction_add(self,reaction,user): #cached
        python = discord.utils.get(user.guild.roles, name="python")
        cunts = discord.utils.get(user.guild.roles, name = "cunts")
        if str(reaction.emoji) == "🐍":
            await user.add_roles(python)
        if str(reaction.emoji)=="💩":
            await user.add_roles(cunts)
        
        # await reaction.message.channel.send(str(user)+" reacted to "+ reaction.message.content + " with "+ reaction.emoji)
        # await reaction.message.channel.send("Count: " +str(reaction.count))

    async def on_raw_reaction_add(self,payload): #uncached
        print(str(payload))
        channel = client.get_channel(payload.channel_id)
        user = client.get_user(payload.user_id)
        message = await channel.fetch_message(payload.message_id)
        await channel.send(str(user)+" reacted to "+ message.content + " with "+ payload.emoji)
    
    async def on_member_join(self,member):
        pass
    async def on_member_remove(self,member):
        pass
    async def on_member_update(self,before,after):
        #before and after are not users; they are members
        # print(str(before.joined_at))
        # print(str(before.activities))
        # print(str(before.guild))
        # print(str(before.nick))
        # print(str(before.mobile_status))
        # print(str(before.desktop_status))
        # print(str(before.web_status))
        # print(str(after))
        # print(str(before.roles))
        # roles = discord.utils.get(after.guild.roles, name="zum_verteilen")
        # await after.add_roles(roles)
        pass



        

        
         
client = MyClient()
client.loop.create_task(add_senior_role())

client.run("NzAyNjAwNDgyNTU1ODIyMTgx.XqCxZQ.Y8N6I2ASBu5n4Xihnepp-TvwWno")
