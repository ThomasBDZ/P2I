var str = '{{ data}}';
      let longueur = str.length;
      let myMap;
          let canvas;
          const mappa = new Mappa('Leaflet');
          let data = [];
          let ecole = str.substring(5, longueur-5)
          console.log(ecole)
          const options = {
            lat: 0,
            lng: 0,
            zoom: 4,
            style: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png' //choix du type de la carte du monde (ici elle est classique)
          }
          
          function setup(){
            canvas = createCanvas(800,640);
            myMap = mappa.tileMap(options); 
            myMap.overlay(canvas) 
          
            // Chargement des données
            Integres = loadTable('static/excel/Admis.csv', 'csv', 'header');
          
            // Refait les cercles seulement quand la map change et pas à chaque frame
            myMap.onChange(drawIntegres);
          
            fill(70, 203,31); 
            stroke(100);
          }
          
          function draw(){
          }
          // Draw the Integres
          function drawIntegres() {
            // Clear the canvas
            clear();
            let max = 0;
            let min = Infinity;
            for (let i = 0; i < Integres.getRowCount(); i++) {
              const latitude = Number(Integres.getString(i, 'latitude'));
              const longitude = Number(Integres.getString(i, 'longitude'));
              let count = Number(Integres.getString(i, ecole ));
              data.push({
                  latitude,
                  longitude,
                  count
                });
          
                if (count > max) {
                  max = count;
                }
                if (count < min) {
                  min = count;
                }
            }
              console.log(data)
              let minD = sqrt(min);
              let maxD = sqrt(max);
          
            for (let country of data) {
              country.diameter = map(sqrt(country.count), minD, maxD, 0, 6);
            }
            for (let country of data) {
              const pix = myMap.latLngToPixel(country.latitude, country.longitude);
              fill(frameCount % 255, 0, 200, 1);
              const zoom = myMap.zoom();
              const scl = pow(2, zoom);
              ellipse(pix.x, pix.y, country.diameter * scl);
            }
          }