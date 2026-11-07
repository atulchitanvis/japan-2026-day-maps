# Japan 2026 Day Maps

A phone-first web app with a zoomable street map for each day of the Japan trip (19 Nov – 5 Dec 2026, Osaka → Tokyo). It has no build step: open `index.html` and it reads `trip.json`.

- **Day strip** at the top. On open the app picks today's day (Japan time) if the date is in the trip, otherwise the last day you viewed, otherwise Day 1. Bookmark a day with `#day-1` … `#day-17`, or the trip overview with `#overview`.
- **Map:** numbered pins in visit order. Indigo pins are regular stops, orange pins are meals, and dashed outlines are optional stops. Pins that overlap on screen spread out side by side so each one can be tapped.
- **Route lines:** train is solid indigo, bus is dashed amber, taxi is dashed plum, flight is solid teal, and walking is dotted grey. Walking lines follow real footpaths.
- **Tap a pin:** a popup shows the time, notes, **Open in Maps** and **Directions**, and the matching card in the list is highlighted. **Tap a card:** the map zooms to that stop.
- **Buttons on the map:** ◎ shows your location (blue dot with an accuracy circle; it only asks for permission when you tap it), ⛶ fits the whole day, and ↑ makes the map bigger.
- **Google Maps hand-off:** every stop has **Open in Maps**, every leg has **Directions**, and each day has **Open full day in Google Maps**.
- **Booking numbers:** tap a booking pill or tag that contains a reference (e.g. `A47431`) to copy it.
- **Now / Next:** a banner on today's tab shows the current and next stop. Times like "Morning" or "Lunch" are estimated.
- **Works offline:** it's a PWA. The app, `trip.json` and the walking routes are cached on first visit, and map tiles are cached as you look at them. **⬇ Offline maps** saves tiles in advance for one day or the whole trip.

## Run locally

```bash
cd japan-2026-day-maps
python3 -m http.server 8000      # or: npx serve
# open http://localhost:8000
```

Opening the file straight from disk (`file://`) won't work, because the browser blocks it from loading `trip.json`.

## Deploy to GitHub Pages

1. Create a repository, e.g. `japan-2026-day-maps`.
2. Push these files to the `main` branch, at the repo root:
   ```bash
   git remote add origin https://github.com/<you>/japan-2026-day-maps.git
   git push -u origin main
   ```
3. On GitHub, go to **Settings → Pages → Build and deployment**: Source **Deploy from a branch**, Branch **main**, folder **/ (root)**, then Save.
4. After a minute the app is live at `https://<you>.github.io/japan-2026-day-maps/`.

**On the iPhone:** open the URL in Safari, tap **Share → Add to Home Screen**, and launch it from the icon so it runs full-screen. Then open **⬇ Offline maps** on Wi-Fi.

`.nojekyll` is included so GitHub serves the files as they are.

## Editing the itinerary (`trip.json`)

`trip.json` is an array with one object per day:

```jsonc
{
  "day": 4, "date": "22 Nov 2026", "weekday": "Sun", "city": "Kyoto",
  "title": "Arashiyama, then check in to Kyoto",
  "stay": "Rinn Kamiebisu",
  "bookings": [ { "label": "Daizen lunch", "done": false } ],   // done:true → green ✓, else amber ○
  "stops": [
    {
      "n": 1,                                   // number shown on the pin
      "name": "Osaka Station",
      "mapsQuery": "Osaka Station JR, Japan",   // what Google Maps searches for
      "lat": 34.7025, "lng": 135.4959,          // where the pin goes
      "time": "~6:30",                          // free text; "HH:MM" also drives Now/Next
      "notes": "Rucksacks with you.",
      "tags": ["Booked A47431"],                // "Booked…" green; Reserve/Call/To book/To do amber
      "meal": true,                             // orange pin (optional field)
      "optional": true,                         // dashed pin + "Optional" tag (optional field)
      "arriveBy": "train",                      // how you get here from the previous stop:
                                                // train | bus | taxi | walk | flight
      "legNote": "JR Kyoto Line, ~55 min"       // shown between the cards
    }
  ]
}
```

- The first stop of a day has no `arriveBy` or `legNote`.
- To find coordinates for a new stop, right-click the place in Google Maps (or long-press it on the phone) and copy the lat, lng.
- Commit and push. Phones that already have the app open the cached copy first, fetch the new `trip.json` in the background, and redraw with a toast saying "Itinerary updated".
- If you add or move a stop that you **walk** to, run `python3 tools/routes.py` to refresh `routes.json` with the walking path. If you skip this, the app looks the path up live when online and otherwise draws a straight line.
- Check the JSON is valid before pushing: `python3 -m json.tool trip.json > /dev/null`

## Data notes

- All 127 stops were geocoded with OpenStreetMap Nominatim (`tools/geocode.py`, 1 request/second). See **`GEOCODE_LOG.md`** for what moved and by how much, the **11 stops that couldn't be matched** (their approximate pins are unchanged), and a few worth a quick look.
- The Google Maps buttons search by `mapsQuery`, not by the pin, so they land on Google's own result even where an OSM pin is a little off.

## Tiles and their usage policy

The app uses the standard OpenStreetMap tiles (© OpenStreetMap contributors). CARTO's free Voyager and Dark Matter styles now return "API key required", so they aren't used. Dark mode applies a CSS colour inversion to the same OSM tiles, so one offline download covers both themes.

OSM's tile servers are run by volunteers, and their [usage policy](https://operations.osmfoundation.org/policies/tiles/) discourages bulk downloads. The offline downloader therefore:

- only fetches zoom 16 and below, in small areas around stops and walking routes plus a coarse overview of each day (about 1,650 tiles, ~30 MB, for the whole trip),
- uses 2 parallel requests with a 250 ms pause after each, caps the total at 3,000 tiles, and skips tiles already saved.

If you'd rather use a keyed provider (MapTiler, Stadia, Thunderforest), change `TILE_URL`, `ATTR` and `tileUrl()` in `index.html` and `isTile()` in `sw.js`.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole app (Leaflet 1.9.4 from unpkg) |
| `trip.json` | Itinerary data. Edit this one. |
| `routes.json` | Walking-path geometry, generated by `tools/routes.py` (OSRM foot profile via routing.openstreetmap.de; the router.project-osrm.org demo only routes cars) |
| `sw.js` | Service worker: offline app shell and tile cache |
| `manifest.webmanifest`, `icons/` | Home-screen install |
| `GEOCODE_LOG.md` | Geocoding results and the stops to check |
| `tools/geocode.py`, `tools/routes.py` | Data scripts (Python 3, standard library only) |
