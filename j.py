import asyncio
import json
#===================================================================#
import time
import os
import asyncio
import random
from pyromod.helpers import ikb
from pyrogram import Client, filters
#==================================================
# ====================#
api_id = 4109627
api_hash = '5874fe255bec03272faaa41ac22e55dc'
me = 1223702732
biochi = True
chats = {}

app = Client("m5", api_id, api_hash)
last = time.time()
#========================================================================#
async def bla(sec):
    await asyncio.sleep(sec)
#============================================================================#
@app.on_message(filters.command(['kir'], ['/','!','+','-','']))
async def kirekhar(client, message):
    print('kire khar')
    for i in range(int(message.text.split('_')[1])):
        await client.send_message(message.chat.id, message.text.split('kir')[1].split('_')[0] , reply_to_message_id=message.reply_to_message.message_id)
    await app.delete_messages(message.chat.id, message.message_id)
@app.on_message(filters.me & filters.command(['dell'], ['/','!','+','-','','*','~','#','$']))
async def delllll(client, message):
    if message.reply_to_message:
        await client.edit_message_text(message.chat.id, message.message_id, '**deleting ...**')
        await app.delete_user_history(message.chat.id, message.reply_to_message.from_user.id)
        await client.send_message(message.chat.id, '**done**')

#-----------------------
@app.on_message(filters.reply & filters.regex("^([Ii]d)$")) #get id by replying on messages
async def id(client, message):
    if message.from_user.id == me:
        ids = message.reply_to_message.from_user.id
        await client.edit_message_text(message.chat.id, message.message_id, f'`{ids}`')
#=====================================================================================================================================#
@app.on_message(filters.me & filters.regex("^\/ping$"))
async def ping(client, message):
    await app.edit_message_text(message.chat.id, message.message_id, "┈┅┅━━━━✦━━━━┅┅┈\n             Im Online\n┈┅┅━━━━✦━━━━┅┅┈")
#=====================================================================================================================================#
@app.on_message(filters.command(['setprofile', 'setprof'],['/','!','+','-','','*','~','#','$'])) #set telegram profile
async def setprofilephoto(client, message):
       if message.from_user.id == me:
        try:
            gif = message.reply_to_message.animation if message.reply_to_message.video else None
            photo = message.reply_to_message.photo if message.reply_to_message.photo else None
            if photo:
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس .**')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس ..**')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس ...**')
                await message.reply_to_message.download('profile.png')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس ..**')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود عکس .**')
                await client.set_profile_photo(photo = 'downloads/profile.png')
                os.remove('downloads/profile.png')
                await client.edit_message_text(message.chat.id, message.message_id, '**پروفایل با موفقیت تنظیم شد 👁**')
                await bla(10)
                await app.delete_messages(message.chat.id, message.message_id)

            if gif: #it does not working right now :(
                await client.edit_message_text(message.chat.id, message.message_id, '**درحال دانلود گیف .**')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود گیف ..**')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود گیف ...**')
                await message.reply_to_message.download('profile.mp4')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود گیف ..**')
                await client.edit_message_text(message.chat.id, message.message_id, '**در حال دانلود گیف .**')
                await client.set_profile_photo(video = 'downloads/profile.mp4')
                os.remove('downloads/profile.mp4')
                await client.edit_message_text(message.chat.id, message.message_id, '**پروفایل با موفقیت تنظیم شد 👁**')
        except:
            pass
#=======================================================================================================================#
@app.on_message(filters.command(['startbio', 'bio'],['/','!','+','-','','*','~','#','$'])) #Change Biography every 60 seconds !
async def strtbio(client, message):
    global biochi
    if message.from_user.id == me:
        try:
            emojies = ['🌵','🌱','🌾','🪐','☄️','✨','🔥','💥','🌪','🌟','🌎','🌙','🧘🏽‍♂️','🎧','🎤','🎸','🎮','🎯','♟','🎙','💣','⚔️','🗡','🔮','📿','💊','🧬','🖤']
            await app.edit_message_text(message.chat.id, message.message_id, '**تغییر خودکار بیو روشن شد✅**')
            while 1 == 1:
                rand = int(random.randint(0, 28))
                emo = emojies[rand]
                if biochi == False:
                    break
                await app.update_profile(first_name = 'Alion' ,bio=f"تاریخ یه فی البداهه اس{emo}")
                await bla(60)
        except:
            pass
