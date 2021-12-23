class Script(object):
    START_TXT = """Hello {},

My name is <a href=https://t.me/{}>{}</a>!

<b>I can provide Movies. A Telegram Auto Filter Bot. Its Easy To Use Me :)

Just Add me to Your Group As Admin, Hit The Help Button For More Info..</b>"""

    HELP_TXT = """Hey {}

<b>Here Is The Help For My Commands.</b>"""

    ABOUT_TXT = """<b>➥ My name: {}
➥ Creator: Zaute Km
➥ Library: Pyrogram
➥ Language: Python 𝟹
➥ Data Base: MongoDB
➥ Bot Server: Railway/Heroku
➥ Build Status: v1.0.1 [ Beta ]"""

    SOURCE_TXT = """<b>Source:</b>
IMDb is a Open source project.
Source: <a href='https://github.com/josprojects/tgmoviebot'>GitHub - Click here 👈</a>

<b>DEVS:</b>
- <a href='https://t.me/josprojects'>Jos Projects</a>

<b>SUPPORT GROUP</b>
- <a href='https://t.me/+y53tWFUw6Q43NzE9'>Jos Movie Club</a>"""

    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. IMDb should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - add a filter in chat.
• /filters - list all the filters of a chat.
• /del - delete a specific filter in chat.
• /delall - delete the whole filters in a chat (chat owner only)."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- tgmoviebot support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. IMDb supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/josprojects)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    BUG_TXT = """Help: <b> Here my bug fixing developers </b>
𝗪𝗲 𝗮𝗿𝗲 𝗻𝗼𝘁 𝘀𝗲𝗲𝗻 𝗮𝗻𝘆 𝗯𝘂𝗴 𝘀𝗼 𝗶𝗳 𝘆𝗼𝘂 𝘀𝗲𝗲𝗻 𝗮𝗻𝘆 𝗯𝘂𝗴 𝘀𝗼 𝗽𝗹𝗲𝗮𝘀𝗲 𝗿𝗲𝗽𝗼𝗿𝘁 𝗶𝘁
<a href='https://t.me/Alifmuhammad_tg'>𝗔𝗹𝗶𝗳 𝗺𝘂𝗵𝗮𝗺𝗺𝗲𝗱</a>

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
𝟭. 𝗠𝗮𝗸𝗲 𝗺𝗲 𝘁𝗵𝗲 𝗮𝗱𝗺𝗶𝗻 𝗼𝗳 𝘆𝗼𝘂𝗿 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗶𝗳 𝗶𝘁'𝘀 𝗽𝗿𝗶𝘃𝗮𝘁𝗲.
𝟮. 𝗠𝗮𝗸𝗲 𝘀𝘂𝗿𝗲 𝘁𝗵𝗮𝘁 𝘆𝗼𝘂𝗿 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗱𝗼𝗲𝘀 𝗻𝗼𝘁 𝗰𝗼𝗻𝘁𝗮𝗶𝗻𝘀 𝗰𝗮𝗺𝗿𝗶𝗽𝘀, 𝗽𝗼𝗿𝗻 𝗮𝗻𝗱 𝗳𝗮𝗸𝗲 𝗳𝗶𝗹𝗲𝘀.
𝟯. 𝗙𝗼𝗿𝘄𝗮𝗿𝗱 𝘁𝗵𝗲 𝗹𝗮𝘀𝘁 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝘁𝗼 𝗺𝗲 𝘄𝗶𝘁𝗵 𝗾𝘂𝗼𝘁𝗲𝘀.
 𝗜'𝗹𝗹 𝗮𝗱𝗱 𝗮𝗹𝗹 𝘁𝗵𝗲 𝗳𝗶𝗹𝗲𝘀 𝗶𝗻 𝘁𝗵𝗮𝘁 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝘁𝗼 𝗺𝘆 𝗱𝗯."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- 𝗜𝘁 𝗵𝗲𝗹𝗽𝘀 𝘁𝗼 𝗮𝘃𝗼𝗶𝗱 𝘀𝗽𝗮𝗺𝗺𝗶𝗻𝗴 𝗶𝗻 𝗴𝗿𝘂𝗼𝗽.

<b>NOTE:</b>
1. 𝗢𝗻𝗹𝘆 𝗮𝗱𝗺𝗶𝗻𝘀 𝗰𝗮𝗻 𝗮𝗱𝗱 𝗮 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻.
2. 𝗦𝗲𝗻𝘁 <code>/connect</code> 𝗳𝗼𝗿 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗻𝗴 𝗺𝗲 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗽𝗺

