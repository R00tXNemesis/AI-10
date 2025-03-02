import requests
import concurrent.futures

# Daftar lebih dari 100 situs untuk pencarian username
SITES = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://x.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "YouTube": "https://www.youtube.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Medium": "https://medium.com/@{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "Flickr": "https://www.flickr.com/people/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Dribbble": "https://dribbble.com/{}",
    "VK": "https://vk.com/{}",
    "Blogger": "https://{}.blogspot.com",
    "WordPress": "https://{}.wordpress.com",
    "Goodreads": "https://www.goodreads.com/{}",
    "Bandcamp": "https://{}.bandcamp.com",
    "500px": "https://500px.com/{}",
    "Replit": "https://replit.com/@{}",
    "CodePen": "https://codepen.io/{}",
    "HackTheBox": "https://www.hackthebox.com/home/users/profile/{}",
    "AskFM": "https://ask.fm/{}",
    "WeHeartIt": "https://weheartit.com/{}",
    "LastFM": "https://www.last.fm/user/{}",
    "Gravatar": "https://gravatar.com/{}",
    "Patreon": "https://www.patreon.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Gumroad": "https://{}.gumroad.com",
    "AngelList": "https://angel.co/u/{}",
    "Coub": "https://coub.com/{}",
    "Wattpad": "https://www.wattpad.com/user/{}",
    "MixCloud": "https://www.mixcloud.com/{}",
    "Gfycat": "https://gfycat.com/@{}",
    "Vero": "https://www.vero.co/{}",
    "Badoo": "https://badoo.com/en/profile/{}",
    "OK.ru": "https://ok.ru/{}",
    "LiveJournal": "https://{}.livejournal.com",
    "Canva": "https://www.canva.com/{}/",
    "Lomography": "https://www.lomography.com/homes/{}",
    "Ello": "https://ello.co/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "Furaffinity": "https://www.furaffinity.net/user/{}",
    "Scribd": "https://www.scribd.com/user/{}",
    "Kaggle": "https://www.kaggle.com/{}",
    "Keybase": "https://keybase.io/{}",
    "Trakt": "https://trakt.tv/users/{}",
    "Hackster": "https://www.hackster.io/{}",
    "Chess": "https://www.chess.com/member/{}",
    "Duolingo": "https://www.duolingo.com/profile/{}",
    "Ebay": "https://www.ebay.com/usr/{}",
    "Fanpop": "https://www.fanpop.com/fans/{}",
    "Kofi": "https://ko-fi.com/{}",
    "Venmo": "https://venmo.com/{}",
    "Unsplash": "https://unsplash.com/@{}",
    "BitBucket": "https://bitbucket.org/{}",
}

# Fungsi untuk mengecek username di situs tertentu
def cek_username(site, url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[✓] {site}: {url}")  # Jika username ditemukan
        else:
            print(f"[X] {site}: Tidak ditemukan")  # Jika tidak ditemukan
    except requests.exceptions.RequestException:
        print(f"[!] {site}: Gagal mengakses")

# Fungsi utama untuk menjalankan pencarian secara paralel
def main(username):
    print(f"\n🔎 Mencari jejak digital untuk: {username}\n")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for site, url in SITES.items():
            executor.submit(cek_username, site, url.format(username))

if __name__ == "__main__":
    user = input("Masukkan username yang ingin dilacak: ")
    main(user)