#=======================================================================================================================#
@app.on_message(filters.command(['stopbio', 'biooff'],['/','!','+','-','','*','~','#','$'])) #make off biography changer
async def stpbio(client, message):
    try:
        global biochi
        if message.from_user.id == me:
            biochi == False
            await app.edit_message_text(message.chat.id, message.message_id, '**تغییر خودکار بیو خاموش شد❗️**')
    except:
        pass
#=======================================================================================================================#
@app.on_message(filters.me & filters.command(['tst', 'test'],['/','!','+','-','','*','~','#','$'])) #for test my codes !
async def test(client, message):
    try:
        print(message)
        await client.edit_message_text(message.chat.id, message.message_id, message.reply_to_message.voice.file_id)
    except Exception as qwes:
        print(qwes)
#=======================================================================================================================#
#=======================================================================================================================#
@app.on_message(filters.me & filters.command(['download', 'save'],['/','!','+','-','','*','~','#','$'])) #Download files from telegram and save in local directory
async def downloader(client, message):
    try:
        video = message.reply_to_message.video if message.reply_to_message.video else None
        photo = message.reply_to_message.photo if message.reply_to_message.photo else None
        music = message.reply_to_message.audio if message.reply_to_message.audio else None
        if video:
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await message.reply_to_message.download(f'{message.message_id}.mp4')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloaded !**')
            await bla(10)
            await app.delete_messages(message.chat.id, message.message_id)
        elif photo:
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await message.reply_to_message.download(f'{message.message_id}.png')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloaded !**')
            await bla(8)
            await app.delete_messages(message.chat.id, message.message_id)
        elif music:
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading .**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ..**')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloading ...**')
            await message.reply_to_message.download(f'{message.message_id}.mp3')
            await client.edit_message_text(message.chat.id, message.message_id, '**Downloaded !**')
            await bla(8)
            await app.delete_messages(message.chat.id, message.message_id)
        else:
            whattosave = message.reply_to_message
            await whattosave.forward(me)
            await app.delete_messages(message.chat.id, message.message_id)
    except:
        pass
