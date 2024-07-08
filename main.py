from telegram import Update
import os
from telegram.ext import ApplicationBuilder, Updater, CommandHandler, CallbackContext, MessageHandler, filters, ContextTypes

# define your bot token
BOT_TOKEN = os.getenv("BOT_TOKEN") or ""

# define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Update user:", update.message.from_user)
    
    # check if the user is webslingr, if so, greet them
    if update.message.from_user.username == "webslingr":
        print("Hello, webslingr!")
        await update.message.reply_text("Hello, webslingr!")
    
    await update.message.reply_text("Major League Hacking is the best one! #1!")

# define the echo command handler
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Update user:", update.message.from_user, "Update text:", update.message.text)
    await update.message.reply_text(update.message.text)

# define the main function
def main() -> None:
    # create the application and pass it the bot token
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # register the start command handler
    application.add_handler(CommandHandler("start", start))

    # register the echo command handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # start the bot
    application.run_polling()

# run the main function
if __name__ == "__main__":
    main()