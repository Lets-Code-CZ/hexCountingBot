Simple bot for *Hexadecimal* counting activity

## Setup
1. Clone repository
2. Setup and activate virtual enviroment
```bash
python -m venv ./venv
./venv/Scripts/activate.bat
```
3. Install requirements
```bash
pip install -r requirements.txt
```
4. Make .env file in the root direcotry a provide these values
```bash
TOKEN = <your_api_secret>
ALLOWED_CHANNEL_ID = <guild_text_channel_id>
```
5. Run the bot
```bash
python main.py
```
