from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup , ReplyKeyboardMarkup , KeyboardButton

async def  translate_langs_btn():
    btn = InlineKeyboardMarkup(row_widht=2)

    btn.add(
        InlineKeyboardButton(
            text='ru', callback_data='lang:ru'

        ),
        InlineKeyboardButton(
            text='uz', callback_data='lang:uz'

        ),

        InlineKeyboardButton(
            text='en.', callback_data='lang:en'

        ),



        
    )

    return btn