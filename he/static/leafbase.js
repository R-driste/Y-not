var map = L.map(document.getElementById('map'),{minZoom: 3}).setView(([40, -100]), 4);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 20,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    // add Stamen Watercolor to map.

    var bounds = [
        [23.396308, -125.0], // Southwest corner (latitude, longitude)
        [48.384358, -66.93457] // Northeast corner (latitude, longitude)
    ];
    
map.setMaxBounds(bounds);

map.on('click', function(event) {
    // Get the coordinates of the clicked point
    var lat = event.latlng.lat;
    var lng = event.latlng.lng;
    
    // Add a marker at the clicked point
    var marker = L.marker([lat, lng]).addTo(map);
});