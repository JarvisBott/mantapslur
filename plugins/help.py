#Developer : Hiruwa

from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"🍁AdhanMod🍁\n\nCurrently Only supports Youtube Single  (No playlist) Just Send Youtube Url"
    await message.reply_text(helptxt)
