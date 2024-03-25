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

markers = []
var lat;
var lng;
map.on('click', function(event) {
    // Get the coordinates of the clicked point
    var lat = event.latlng.lat;
    var lng = event.latlng.lng;
    
    // Add a marker at the clicked point
    var newmarker = L.marker([lat, lng])
    newmarker.addTo(map);
    markers.push(newmarker);
    
    if (markers.length > 1){
        map.removeLayer(markers[0]);
        markers.shift();
    }
});

function getLocation(){
    window.location.replace("/recievejavascriptcoordsjbfouefouesfeuofsu?lat=" + lat + "&long=" + lng);
};
