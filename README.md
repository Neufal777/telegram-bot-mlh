# telegram-bot-mlh

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/telegram-bot-mlh.git
   cd telegram-bot-mlh
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set Up Environment Variables:**
   - Duplicate `.env.example` and rename it to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and replace `BOT_TOKEN` with your actual Telegram bot token obtained from the BotFather.
4. **Activate the Virtual Environment:**
   If you are using a virtual environment (recommended), activate it:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
5. **Run the Bot:**
   ```bash
   python main.py
   ```

## Bot Commands

- `/start` - Starts the bot and greets the user.
- Any other text message will be echoed back to the user.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests.
