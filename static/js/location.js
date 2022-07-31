onload = getLocation()


function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

var lat;
var lon;

function showPosition(position) {
    // 18.4651194,73.8353216
    lat = 18.4651194;
    // lat = position.coords.latitude;
    lon = 73.8353216;
    // lon = position.coords.longitude;
    var url = "https://maps.google.com/maps?q=" + lat + "," + lon + "&hl=es;z=17&amp&output=embed";
    document.getElementById("myframe").setAttribute("src", url);
}

function getCo_ordinates() {
    if (document.getElementById('coordinates').value != "") {
        document.getElementById('coordinates').value = null
    } else {
        document.getElementById('coordinates').value = lat + "," + lon;
    }
}

function getCoordinates() {
    return (lat + "," + lon);
}
