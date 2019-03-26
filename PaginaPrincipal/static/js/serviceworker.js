let cacheName = 'mis-perris';


self.addEventListener('install', function(event) {
    event.waitUntil(
      caches.open(cacheName).then(function(cache) {
        return cache.addAll([
          '/base_layout'
        ]);
      })
    );
  });
  
  self.addEventListener('fetch', function(event) {
    if(!self.navigator.onLine){
        var requestUrl = new URL(event.request.url);
        if (requestUrl.origin === location.origin) {
            if ((requestUrl.pathname === '/')) {
            event.respondWith(caches.match('/base_layout'));
            return;
            }
        }
        event.respondWith(
            caches.match(event.request).then(function(response) {
            return response || fetch(event.request);
            })
        );
    }
  });