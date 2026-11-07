#!/usr/bin/env python3
"""Geocode every stop in trip.json with OSM Nominatim (1 req/s).

Usage: python3 tools/geocode.py [--write]
Writes tools/geocode_cache.json and GEOCODE_LOG.md. With --write, updates
lat/lng in trip.json for confident matches only.
"""
import json, math, re, sys, time, urllib.parse, urllib.request, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = "Japan2026DayMaps/1.0 (personal trip map; github pages)"
CACHE_F = os.path.join(ROOT, "tools", "geocode_cache.json")
cache = json.load(open(CACHE_F)) if os.path.exists(CACHE_F) else {}
last = [0.0]

def km(a, b, c, d):
    r = math.radians
    x = math.sin(r(c - a) / 2) ** 2 + math.cos(r(a)) * math.cos(r(c)) * math.sin(r(d - b) / 2) ** 2
    return 12742 * math.asin(math.sqrt(x))

def search(q):
    if q in cache:
        return cache[q]
    wait = 1.1 - (time.time() - last[0])
    if wait > 0:
        time.sleep(wait)
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(
        {"format": "jsonv2", "q": q, "countrycodes": "jp", "limit": 5, "accept-language": "en"})
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                res = json.load(r)
            break
        except Exception as e:
            print("  retry", q, e, file=sys.stderr); time.sleep(3)
    else:
        res = None
    last[0] = time.time()
    if res is not None:
        cache[q] = res
        json.dump(cache, open(CACHE_F, "w"), ensure_ascii=False, indent=0)
    return res or []

