var map = L.map(document.getElementById('map'),{minZoom: 2}).setView(([40, -100]), 4);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 20,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    // add Stamen Watercolor to map.

    var bounds = [
        [-56, -150.0], // Southwest corner (latitude, longitude)
        [156, 160] // Northeast corner (latitude, longitude)
    ];
    
map.setMaxBounds(bounds);



