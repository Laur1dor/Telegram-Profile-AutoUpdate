import asyncio
import datetime
from datetime import timedelta
from pyrogram import Client, idle
from pyrogram.errors import FloodWait
import httpx

api_id = # YOUR_API_ID
api_hash = '' # YOUR_API_HASH 
app = Client("my_account", api_id=api_id, api_hash=api_hash)

def get_time(offset_hours):
    return (datetime.datetime.utcnow() + timedelta(hours=offset_hours)).strftime("%H:%M")

async def fetch_prices():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,the-open-network&vs_currencies=usd"
        async with httpx.AsyncClient() as client:
            r = await client.get(url, timeout=10)
            data = r.json()
            btc = int(round(data["bitcoin"]["usd"]))
            eth = int(round(data["ethereum"]["usd"]))
            ton = round(data["the-open-network"]["usd"], 2)
            return btc, eth, ton
    except Exception as e:
        print(f"[Ошибка CoinGecko] {e}")
        return "?", "?", "?"

async def fetch_cbr_rates():
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get("https://www.cbr-xml-daily.ru/daily_json.js", timeout=10)
            data = r.json()["Valute"]
            usd = round(data["USD"]["Value"], 2)
            eur = round(data["EUR"]["Value"], 2)
            cny = round(data["CNY"]["Value"], 2)
            return usd, eur, cny
    except Exception as e:
        print(f"[Ошибка CBR] {e}")
        return "??", "??", "??"

async def update():
    while True:
        try:
            moscow = get_time(3)
            #okinawa = get_time(9)
            tokyo = get_time(9)
            paris = get_time(2)

            name = f"YOUR_NICKNAME {moscow}"

            btc, eth, ton = await fetch_prices()
            usd, eur, cny = await fetch_cbr_rates()

            bio = (
                f"✅Updated every minute┊🇷🇺MSK {moscow}┊🇯🇵TYO {tokyo}┊🇫🇷PAR {paris}┊"
                f"🟠BTC ${btc}┊🟣ETH ${eth}┊🔷TON ${ton:.2f}┊"
                f"💵USD {usd}₽┊💶EUR {eur}₽┊💴CNY {cny}₽"
            )

            me = await app.get_me()

            if me.first_name != name:
                await app.update_profile(first_name=name)
                print(f"[OK] Имя обновлено → {name}")

            await app.update_profile(bio=bio)
            print(f"[OK] Bio обновлено")

        except FloodWait as e:
            print(f"[FloodWait] Telegram ограничил. Ждём {e.value} секунд.")
            await asyncio.sleep(e.value)
        except Exception as e:
            print(f"[Ошибка] {e}")

        # Ждём до начала следующей минуты
        await asyncio.sleep(60 - datetime.datetime.now().second)

async def main():
    await app.start()
    asyncio.create_task(update())
    await idle()
    await app.stop()

asyncio.run(main())
