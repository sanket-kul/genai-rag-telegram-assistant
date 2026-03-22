from telegram import Update
from telegram.ext import ContextTypes

async def ask_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pipeline = context.application.bot_data["pipeline"]

    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("Please provide a query. Example: /ask What is leave policy?")
        return

    user_id = update.effective_user.id
    response = pipeline.run(user_id, query)

    await update.message.reply_text(response)


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/ask <query> - Ask questions\n"
        "/summarize - Summarize last conversation\n"
        "/help - Show this message"
    )


async def summarize_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pipeline = context.application.bot_data["pipeline"]

    user_id = update.effective_user.id
    summary = pipeline.summarize(user_id)

    await update.message.reply_text(summary)