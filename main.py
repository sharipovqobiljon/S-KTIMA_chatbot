import telebot
from telebot import types

bot = telebot.TeleBot("7326773284:AAEUcGxC1lR4HnGQc8HNyeFdKgqhyaK-eqw")
ADMIN_ID = '6400925437'
target_user_id = None
kanal="@Samarqand_Kattaqorgon_tuman_IM"

@bot.message_handler(commands=['start'])
def start(message):
    bun = types.InlineKeyboardMarkup(row_width=1)
    bun.add(
        types.InlineKeyboardButton(text="1-kanalga obuna bo'ling", url="https://t.me/Samarqand_Kattaqorgon_tuman_IM"),
        types.InlineKeyboardButton(text="✅Tekshirish", callback_data="|checksub")
    )
    ulanganmi = bot.get_chat_member(kanal, message.from_user.id).status
    print(ulanganmi)
    if ulanganmi == "member" or ulanganmi == "creator" or ulanganmi == "admin" or ulanganmi == "administrator":
        if message.chat.id == int(ADMIN_ID):
            bot.send_message(ADMIN_ID, "👋")
            bot.send_message(ADMIN_ID, "Assalomu Alaykum Admin hizmatga tayyorman.")
        else:
            bot.send_message(message.from_user.id, f"Assalomu Alaykum hurmatli {message.from_user.id}.")
            bot.send_message(message.from_user.id, "Habar yuborishingiz mumkin! \n Javobini shu botdan olasiz.")
    else:

        bot.send_message(message.from_user.id, "Assalomu alykum haba yuborish uchun kanalga qo'shiling.", reply_markup=bun)

@bot.callback_query_handler(func=lambda x:x.data)
def tek(msg:types.Message):
    match msg.data:
        case "|checksub":
                bot.delete_message(msg.message.chat.id, msg.message.id)

                bun=types.InlineKeyboardMarkup(row_width=1)
                bun.add(
                    types.InlineKeyboardButton(text="1-kanalga obuna bo'ling",url="https://t.me/Samarqand_Kattaqorgon_tuman_IM"),
                    types.InlineKeyboardButton(text="✅Tekshirish",callback_data="|checksub")
                )
                ulanganmi=bot.get_chat_member(kanal,msg.from_user.id).status

                if ulanganmi == "member" or ulanganmi=="creator" or ulanganmi=="admin":
                    bot.send_message(msg.from_user.id,f"Assalomu alaykum hurmatli {msg.from_user.username}. Siz habaringizni yuborishingiz mumkin.")
                else:
                            bun=types.InlineKeyboardMarkup(row_width=1)
                            bun.add(
                                        types.InlineKeyboardButton(text="1-kanalga obuna bo'ling",url="https://t.me/Samarqand_Kattaqorgon_tuman_IM"),
                                        types.InlineKeyboardButton(text="✅Tekshirish",callback_data="|checksub")
                            )
                            bot.send_message(msg.from_user.id,"Kanalga qo'shiling",reply_markup=bun)
        case "y":
            bot.send_message(msg.from_user.id,"Marxamat savolingizni yozing...")

@bot.message_handler(func=lambda message: message.chat.id != int(ADMIN_ID))
def forward_to_admin(message):
    user_message = message.text
    user_id = message.chat.id
    bot.send_message(ADMIN_ID, f"Foydalanuvchidan xabar:\n\n{user_message}\n\n ID: <code>{user_id}</code>",parse_mode="html")



@bot.message_handler(func=lambda message: message.chat.id == int(ADMIN_ID) and message.text.isdigit())
def save_user_id(message):
    global target_user_id
    target_user_id = int(message.text)
    bot.send_message(ADMIN_ID, f"Foydalanuvchi ID <code>{target_user_id}</code> saqlandi. Endi barcha xabarlar shu ID ga yuboriladi.",parse_mode="html")


@bot.message_handler(func=lambda message: message.chat.id == int(ADMIN_ID) and target_user_id is not None)
def send_message_to_saved_id(message):
    bot.send_message(target_user_id, f"{message.text}")

bot.polling()