# Extra queries (often the Japanese name) tried FIRST for stops whose English
# mapsQuery Nominatim can't resolve or resolves to the wrong place.
OVERRIDES = {
    "Kansai International Airport, Japan": ["関西国際空港 第1ターミナル", "Kansai Airport Terminal 1"],
    "BON Condominium Umeda Osaka, Japan": ["BON Condominium Umeda", "ボンコンドミニアム梅田"],
    "Kinryu Ramen Midosuji Dotonbori Osaka, Japan": ["金龍ラーメン 御堂筋店", "金龍ラーメン", "Kinryu Ramen"],
    "Osaka Umeda Station Hankyu, Japan": ["大阪梅田駅", "Osaka-umeda"],
    "Minoh Falls, Japan": ["箕面大滝", "Minoo Falls"],
    "Yaekatsu Janjan Yokocho Osaka, Japan": ["八重勝", "Yaekatsu"],
    "Osaka Namba Station Kintetsu, Japan": ["大阪難波駅", "Osaka-Namba"],
    "Ise Jingu Naiku Uji Bridge, Japan": ["宇治橋 伊勢", "皇大神宮", "Kotai Jingu"],
    "Meoto Iwa Futami, Japan": ["夫婦岩", "二見興玉神社"],
    "Adashino Nenbutsuji, Japan": ["化野念仏寺", "Adashino Nembutsu-ji"],
    "Otagi Nenbutsuji, Japan": ["愛宕念仏寺", "Otagi Nembutsu-ji"],
    "Arashiyama Daizen Kyoto, Japan": ["大善 嵐山", "Daizen"],
    "Rinn Kamiebisu Kyoto, Japan": ["Rinn Kamiebisu"],
    "Hana Tanuki Kyoto okonomiyaki, Japan": ["花たぬき 京都", "花たぬき"],
    "Kyoto Sumibi Kushiyaki Tsujiy, Japan": ["炭火串焼 辻や", "辻や 京都"],
    "Philosopher's Path Kyoto, Japan": ["哲学の道", "Philosopher's Walk"],
    "Gion Okaru Kyoto, Japan": ["祇園おかる", "おかる 祇園"],
    "Hanamikoji Street Kyoto, Japan": ["花見小路通", "Hanamikoji-dori"],
    "Kyoto Station Shinkansen, Japan": ["京都駅", "Kyoto Station"],
    "Miyota Matsumoto soba, Japan": ["みよ田 松本", "みよ田"],
    "Kiso Mikawaya Kiso-Fukushima, Japan": ["三河屋 木曽福島", "三河屋 木曽町", "Mikawaya Kiso"],
    "Magome Pass Nakasendo, Japan": ["馬籠峠", "Magome Pass"],
    "Takayama Nohi Bus Center, Japan": ["濃飛バスセンター", "高山濃飛バスセンター", "Takayama Nohi Bus Center"],
    "Shiroyama Viewpoint Shirakawago, Japan": ["荻町城跡展望台", "城山天守閣 展望台", "Ogimachi Castle Ruins Observatory"],
    "Wada House Shirakawago, Japan": ["和田家 白川村", "Wada House"],
    "Shirakawago Irori restaurant, Japan": ["いろり 白川村", "Irori Shirakawa"],
    "Kenrokuen Garden Mayumizaka Gate, Japan": ["真弓坂口", "兼六園 真弓坂", "Kenrokuen"],
    "Morimori Sushi Omicho Kanazawa, Japan": ["もりもり寿し 近江町店", "もりもり寿し"],
    "Kanazawa Katani gold leaf, Japan": ["金沢かたに", "かたに 金箔", "Katani"],
    "Izakaya Gappa Kanazawa, Japan": ["がっぱ 金沢", "居酒屋がっぱ"],
    "Kawaguchiko Hotel, Japan": ["河口湖ホテル", "Kawaguchiko Hotel"],
    "Houtou Kura Funari Kawaguchiko, Japan": ["ほうとう蔵 歩成", "歩成 河口湖"],
    "Oishi Park Kawaguchiko, Japan": ["大石公園", "Oishi Park"],
    "Koshu Houtou Kosaku Kawaguchiko, Japan": ["小作 河口湖駅前店", "甲州ほうとう 小作 河口湖", "Kosaku Kawaguchiko"],
    "Sakuratei Harajuku, Japan": ["さくら亭 神宮前", "Sakuratei"],
    "Toritake Sohonten Shibuya, Japan": ["鳥竹 総本店", "鳥竹"],
    "Kappabashi Dougu Street, Japan": ["かっぱ橋道具街", "合羽橋道具街", "Kappabashi"],
    "Galerie Dentsdelion Tokyo, Japan": ["ギャルリー・ダンドリオン", "Galerie Dentsdelion"],
    "Mendokoro Honta Akihabara, Japan": ["麺処 ほん田 秋葉原本店", "ほん田 秋葉原", "Mendokoro Honda"],
    "Ginza 4-chome, Japan": ["銀座四丁目交差点", "Ginza 4-chome Intersection"],
}

# Matches we looked at and rejected: keep the hand-placed pin.
KEEP_ORIGINAL = {
    "Kawaguchiko Hotel, Japan": "Nominatim returns other hotels (Kawaguchiko Park Hotel / Tominoko Hotel)",
    "Fushimi Inari Taisha, Japan": "OSM centroid is up the mountain; original pin is the main gate",
    "Nara Park, Japan": "OSM centroid is far east of the deer area by Todai-ji",
}
CHECK = {
    "Houtou Kura Funari Kawaguchiko, Japan": "matched the Funari on Route 139 (Oarashi); confirm it is the branch you want",
    "APA Hotel Higashi Shinjuku Kabukicho Tower, Japan": "OSM only says 'APA Hotel' (Kabukicho 2-chome, Shokuan-dori); several APAs nearby",
    "Osaka Umeda Station Hankyu, Japan": "Day 2 stop 1 is named BON Condominium but its mapsQuery is Hankyu Osaka-umeda Station, so the pin is the station",
}