<b>Commands and Usage:</b>
• /connect  - 𝗰𝗼𝗻𝗻𝗲𝗰𝘁 𝗮 𝗽𝗮𝗿𝘁𝗶𝗰𝘂𝗹𝗮𝗿 𝗰𝗵𝗮𝘁 𝘁𝗼 𝘆𝗼𝘂𝗿 𝗣𝗠.
• /disconnect  - 𝗱𝗶𝘀𝗰𝗼𝗻𝗻𝗲𝗰𝘁 𝗳𝗿𝗼𝗺 𝗮 𝗰𝗵𝗮𝘁.
• /connections - 𝗹𝗶𝘀𝘁 𝗼𝗳 𝗮𝗹𝗹 𝘆𝗼𝘂𝗿 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻𝘀."""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

𝘀𝗲𝗹𝗲𝗰𝘁 𝗮 𝗳𝗶𝗹𝘁𝗲𝗿𝘀 𝘁𝘆𝗽𝗲 𝗯𝗲𝗹𝗼𝘄:"""

    PASTE_TXT = """Help: <b>Paste</b>

𝗣𝗮𝘀𝘁𝗲 𝘀𝗼𝗺𝗲 𝘁𝗲𝘅𝘁 𝗼𝗿 𝗱𝗼𝗰𝘂𝗺𝗲𝗻𝘁 𝗼𝗻 𝘀 𝘄𝗲𝗯𝘀𝗶𝘁𝗲!

<b>Commands and Usage:</b>
• /paste [text] - paste the given text on Pasty
• /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
• /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
• /id - get id of a specifed user.
• /info  - get information about a user.
• /json - get the json details of a message.

<b>NOTE:</b>
• 𝗜𝗠𝗗𝗯 𝘀𝗵𝗼𝘂𝗹𝗱 𝗵𝗮𝘃𝗲 𝗮𝗱𝗺𝗶𝗻 𝗽𝗿𝗶𝘃𝗶𝗹𝗹𝗮𝗴𝗲.
• 𝗧𝗵𝗲𝘀𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝘄𝗼𝗿𝗸𝘀 𝗼𝗻 𝗯𝗼𝘁𝗵 𝗽𝗺 𝗮𝗻𝗱 𝗴𝗿𝗼𝘂𝗽.
• 𝗧𝗵𝗲𝘀𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗰𝗮𝗻 𝗯𝗲 𝘂𝘀𝗲𝗱 𝗯𝘆 𝗮𝗻𝘆 𝗴𝗿𝗼𝘂𝗽 𝗺𝗲𝗺𝗯𝗲𝗿."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
• /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
• 𝗜𝗠𝗗𝗯 𝘀𝗵𝗼𝘂𝗹𝗱 𝗵𝗮𝘃𝗲 𝗮𝗱𝗺𝗶𝗻 𝗽𝗿𝗶𝘃𝗶𝗹𝗹𝗮𝗴𝗲.
• 𝗧𝗵𝗲𝘀𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝘄𝗼𝗿𝗸𝘀 𝗼𝗻 𝗯𝗼𝘁𝗵 𝗽𝗺 𝗮𝗻𝗱 𝗴𝗿𝗼𝘂𝗽.
• 𝗧𝗵𝗲𝘀𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗰𝗮𝗻 𝗯𝗲 𝘂𝘀𝗲𝗱 𝗯𝘆 𝗮𝗻𝘆 𝗴𝗿𝗼𝘂𝗽 𝗺𝗲𝗺𝗯𝗲𝗿."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
• /imdb  - get the film information from IMDb source.
• /search  - get the film information from various sources.

<b>NOTE:</b>
• 𝗜𝗠𝗗𝗯 𝘀𝗵𝗼𝘂𝗹𝗱 𝗵𝗮𝘃𝗲 𝗮𝗱𝗺𝗶𝗻 𝗽𝗿𝗶𝘃𝗶𝗹𝗹𝗮𝗴𝗲.
• 𝗧𝗵𝗲𝘀𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝘄𝗼𝗿𝗸𝘀 𝗼𝗻 𝗯𝗼𝘁𝗵 𝗽𝗺 𝗮𝗻𝗱 𝗴𝗿𝗼𝘂𝗽.
• 𝗧𝗵𝗲𝘀𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗰𝗮𝗻 𝗯𝗲 𝘂𝘀𝗲𝗱 𝗯𝘆 𝗮𝗻𝘆 𝗴𝗿𝗼𝘂𝗽 𝗺𝗲𝗺𝗯𝗲𝗿."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
• /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
• /ban - 𝗯𝗮𝗻 𝗮 𝘂𝘀𝗲𝗿.
• /tban - 𝘁𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝗶𝗹𝘆 𝗯𝗮𝗻 𝗮 𝘂𝘀𝗲𝗿. 𝗘𝘅𝗮𝗺𝗽𝗹𝗲 𝘁𝗶𝗺𝗲 𝘃𝗮𝗹𝘂𝗲: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /mute - mute a user.
• /tmute - 𝘁𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝗶𝗹𝘆 𝗺𝘂𝘁𝗲 𝗮 𝘂𝘀𝗲𝗿. 𝗘𝘅𝗽𝗮𝗺𝗽𝗹𝗲 𝘁𝗶𝗺𝗲 𝘃𝗮𝗹𝘂𝗲: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
• /unban or /unmute - 𝘂𝗻𝗺𝘂𝘁𝗲 𝗮 𝘂𝘀𝗲𝗿 𝗮𝗻𝗱 𝘂𝗻𝗯𝗮𝗻 𝗮 𝘂𝘀𝗲𝗿.

<b>Examples:</b>
- 𝗠𝘂𝘁𝗲 𝗮 𝘂𝘀𝗲𝗿 𝗳𝗼𝗿 𝘁𝘄𝗼 𝗵𝗼𝘂𝗿𝘀.
-> <code>/tmute @username 2𝗵</code>

<b>NOTE:</b>
• 𝗜𝗠𝗗𝗯 𝘀𝗵𝗼𝘂𝗹𝗱 𝗵𝗮𝘃𝗲 𝗮𝗱𝗺𝗶𝗻 𝗽𝗿𝗶𝘃𝗶𝗹𝗹𝗮𝗴𝗲.
• 𝗧𝗵𝗲𝘀𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝘄𝗼𝗿𝗸𝘀 𝗼𝗻𝗹𝘆 𝗼𝗻 𝗴𝗿𝗼𝘂𝗽𝘀.
• 𝗧𝗵𝗲𝘀𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗰𝗮𝗻 𝗯𝗲 𝘂𝘀𝗲𝗱 𝗯𝘆 𝗮𝗻𝘆 𝗴𝗿𝗼𝘂𝗽 𝗺𝗲𝗺𝗯𝗲𝗿.."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
𝗧𝗵𝗶𝘀 𝗺𝗼𝗱𝘂𝗹𝗲 𝗼𝗻𝗹𝘆 𝘄𝗼𝗿𝗸𝘀 𝗳𝗼𝗿 𝗺𝘆 𝗮𝗱𝗺𝗶𝗻𝘀

<b>Commands and Usage:</b>
• /logs - to get the rescent errors.
• /stats - to get status of files in db.
• /delete - to delete a specific file from db.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids.
• /leave - to leave from a chat.
• /disable - do disable a chat.
• /ban_users - to ban a user.
• /unban_users - to unban a user.
• /channel - to get list of total connected channels.
• /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>Total Files:</b> <code>{}</code>
<b>Total Users:</b> <code>{}</code>
<b>Total Chats:</b> <code>{}</code>
<b>Used Storage:</b> <code>{}</code> MiB
<b>Free Storage:</b> <code>{}</code> MiB"""

    FORCESUB_TXT = """**♦️ READ THIS INSTRUCTION ♦️**

__🗣 In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately 🙈__

**👇 JOIN THIS CHANNEL & TRY AGAIN 👇**"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝘄𝗶𝘁𝗵 𝗿𝗲𝗾𝘂𝗶𝗿𝗲𝗱 𝗮𝗿𝗴𝘂𝗺𝗲𝗻𝘁𝘀 𝗮𝗻𝗱 𝗶 𝘄𝗶𝗹𝗹 𝗸𝗶𝗰𝗸 𝗺𝗲𝗺𝗯𝗲𝗿𝘀 𝗳𝗿𝗼𝗺 𝗴𝗿𝗼𝘂𝗽.
• /instatus - 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸 𝗰𝘂𝗿𝗿𝗲𝗻𝘁 𝘀𝘁𝗮𝘁𝘂𝘀 𝗼𝗳 𝗰𝗵𝗮𝘁 𝗺𝗲𝗺𝗯𝗲𝗿 𝗳𝗿𝗼𝗺 𝗴𝗿𝗼𝘂𝗽..
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - 𝘁𝗼 𝗸𝗶𝗰𝗸 𝗺𝗲𝗺𝗯𝗲𝗿𝘀 𝘄𝗵𝗼 𝗮𝗿𝗲 𝗼𝗳𝗳𝗹𝗶𝗻𝗲 𝗳𝗼𝗿 𝗺𝗼𝗿𝗲 𝘁𝗵𝗮𝗻 𝗮 𝗺𝗼𝗻𝘁𝗵 𝗮𝗻𝗱 𝗗𝗲𝗹𝗲𝘁𝗲𝗱 𝗔𝗰𝗰𝗼𝘂𝗻𝘁𝘀.
• /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """❗You have to be the group creator to do that."""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """🚮 Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """❗I am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
