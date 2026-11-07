/* Japan 2026 Day Maps service worker
   - App shell + trip data: served from cache instantly, refreshed in the background.
   - Map tiles: cache-first (saved as you browse, or via "Offline maps"). */
const VERSION = 'v1';
const SHELL = 'shell-' + VERSION;
const TILES = 'tiles-v1'; // keep across app updates so saved maps survive
const LEAFLET = [
  'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',
  'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
];
const LOCAL = ['./index.html', './trip.json', './routes.json', './manifest.webmanifest',
  './icons/icon-192.png', './icons/icon-512.png', './icons/apple-touch-icon.png'];

self.addEventListener('install', e => {
  e.waitUntil((async () => {
    const c = await caches.open(SHELL);
    await c.addAll(LOCAL);
    await Promise.all(LEAFLET.map(async u => { const r = await fetch(u, {mode: 'cors'}); if (r.ok) await c.put(u, r); }));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) if (k !== SHELL && k !== TILES) await caches.delete(k);
    await self.clients.claim();
  })());
});

const isTile = u => u.hostname === 'tile.openstreetmap.org';

async function tile(req) {
  const c = await caches.open(TILES), key = req.url;
  const hit = await c.match(key);
  if (hit) return hit;
  try {
    const r = await fetch(req);
    if (r.ok) c.put(key, r.clone()).catch(() => {});
    return r;
  } catch (err) {
    return new Response('', {status: 504, statusText: 'offline'});
  }
}

async function shell(e) {
  const req = e.request, url = new URL(req.url);
  const c = await caches.open(SHELL);
  const fresh = url.searchParams.has('fresh');
  // Same-origin files are keyed by path (query ignored); page navigations map to index.html.
  const key = url.origin !== location.origin ? req.url
    : (req.mode === 'navigate' || url.pathname.endsWith('/')) ? new URL('./index.html', self.registration.scope).href
    : url.origin + url.pathname;
  const network = fetch(req, fresh ? {cache: 'no-store'} : undefined).then(r => {
    if (r.ok) c.put(key, r.clone()).catch(() => {});
    return r;
  });
  if (fresh) return network.catch(() => c.match(key));
  const cached = await c.match(key);
  if (cached) { e.waitUntil(network.catch(() => {})); return cached; }
  return network.catch(async () => (await c.match(key)) || new Response('Offline', {status: 503}));
}

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (isTile(url)) return e.respondWith(tile(req));
  if (url.origin === location.origin || url.hostname === 'unpkg.com') return e.respondWith(shell(e));
});
