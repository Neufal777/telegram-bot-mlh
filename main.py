import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables from the .env file
load_dotenv()

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Get the bot token from environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')


# Define the start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
   
    await update.message.reply_text("Major League Hacking is the best one! #1!")
    await update.message.reply_text(f"Hello, {user.username}")

# Define the echo command handler
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(context)
    user = update.message.from_user
    text = update.message.text
    await update.message.reply_text(text)

# Define the main function
def main() -> None:
    if not BOT_TOKEN:
        print("BOT_TOKEN is not set in the environment variables.")
        return
    
    # Create the application and pass it the bot token
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register the start command handler
    application.add_handler(CommandHandler("start", start))

    # Register the echo command handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Start the bot
    application.run_polling()

# Run the main function
if __name__ == "__main__":
    main()
