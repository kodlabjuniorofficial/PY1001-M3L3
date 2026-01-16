import requests

# 1. GÖREV: Aramak istediğimiz kelimeyi belirleyelim
topic = "Robot"
url = f"https://tr.wikipedia.org/api/rest_v1/page/summary/{topic}"
# 2. GÖREV: Wikipedia bizi 'robot' sanıp engellemesin diye kimlik kartı ekleyelim
headers = {'User-Agent': 'BilgeBot/1.0'}

# 3. GÖREV: İnternetten veriyi çekip JSON olarak kaydedelim
response = requests.get(url, headers=headers)
veri = response.json()

# 4. GÖREV: extract (bilgi) ve thumbnail (görsel) anahtarlarını çekin
# bilgi = ...
# gorsel = ...

print(f"--- {topic} Hakkında Bulunanlar ---")
# Yazdırın...