import telebot

TOKEN = '8693813296:AAHWde9efzDl3cCVaV5bULkibSi2l-N9n0I'
ADMIN_ID = 'ያንተ_አይዲ' # አድሚኑ ደረሰኙን የሚያይበት ቦታ
bot = telebot.TeleBot(TOKEN)

# ኮርሱ የያዘው የፒዲኤፍ ፋይል መንገድ
PDF_PATH = 'Import_Export_Course.pdf' 

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('ኮርሱን ይግዙ')
    bot.reply_to(message, "እንኳን ወደ ኢምፖርት ኤክስፖርት አካዳሚ በደህና መጡ! 🌍\nኮርሱን ለመግዛት ከታች ያለውን ይጫኑ።", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'ኮርሱን ይግዙ')
def buy_course(message):
    bot.reply_to(message, "የክፍያ መረጃ፡\nባንክ፡ የኢትዮጵያ ንግድ ባንክ\nአካውንት፡ 1000XXXXXXX\n\nከከፈሉ በኋላ ደረሰኙን (Receipt) ፎቶ አንስተው ይላኩልን።")

@bot.message_handler(content_types=['photo'])
def handle_receipt(message):
    # ደረሰኙን ለአድሚን መላክ
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    bot.reply_to(message, "ደረሰኙ ደርሶናል! አድሚኑ ሲያረጋግጥ ፒዲኤፉ ይላክልዎታል።")

@bot.message_handler(commands=['send_course'])
def send_course(message):
    # ይህንን ትዕዛዝ አድሚኑ ብቻ ነው የሚጠቀመው
    if str(message.chat.id) == ADMIN_ID:
        # ለተጠቃሚው PDF መላክ (ይህንን logic በ Database ማሳደግ ትችላለህ)
        with open(PDF_PATH, 'rb') as f:
            bot.send_document(message.chat.id, f) # ለሙከራ አድሚኑ ላይ ይልካል
    else:
        bot.reply_to(message, "ይህ ትዕዛዝ ለአድሚን ብቻ ነው!")

bot.polling()
