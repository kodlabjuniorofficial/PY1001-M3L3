from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from assistant import Assistant

bot_brain = Assistant("ZeyBot")

# /start, /durum, /sarj handlers...

# 1. GÖREV: 'say_info' asenkron fonksiyonunu yazın.
async def say_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)
    
    if query:
        # Asistana sora (result bir sözlük dönecek)
        result = bot_brain.search_info(query)
        
        if result["status"] == "ok":
            # 2. GÖREV: Eğer görsel (result["image"]) varsa 'reply_photo' kullanın.
            # Yoksa sadece 'reply_text' ile metni gönderin.
            pass
        else:
            await update.message.reply_text(result["message"])
    else:
        await update.message.reply_text("❓ Neyi merak ediyorsun? Örn: /nedir Mars")

if __name__ == '__main__':
    TOKEN = "TOKEN_BURAYA"
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Handlers...
    app.add_handler(CommandHandler('start', start))
    # 3. GÖREV: 'nedir' komutunu ekleyin
    # ...
    app.run_polling()