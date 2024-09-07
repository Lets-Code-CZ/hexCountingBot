# 🤖 hex_count Discord bot na Let's Code
Velice jednoduchý Discord bot napsaný v Pythonu pro naší počítací místnost na Discord serveru. Bot kontroluje, zda číslo navazuje na předchozí hexadecimální číslo v pořadí. Pokud někdo pošle špatnou odpověď, bot ho opraví a pokračuje se v počítání.

- **Autor:** [TheFrederick (@thefrederick-git)](https://github.com/thefrederick-git)
- **Původní autor:** [FOFOLA_1 (@FOFOLA1)](https://github.com/FOFOLA1/Discord-Counting-Bot)

## 🔧 Sestav si vlastního Discord bota!
1. Naklonuj si náš repozitář
2. Nastav a aktivuj si virtuální prostředí (VE) 
```bash
python -m venv ./venv
./venv/Scripts/activate.bat
```
3. Nainstaluj potřebné balíčky
```bash
pip install -r requirements.txt
```
4. Vytvoř .env soubor v kořenovém adresáři projektu a vlož tento obsah do souboru:
```bash
TOKEN = <your_api_secret>
ALLOWED_CHANNEL_ID = <guild_text_channel_id>
```
5. Zapni Discord bota
```bash
python main.py
```
![Let's Code banner](https://lets-code.cz/assets/content/LC_Banner_GitHub.png)
