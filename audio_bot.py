import telebot
import schedule
import time
import random

TOKEN = '8693813296:AAHWde9efzDl3cCVaV5bULkibSi2l-N9n0I'
bot = telebot.TeleBot(TOKEN)
USER_ID = 'ያለህን_ቁጥር_አስገባ' # የመነሳሻ መልዕክት የሚደርስበት ሰው አይዲ

quotes = [
    "ጠዋት፡ ዛሬ አዲስ እድል ነው! አንድ ገጽ በማንበብ ጀምረው።",
    "ጠዋት፡ እውቀት ኃይል ነው፤ ዛሬ የሆነ አዲስ ነገር ተማር።",
    "ማታ፡ ዛሬ ምን አሳካህ? ለራስህ ክብር ስጥ።",
    "ማታ፡ እረፍት አድርግ፣ ነገ አዲስ ጀብዱ ይጠብቅሃል!"
]

def send_motivation():
    quote = random.choice(quotes)
    bot.send_message(USER_ID, quote)

# ፕሮግራሙ እንዲሰራ መርሐግብር ማውጣት
schedule.every().day.at("06:00").do(send_motivation)
schedule.every().day.at("21:00").do(send_motivation)

while True:
    schedule.run_pending()
    time.sleep(1)
