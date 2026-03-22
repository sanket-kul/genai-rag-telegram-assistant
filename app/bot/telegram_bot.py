from telegram.ext import ApplicationBuilder, CommandHandler
from app.bot.handlers import ask_handler, help_handler, summarize_handler
from app.config import settings

def run_bot(pipeline):
    app = ApplicationBuilder().token(settings.TELEGRAM_TOKEN).build()

    app.bot_data["pipeline"] = pipeline

    app.add_handler(CommandHandler("ask", ask_handler))
    app.add_handler(CommandHandler("help", help_handler))
    app.add_handler(CommandHandler("summarize", summarize_handler))

    app.run_polling()