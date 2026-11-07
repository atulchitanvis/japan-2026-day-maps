#!/usr/bin/env python3
"""Build routes.json: real walking geometry for every 'walk' leg in trip.json.

Uses the FOSSGIS OSRM foot profile (the router.project-osrm.org demo only
routes cars). Run again after editing coordinates; missing legs fall back to
a live lookup in the app, then to straight lines.
"""
import json, os, time, urllib.request, math

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = "https://routing.openstreetmap.de/routed-foot/route/v1/foot/{},{};{},{}?overview=full&geometries=geojson"
UA = "Japan2026DayMaps/1.0 (personal trip map)"
key = lambda a, b: f"{a['lat']:.5f},{a['lng']:.5f}>{b['lat']:.5f},{b['lng']:.5f}"
km = lambda a, b: 6371 * math.hypot(math.radians(b['lat'] - a['lat']), math.radians(b['lng'] - a['lng']) * math.cos(math.radians(a['lat'])))

trip = json.load(open(os.path.join(ROOT, "trip.json")))
out = {}
for d in trip:
    st = d["stops"]
    for i in range(1, len(st)):
        a, b = st[i - 1], st[i]
        if b.get("arriveBy") != "walk" or km(a, b) < 0.02:
            continue
        k = key(a, b)
        if k in out:
            continue
        req = urllib.request.Request(URL.format(a["lng"], a["lat"], b["lng"], b["lat"]), headers={"User-Agent": UA})
        try:
            j = json.load(urllib.request.urlopen(req, timeout=30))
            r = j["routes"][0]
            pts = [[round(y, 5), round(x, 5)] for x, y in r["geometry"]["coordinates"]]
            # snap the ends to the pins so lines meet the markers
            pts = [[a["lat"], a["lng"]]] + pts + [[b["lat"], b["lng"]]]
            out[k] = pts
            print(f"Day {d['day']} {a['n']}->{b['n']}: {r['distance']/1000:.2f} km walk, {r['duration']/60:.0f} min (straight {km(a,b):.2f} km)")
        except Exception as e:
            print(f"Day {d['day']} {a['n']}->{b['n']}: FAILED {e}")
        time.sleep(1.1)
json.dump(out, open(os.path.join(ROOT, "routes.json"), "w"), separators=(",", ":"))
print(len(out), "legs written")
