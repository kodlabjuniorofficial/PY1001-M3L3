from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from assistant import Assistant

# Modül-2'den miras kalan zeki beyin!
bot_brain = Assistant("ZeyBot")

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(bot_brain.greet())

# /durum
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Beyinden tüm istatistikleri (pil, sayaç) çekiyoruz
    report = bot_brain.show_status()
    await update.message.reply_text(report)

# /sarj
async def charge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = bot_brain.charge()
    await update.message.reply_text(msg)

# /not_al [not içeriği]
async def add_note_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # context.args kullanıcıdan gelen kelimeleri içeren bir listedir
    user_text = " ".join(context.args)
    
    if user_text:
        # Metni beynin add_note metoduna gönderiyoruz
        result = bot_brain.add_note(user_text)
        await update.message.reply_text(result)
    else:
        await update.message.reply_text("❌ Not yazmayı unuttun! Örn: /not_al Sınava çalış")

# /isim_degistir [yeni isim]
async def change_name_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_name = " ".join(context.args)
    if new_name:
        result = bot_brain.set_name(new_name)
        await update.message.reply_text(result)
    else:
        await update.message.reply_text("❌ Lütfen bir isim girin! Örn: /isim_degistir IronBot")

if __name__ == '__main__':
    TOKEN = "BURAYA_SİZİN_TOKEN_GELECEK"
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Komutların Kayıt İşlemleri
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('durum', status))
    app.add_handler(CommandHandler('sarj', charge))
    app.add_handler(CommandHandler('not_al', add_note_cmd))
    app.add_handler(CommandHandler('isim_degistir', change_name_cmd))
    
    print("M3L2 Final Projesi Aktif! 🚀")
    app.run_polling()