#==============================================================================================================================#
@app.on_message(filters.me & filters.command(['auto', 'delkhar', 'khar', 'remove', 'addvoice', 'answers'],['/','!','+','-','','*','~','#','$']))
async def databasing(client, message):
    try:
        with open('users.json', 'r', encoding='utf8') as jsonfile:
            data = json.load(jsonfile)
        if 'answers' in message.text:
            text = 'لیست جواب خودکار : \n'
            for id in data['autoanswer']:
                T = data["autoanswer"][id]
                text += f'[{id}](tg://user?id={id}) : {T} \n'
            await client.send_message(message.chat.id, text, reply_to_message_id=message.message_id)

        if 'auto' in message.text:
            answer = message.text.split('auto')[1]
            for i in data["autoanswer"]:
                if i == str(message.reply_to_message.from_user.id):
                    data["autoanswer"][str(message.reply_to_message.from_user.id)] =answer

            data['autoanswer'][str(message.reply_to_message.from_user.id)] = answer
            with open('users.json', 'w', encoding='utf8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            await client.edit_message_text(message.chat.id, message.message_id, f'''
            **Auto Answer Changed to : ** __{answer}__''')


        if 'khar' in message.text and 'delkhar' not in message.text:
            for i in data["blocklist"]:
                if i == str(message.reply_to_message.from_user.id):
                    await app.delete_messages(message.chat.id, message.message_id)
                    return
            data['blocklist'].append(str(message.reply_to_message.from_user.id))
            with open('users.json', 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            await client.edit_message_text(message.chat.id, message.message_id, '**دیگه به شما جواب داده نمیشه :)**')


        if 'delkhar' in message.text:
            uid = message.reply_to_message.from_user.id
            for i in data["blocklist"]:
                if i == str(uid):
                    data["blocklist"].remove(str(i))
            with open('users.json', 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            await client.edit_message_text(message.chat.id, message.message_id, "**حساب شدی بی آبرو**")

        if 'remove' in message.text:
            uid = message.reply_to_message.from_user.id
            if str(uid) in data["autoanswer"]:
                data["autoanswer"].pop(str(uid))
            with open('users.json', 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            await app.delete_messages(message.chat.id, message.message_id)
        if 'addvoice' in message.text:
            fid = message.reply_to_message.message_id
            texts = message.text.split('addvoice ')[1]
            for i in texts.split(' '):
                data["voice"][i] = fid
            with open('users.json', 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            await client.edit_message_text(message.chat.id, message.message_id, "**ست شد !**")

    except Exception as r:
        print(r)
@app.on_message(filters.channel)
async def jokegir(client, message):
    if message.chat.username == 'alion_self_jokegir':
        try:
            with open('users.json', 'r', encoding='utf-8') as jsonfile:
                data = json.load(jsonfile)
            jokessss = message.text
            if '@' in message.text:
                bedoneat = message.text.split('@')[1].split(' ')[0]
                jokessss = jokessss.replace(bedoneat, '').replace('@', '')
            if '#' in message.text:
                bedonehash = message.text.split('#')[1].split(' ')[0]
                jokessss = jokessss.replace(bedonehash, '').replace('#', '')

            data['jokes'].append(jokessss)
            with open('users.json', 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=4)

        except Exception as R:
            print(R)
@app.on_message(filters.me & filters.command(['joke'],['/','+','!','-','*','#', '$', '']))
async def jokebde(client, message):
    try:
        with open('users.json', 'r', encoding='utf-8') as jsonfile:
            data = json.loads(jsonfile.read())
        jokesh = random.choice(data['jokes'])
        await client.send_message(message.chat.id, jokesh, reply_to_message_id=message.message_id)
        await app.delete_messages(message.chat.id, message.message_id)
    except Exception as r:
        print(r)



#===============================================================================================================================#
@app.on_message(filters.mentioned)
async def mentionedme(client, message):
    global last
    try:
        rp = message.reply_to_message
        if rp:
            if rp.from_user.id == me:

                return
        if time.time() - last < 10:
            return
        default = "حق با توعه"
        print('hey')
        with open('users.json', 'r', encoding='utf-8') as jsonfile:
            data = json.loads(jsonfile.read())
        if str(message.from_user.id) in data['blocklist']:
            print('blocked user !')
            return
        for userid in data['autoanswer']:
            print('auto answering ...')
            if int(userid) == message.from_user.id:
                print('it exists...')
                print('getting from db')
                await client.send_message(message.chat.id, data['autoanswer'][str(userid)], reply_to_message_id=message.message_id)
                await bla(20)
                return
        await client.send_message(message.chat.id, default, reply_to_message_id=message.message_id)
        await bla(20)
        last = time.time()
    except Exception as t:
        print(t)


#===============================================================================================================================#
@app.on_message(filters.me & filters.command(['stick', 'photo', 'voice', 'audio'],['/','!','+','-','','*','~','#','$'])) #file converter :)
async def convertermessage(client, message):
    try:
        rp = message.reply_to_message
        if rp.sticker:
            print('got')
            await rp.download('files1.png')
            await client.send_photo(message.chat.id, 'downloads/files1.png', reply_to_message_id = rp.message_id)
            await app.delete_messages(message.chat.id, message.message_id)
            os.remove('downloads/files1.png')
        if rp.photo:
            print('got')
            await rp.download('files2.webp')
            print('downloaded')
            await client.send_sticker(message.chat.id, 'downloads/files2.webp', reply_to_message_id = rp.message_id)
            print('sent')
            await app.delete_messages(message.chat.id, message.message_id)
            os.remove('downloads/files2.webp')
        if rp.voice:
            print('got')
            await rp.download('files2.mp3')
            print('downloaded')
            await client.send_audio(message.chat.id, 'downloads/files2.mp3', reply_to_message_id = rp.message_id)
            print('sent')
            await app.delete_messages(message.chat.id, message.message_id)
            os.remove('downloads/files2.mp3')
        if rp.audio:
            print('got')
            await rp.download('files2.ogg')
            print('downloaded')
            await client.send_voice(message.chat.id, 'downloads/files2.ogg', reply_to_message_id = rp.message_id)
            print('sent')
            await app.delete_messages(message.chat.id, message.message_id)
            os.remove('downloads/files2.ogg')
    except:
        pass
#=============================================================================================================================#
@app.on_message(filters.me & filters.command(['load'], ['/','!','+','-','','*','~','#','$']))
async def loader(client, message):
    try:
        freete = '|'
        text111 = '███████████████████|'
        for i in text111:
            freete += i
            await client.edit_message_text(message.chat.id, message.message_id, freete)
        await client.edit_message_text(message.chat.id, message.message_id, 'Completely Loaded !')
    except:
        pass
#==============================================================================================================================#
@app.on_message(filters.text & filters.group)
async def youme(client, message):
    global last
    try:
        callme = ['alion', 'Alion', 'الیون', 'علیون', 'علی یون', 'الی یون', 'علیکون']
        sorena = ['sorena','Sorena', 'سورنا', 'علی سورنا', 'ناخدا جلال', 'nakohoda jelal','Nakhoda Jelal','پیچک','pichak']
        sorenaj = '**بریم سورنا گوش بدیم** 🦌🖤'
        putak = ['putak','Putak', 'پوتک','پیامبر','خودکشی','khodkoshi','changar', 'چنگار']
        putakj = '**بریم پوتک گوش بدیم** 🖤🤘🏿'
        pishro = ['pishro','Pishro', 'پیشرو', 'parvaz', 'rail','ریل ','قیلی ویلی', 'اثر منفی', 'چاقال']
        pishroj = '**بریم پیشرو گوش بدیم** 🤘🏿👁🙏🏾✍🏾🙇🏾‍♂️🌘🌪'
        if message.from_user.id == me:
            if message.text == '!re':   #idk really for what :(
                await message.reply_text('**ربات با موفقیت ریستارت شد ☄️**')
                await app.restart()
        else:
            if time.time()-last < 20:
                return
            for i in callme:
                if i in message.text:
                    filsss = ['AwACAgQAAxkBAALkxmCUN_A0TzUR_eY7MlAAAUw-7-67TQAC3AoAAjt1qFCInVENkfQeZh4E',
                              'AwACAgQAAxkBAALkx2CUN_V6iChaki2eNAulEbM75ODVAALdCgACO3WoUMoUY08q6VseHgQ',
                              'AwACAgQAAxkBAALkyGCUN_quVBS9oW_CbBffcA6KNMy-AALeCgACO3WoUHVnK0yMyiFQHgQ',
                              'AwACAgQAAxkBAALkwGCUOAEGlkJ1pzEYDSjSeycNkuuBAALBCgACO3WoUGiqSC5wjSvEHgQ',
                              'AwACAgQAAxkBAALk2mCUPr0c5HKTrTQiFAxLXovUuWiAAALpCgACO3WoULTD6DEm-HNNHgQ',
                              'AwACAgQAAxkBAALk22CUPsDt19IxvVP-ug3QYip008rDAALqCgACO3WoUMeC3Xii8U45HgQ',
                              'AwACAgQAAxkBAALk4mCUPsaRgGFypZMWDQZGTAFs_wz-AALsCgACO3WoUH1bISVjlHvcHgQ',
                              'AwACAgQAAxkBAALk42CUPsskGIe3ExklrHIJ3FMjQ8deAALtCgACO3WoUNAvuN28J4SXHgQ',
                              ]
                    adad = random.choice(filsss)
                    last = time.time()
                    try:
                        await client.send_voice(message.chat.id, voice = adad, reply_to_message_id=message.message_id)
                    except Exception as chera:
                        print(chera)
                    await bla(10)
            for i in sorena:
                if i in message.text:
                    last = time.time()
                    await message.reply_text(sorenaj)
                    await bla(20)
            for i in putak:
                if i in message.text:
                    last = time.time()
                    await message.reply_text(putakj)
                    await bla(20)
            for i in pishro:
                if i in message.text:
                    last = time.time()
                    await message.reply_text(pishroj)
                    await bla(20)
    except:
        pass


@app.on_message(filters.group)
async def post251saz(client, message):
    try:
        print("group")
        emojies = '🤣🍎💀🥶🍆😈😔🤘🏿🥳🥶✊🏾✌🏾👀🐸🌵🌱🌵👀💁🏽‍♂💆🏾‍♂🐊🐘🦧🦍🐫🦒🦘🐃🐂🐄🐐🦙🐑🐏🐖🐩🦃🐉🍀☘🎄🌲🦔🐿🦨🪐☄️⚡️✨☀🌟🌎🌙🌗🍎🥖🍣🥃🥎🛹🏌🏾‍♀🎤🎯🎮💣🧨🪓🔪⛓⚙🛠🔫⛏🩸💉🔑🎁'
        nuemo = len(emojies)
        rand = random.randint(0, int(nuemo))
        whi12 = emojies[rand]
        if message.forward_from_chat.username == 'ali_sarsakht':
            print(message)
            if message.forward_signature == 'Alion':
                print('yesssssssssss its alion')
            await client.send_message(message.chat.id,f'**پست شما خورده شد **{whi12}', reply_to_message_id=message.message_id)
        elif message.forward_from_chat.username == 'pgming':
            if message.forward_signature == 'Alireza':
                print('yesssssssssss its alireza')
                print(message)
                await client.send_message(-1001444467770,f'**پست شما خورده شد **{whi12}', reply_to_message_id=message.message_id)
        elif message.forward_from_chat.username == 'nigga57':
            if message.forward_signature == 'Amir':
                print('yesssssssssss its alion')
            print(message)
            await client.send_message(-1001313696110, 'hey i know that', reply_to_message_id=message.message_id)
    except Exception as xzc:
        print(xzc)




app.run()

