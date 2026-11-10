/* Japan 2026 Day Maps service worker
   - App shell + trip data: served from cache instantly, refreshed in the background.
   - Map tiles: cache-first (saved as you browse, or via "Offline maps"). */
const VERSION = 'v3';
const SHELL = 'shell-' + VERSION;
const TILES = 'ofm-v1'; // keep across app updates so saved maps survive
const LEAFLET = [
  'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',
  'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
  'https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.css',
  'https://unpkg.com/maplibre-gl@4.7.1/dist/maplibre-gl.js',
  'https://unpkg.com/@maplibre/maplibre-gl-leaflet@0.0.22/leaflet-maplibre-gl.js',
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

const isMap = u => u.hostname === 'tiles.openfreemap.org';
// Styles and the tile index change occasionally: serve cached, refresh in the background.
const isIndex = u => u.pathname.startsWith('/styles/') || u.pathname === '/planet';
// Vector tile URLs carry a data version; key them version-free so saved maps keep working.
const canon = url => url.replace(/\/planet\/[^/]+\//, '/planet/v/');

async function mapAsset(e) {
  const req = e.request, url = new URL(req.url);
  const c = await caches.open(TILES), key = canon(req.url);
  const hit = await c.match(key);
  const network = fetch(req).then(r => { if (r.ok) c.put(key, r.clone()).catch(() => {}); return r; });
  if (hit) { if (isIndex(url)) e.waitUntil(network.catch(() => {})); return hit; }
  return network.catch(() => new Response('', {status: 504, statusText: 'offline'}));
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
  if (isMap(url)) return e.respondWith(mapAsset(e));
  if (url.origin === location.origin || url.hostname === 'unpkg.com') return e.respondWith(shell(e));
});
