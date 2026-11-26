// Bump V on every release: install pre-caches the new shell, activate drops old caches.
// Stale-while-revalidate means a deployed change shows up on the *second* launch.
const V = 'tl-v7';
const SHELL = ['./', 'index.html', 'manifest.json', 'icon-180.png', 'icon-192.png', 'icon-512.png'];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(V)
      .then(c => c.addAll(SHELL.map(u => new Request(u, { cache: 'reload' }))))  // bypass the HTTP cache
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== V).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Stale-while-revalidate for every GET, same-origin or not (Google Fonts CSS and font files included).
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET' || !req.url.startsWith('http')) return;
  const nav = req.mode === 'navigate';
  e.respondWith((async () => {
    const cache = await caches.open(V);
    const cached = (await cache.match(req, { ignoreSearch: nav })) || (nav ? await cache.match('./') : undefined);
    const fresh = fetch(req).then(res => {
      if (res && (res.status === 200 || res.type === 'opaque')) cache.put(req, res.clone()).catch(() => {});
      return res;
    }).catch(() => undefined);
    if (cached) { e.waitUntil(fresh); return cached; }
    const res = await fresh;
    if (res) return res;
    return (nav && (await cache.match('index.html'))) || Response.error();
  })());
});
