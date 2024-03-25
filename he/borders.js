fetch('path/to/your/geojson/file.json')
  .then(response => response.json())
  .then(data => {
    // Use the fetched GeoJSON data here
    console.log(data);
  });
