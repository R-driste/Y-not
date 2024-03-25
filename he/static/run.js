
function ADD(){
    for (c in coords){
        var newmarker = L.marker([c[0], c[1]]).addTo(map)
    }
};