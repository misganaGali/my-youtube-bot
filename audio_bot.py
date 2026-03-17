import telebot
from telebot import types

TOKEN = '8693813296:AAHWde9efzDl3cCVaV5bULkibSi2l-N9n0I'
ADMIN_ID = '442843505' # የአድሚን አይዲህ
bot = telebot.TeleBot(TOKEN)

# ዋናው ሜኑ
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('📚 ኮርሱን ይመልከቱ', '💳 ኮርሱን ይግዙ')
    markup.add('📞 እገዛ ያግኙ')
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "እንኳን ወደ ኢምፖርት ኤክስፖርት አካዳሚ በደህና መጡ! 🌍", reply_markup=main_menu())

@bot.message_handler(func=lambda message: message.text == '📚 ኮርሱን ይመልከቱ')
def course_info(message):
    bot.reply_to(message, "ኮርሱ ስለ ኢምፖርት እና ኤክስፖርት ህግጋት፣ የሎጂስቲክስ ስራ እና የንግድ እቅድ አዘገጃጀት ያስተምራል።")

@bot.message_handler(func=lambda message: message.text == '💳 ኮርሱን ይግዙ')
def payment_info(message):
    msg = """
💳 የክፍያ አማራጮች፡

1. ቴሌብር (Telebirr): 09XXXXXXXX
2. ንግድ ባንክ (CBE): 1000XXXXXXXX

ከከፈሉ በኋላ ደረሰኙን ፎቶ አንስተው ይላኩልን።
    """
    bot.reply_to(message, msg)

@bot.message_handler(content_types=['photo'])
def handle_receipt(message):
    # ደረሰኙን ለአድሚን መላክ
    caption = f"🚨 አዲስ ደረሰኝ መጥቷል! \nከ፡ {message.from_user.first_name} (@{message.from_user.username})"
    
    # ለአድሚን ፎቶውን እና የ "አጽድቅ" ቁልፎችን መላክ
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✅ አጽድቅ (PDF ላክ)", callback_data=f"approve_{message.chat.id}"))
    
    bot.send_photo(ADMIN_ID, message.photo[-1].file_id, caption=caption, reply_markup=markup)
    bot.reply_to(message, "ደረሰኝዎ ደርሶናል! አድሚኖቻችን በአጭር ጊዜ ውስጥ ያረጋግጣሉ።")

# አድሚኑ ቁልፉን ሲጫን የሚሰራው
@bot.callback_query_handler(func=lambda call: call.data.startswith('approve'))
def approve_payment(call):
    user_id = call.data.split('_')[1]
    bot.send_message(user_id, "ክፍያዎ ተረጋግጧል! እንኳን ደስ አለዎት። ይኸው የኮርሱ ፒዲኤፍ ፋይል:")
    # እዚህ ጋር ፒዲኤፍ መላክ ትችላለህ
    # bot.send_document(user_id, open('course.pdf', 'rb'))
    bot.answer_callback_query(call.id, "ተላከ!")

bot.polling(none_stop=True)
