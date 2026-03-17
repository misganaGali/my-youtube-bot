import telebot
import yt_dlp
import os

# የቦት ቶከንህ
TOKEN = '8693813296:AAHWde9efzDl3cCVaV5bULkibSi2l-N9n0I'
bot = telebot.TeleBot(TOKEN)

def download_audio_from_youtube(url):
    # yt-dlp ማዋቀር
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'audio_file.%(ext)s',
        'nocheckcertificate': True, # የደህንነት ሰርቲፊኬት እንዳያግደው
    }
    
    # ቪዲዮውን ማውረድ
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return 'audio_file.mp3'

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "ሰላም! የዩቲዩብ ሊንክ ላኩልኝ፣ ወደ MP3 ቀይሬ እልክላችኋለሁ።")

@bot.message_handler(func=lambda message: True)
def process_link(message):
    url = message.text
    if "youtube.com" in url or "youtu.be" in url:
        try:
            bot.reply_to(message, "እባክዎ ይጠብቁ፣ እየቀየርኩ ነው... ⏳")
            audio_path = download_audio_from_youtube(url)
            
            # ፋይሉን ወደ ቴሌግራም መላክ
            with open(audio_path, 'rb') as f:
                bot.send_audio(message.chat.id, f)
            
            # ፋይሉን መሰረዝ
            os.remove(audio_path)
        except Exception as e:
            bot.reply_to(message, f"ስህተት ተፈጥሯል፡ {str(e)}")
    else:
        bot.reply_to(message, "እባክዎ ትክክለኛ የዩቲዩብ ሊንክ ይላኩ።")

print("ቦቱ እየሰራ ነው...")
bot.polling(none_stop=True)