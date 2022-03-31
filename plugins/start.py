#Developer: Hiruwa

from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel YouTube", url="https://youtube.com/channel/UCsgZRLFYG9_uDZBNunAMQNg")],
        [InlineKeyboardButton(
            "Report Bugs 😪", url="https://t.me/+pbCJCIFKOmI0NDc1")]
    ])
    welcomed = f"Welcome<b>{message.from_user.first_name}</b>\n /help 🍁AdhanMod🍁\n\nHey <b>{message.from_user.first_name}</b>\n/help for More info..🤭"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
