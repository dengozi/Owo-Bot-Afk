import requests
import time
import random

# --- AYARLAR ---
TOKEN = "TOKEN"
CHANNEL_ID = "CHANNEL"

# OwO botun durdurmamız gereken uyarı kelimeleri
DURDURMA_KELIMELERI = [
    "verify", "captcha", "beep boop", "human", "check",
    "solve", "verification", "robot", "doğrulama", "güvenlik"
]


def son_mesaji_kontrol_et():
    header = {'authorization': TOKEN}
    try:
        # Kanaldaki son 5 mesajı çekiyoruz
        r = requests.get(f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages?limit=5", headers=header)
        if r.status_code == 200:
            mesajlar = r.json()
            for m in mesajlar:
                content = m['content'].lower()
                # Eğer listedeki kelimelerden biri mesajda geçiyorsa yakala
                if any(kelime in content for kelime in DURDURMA_KELIMELERI):
                    return True
    except Exception as e:
        print(f"Hata oluştu: {e}")
    return False


def mesaj_gonder(mesaj):
    payload = {'content': mesaj}
    header = {'authorization': TOKEN}
    requests.post(f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages", data=payload, headers=header)


def baslat():
    print("--- OwO Script Aktif! (Captcha Koruması devrede) ---")
    last_pray_time = 0

    while True:
        # 1. KRİTİK KONTROL: Captcha kelimelerinden biri var mı?
        if son_mesaji_kontrol_et():
            print("\n" + "!" * 40)
            print("!!! CAPTCHA VEYA DOĞRULAMA TESPİT EDİLDİ !!!")
            print("Script güvenlik amacıyla durduruldu.")
            print("Lütfen Discord'u kontrol et ve doğrulamayı yap.")
            print("!" * 40)
            break  # Scripti tamamen kapatır

        # 2. KOMUT BLOĞU (Hızlı ve Verimli)
        print("Komutlar gönderiliyor...")
        mesaj_gonder("owoh")
        time.sleep(random.uniform(1.2, 2.3))

        mesaj_gonder("owob")
        time.sleep(random.uniform(1.2, 2.3))

        mesaj_gonder("owo hunt")
        time.sleep(random.uniform(1.2, 2.3))

        mesaj_gonder("owo battle")

        # 3. PRAY KONTROLÜ (5 Dakikada Bir)
        current_time = time.time()
        if current_time - last_pray_time > 305:
            time.sleep(1.5)
            mesaj_gonder("owo pray")
            print(">> Pray atıldı.")
            last_pray_time = current_time

        # 4. BEKLEME SÜRESİ (Rastgele ve Güvenli)
        bekleme = random.randint(16, 21)
        print(f"{bekleme} saniye sonraki tur başlayacak.\n")
        time.sleep(bekleme)


if __name__ == "__main__":
    baslat()
