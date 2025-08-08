
import logging
from telegram import Bot
from datetime import datetime, timedelta
import asyncio

# --- Bot Token ---
TOKEN = "token"

# --- Ders Programı ---
# Format: (Gün, Saat): "Ders Adı"
# Saat formatı 24h, dakika 00
ders_programi = {
    ("Pazartesi", "11:00"): "Ahmet - Proje",
    ("Salı", "11:00"): "Folsec - Proje",
    ("Perşembe", "11:00"): "Ahmet - Proje",
    ("Cuma", "11:00"): "Folsec - Proje",
    ("Pazartesi", "14:00"): "Öykü - Hakan Pro",
    ("Perşembe", "14:00"): "Öykü - Hakan Pro",
    ("Pazartesi", "18:00"): "Mon18",
    ("Çarşamba", "18:00"): "Wed18",
    ("Pazartesi", "20:00"): "Mon20",
    ("Salı", "20:00"): "Salih - Pro",
    ("Çarşamba", "20:00"): "Wed20",
    ("Perşembe", "20:00"): "Thu20",
    ("Cuma", "20:00"): "Fri20",
    ("Salı", "21:30"): "Enes - Pro",
    ("Cuma", "21:30"): "Enes - Pro",
    ("Cuma", "02:44"): "Enes - Pro",
}

# --- Gün Dönüşümü ---
gun_map = {
    0: "Pazartesi",
    1: "Salı",
    2: "Çarşamba",
    3: "Perşembe",
    4: "Cuma",
    5: "Cumartesi",
    6: "Pazar"
}

# --- Log ---
logging.basicConfig(level=logging.INFO)

async def hatirlatma():
    bot = Bot(token=TOKEN)
    chat_id = 5136334837  # Telegram chat_id’n (kendi botuna /start atınca log’dan görebilirsin)

    while True:
        simdi = datetime.now()
        simdi_gun = gun_map[simdi.weekday()]
        simdi_plus = (simdi + timedelta(hours=1)).strftime("%H:%M")

        if (simdi_gun, simdi_plus) in ders_programi:
            ders = ders_programi[(simdi_gun, simdi_plus)]
            mesaj = f"⏳ 1 saat sonra dersin var: {ders} ({simdi_plus})"
            await bot.send_message(chat_id=chat_id, text=mesaj)

        await asyncio.sleep(60)  # Her dakika kontrol et

if __name__ == "__main__":
    asyncio.run(hatirlatma())