def variants(stop, city):
    q = stop["mapsQuery"]
    yield from OVERRIDES.get(q, [])
    yield q
    base = re.sub(r",\s*Japan$", "", q)
    if base != q:
        yield base
    nm = re.sub(r"^(Dinner|Lunch)[^:]*:\s*", "", stop["name"])
    nm = re.sub(r"\s*\(.*?\)", "", nm).split("+")[0].split("/")[0].strip()
    if nm and nm.lower() not in base.lower():
        yield f"{nm}, {city}"

# How far (km) a match may sit from the original pin before we refuse it.
MAXKM = 2.5
COARSE = {"city", "town", "village", "county", "state", "region", "administrative", "municipality", "suburb", "quarter", "province"}

trip = json.load(open(os.path.join(ROOT, "trip.json")))
CITY = {"Kiso Valley": "Kiso", "Departure": "Narita", "Shirakawa-go": "Shirakawa"}
rows, unmatched, kept = [], [], []
for d in trip:
    city = CITY.get(d["city"], d["city"])
    for s in d["stops"]:
        best = None
        if s["mapsQuery"] in KEEP_ORIGINAL:
            kept.append((d["day"], s["n"], s["name"], KEEP_ORIGINAL[s["mapsQuery"]]))
            print(d["day"], s["n"], s["name"], "-> KEPT"); continue
        for q in variants(s, city):
            for r in search(q):
                if r.get("type") in COARSE or r.get("addresstype") in COARSE:
                    continue
                dist = km(s["lat"], s["lng"], float(r["lat"]), float(r["lon"]))
                if dist <= MAXKM and (best is None or dist < best[1]):
                    best = (r, dist, q)
            if best:
                break
        if best:
            r, dist, q = best
            rows.append((d["day"], s["n"], s["name"], q, r["display_name"][:70], round(dist * 1000), float(r["lat"]), float(r["lon"])))
            s["_new"] = (round(float(r["lat"]), 5), round(float(r["lon"]), 5))
        else:
            unmatched.append((d["day"], s["n"], s["name"], s["mapsQuery"]))
        print(d["day"], s["n"], s["name"], "->", "OK %dm" % rows[-1][5] if best else "UNMATCHED", flush=True)

with open(os.path.join(ROOT, "GEOCODE_LOG.md"), "w") as f:
    f.write("# Geocoding log\n\nNominatim (OpenStreetMap), queried with each stop's `mapsQuery` (fallbacks: query without ', Japan', then stop name + city). "
            f"A match is accepted only if it is a specific place (not a city/district polygon) within {MAXKM} km of the original pin.\n\n")
    f.write(f"## Could not match ({len(unmatched)}) — original approximate pin kept, please check\n\n| Day | # | Stop | mapsQuery |\n|---|---|---|---|\n")
    for u in unmatched:
        f.write("| %s | %s | %s | %s |\n" % u)
    f.write(f"\n## Kept original pin on purpose ({len(kept)})\n\n| Day | # | Stop | Why |\n|---|---|---|---|\n")
    for k in kept:
        f.write("| %s | %s | %s | %s |\n" % k)
    chk = [(d["day"], s["n"], s["name"], CHECK[s["mapsQuery"]]) for d in trip for s in d["stops"] if s["mapsQuery"] in CHECK]
    f.write(f"\n## Matched but worth a glance ({len(chk)})\n\n| Day | # | Stop | Note |\n|---|---|---|---|\n")
    for k in chk:
        f.write("| %s | %s | %s | %s |\n" % k)
    f.write(f"\n## Matched ({len(rows)}) — pin moved by\n\n| Day | # | Stop | Query used | OSM result | Moved (m) |\n|---|---|---|---|---|---|\n")
    for r in rows:
        f.write("| %s | %s | %s | %s | %s | %s |\n" % r[:6])

if "--write" in sys.argv:
    for d in trip:
        for s in d["stops"]:
            if "_new" in s:
                s["lat"], s["lng"] = s.pop("_new")
    txt = json.dumps(trip, ensure_ascii=False, indent=2)
    open(os.path.join(ROOT, "trip.json"), "w").write(txt + "\n")
    print("trip.json updated")
