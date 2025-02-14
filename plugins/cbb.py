#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID, START_MSG, ABOUT_TXT, HELP_TXT
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [ [ InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", callback_data ="source"),
                  InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ" , callback_data = "main")],
                 [InlineKeyboardButton("ᴡᴀᴛᴄʜ sʜᴏʀᴛs ᴠɪᴅᴇᴏs", url = "https://t.me/UnseenRobot/shorts")],
                    [
                        InlineKeyboardButton("ʜᴏᴍᴇ", callback_data = "start"),
                        InlineKeyboardButton(" ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [ InlineKeyboardButton(text="🏖️", callback_data="about"),
                    InlineKeyboardButton(text="🍂", callback_data="about"),
                    InlineKeyboardButton(text="⚠️", callback_data="me"),
                    InlineKeyboardButton(text="💸", callback_data="about"),
                    InlineKeyboardButton(text="🎭", callback_data="about"),
                ],[ InlineKeyboardButton( "ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", callback_data = "main" ),
                    InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ", callback_data = "source")
                ], [ InlineKeyboardButton("ᴡᴀᴛᴄʜ sʜᴏʀᴛs ᴠɪᴅᴇᴏs", url = "http://t.me/UnseenRobot/shorts") ],
                [
                    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data = "about"),
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close")
                ]
            ]
            )
        )
    
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
      
    elif data == "main":
        await query.message.edit_text(
            text=f"<blockquote>ʜᴇʟʟᴏ ᴍʏ ᴜsᴇʀs ᴍʏ ᴜᴘᴅᴀᴛᴇ & ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ɪs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.</blockquote>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/Outlawbots"),
                        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ",url = "t.me/outlawbots")
                    ],
                    [   InlineKeyboardButton("ʜᴏᴍᴇ ", callback_data = "start"), 
                        InlineKeyboardButton("ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "me":
            await query.message.edit(
                text=f"<b>ᴛʜɪs sᴇᴄᴛɪᴏɴ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs & ᴅᴇᴠᴇʟᴏᴘᴇʀ</b>",
                disable_web_page_preview=True,
                reply_markup = InlineKeyboardMarkup(
                    [
                        [  InlineKeyboardButton("ᴅᴇᴠʟᴏᴘᴇʀ",url= "t.me/HateXfree"),
                         InlineKeyboardButton("ᴀᴅᴍɪɴ",url = f'tg://user?id={OWNER_ID}')],
                        [ InlineKeyboardButton("ʜᴏᴍᴇ", callback_data = "start"),
                         InlineKeyboardButton( "ᴄʟᴏsᴇ", callback_data = "close")]
                    ]
                )
        )
    elif data == "source":
        await query.message.edit_text(
            text=f"<b><blockquote>ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ\nɪɴ ᴛᴡᴏ ᴡᴀʏs\n★ <a herf='https://publicearn.com/GitHub'>ɢɪᴛʜᴜʙ</a> \n★ <a herf='https://t.me/+Yy9O2e_eJwU3NjRl'>ᴢɪᴘ ғɪʟᴇ </a></blockquote></b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("ɢɪᴛʜᴜʙ ", url="https://publicearn.com/GitHub"),
                        InlineKeyboardButton("ᴢɪᴘ ғɪʟᴇ",url="https://t.me/+Yy9O2e_eJwU3NjRl")
                    ],
                    [   InlineKeyboardButton("ʜᴏᴍᴇ" , callback_data = "start"),
                        InlineKeyboardButton(" ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
                        )
