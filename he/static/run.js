import map from "he/static/leafbase.js"
function ADD(){
    for (lat,lng in coords){
        var newmarker = L.marker([lat, lng]).addTo(map)
    }
};