// This is a JavaScript code that defines the location of recruitment centers, and sets up a map with markers for these centers.

// The LatitudeLongitude array holds the latitude and longitude coordinates of each recruitment center.
var LatitudeLongitude = [{
        lat: 51.50551714132441,
        lng: -0.1651967952227699
    },
    {
        lat: 40.77603773404491,
        lng: -73.97239918809241
    },
    {
        lat: -33.8637228711469,
        lng: 151.2176002382263
    },
    {
        lat: 25.23462190325834,
        lng: 55.29889402751128
    },
    {
        lat: -22.949002295746187,
        lng: -43.15544855337829
    }
];

// The infoWindowContent array holds the contact information for each recruitment center.
var infoWindowContent = [
    '<h1>London</h1><p>Phone Number:</p><ul><li>1234567890</li></ul><p>Email Address:</p><ul><li>London@email.com</li></ul>',
    '<h1>New York</h1><p>Phone Number:</p><ul><li>2345678901</li></ul><p>Email Address:</p><ul><li>NewYork@email.com</li></ul>',
    '<h1>Sydney</h1><p>Phone Number:</p><ul><li>3456789012</li></ul><p>Email Address:</p><ul><li>Sydney@email.com</li></ul>',
    '<h1>Dubai</h1><p>Phone Number:</p><ul><li>4567890123</li></ul><p>Email Address:</p><ul><li>Dubai@email.com</li></ul>',
    '<h1>Rio</h1><p>Phone Number:</p><ul><li>5678901234</li></ul><p>Email Address:</p><ul><li>Rio@email.com</li></ul>',
];

// The map and mapContent variables are used to create and interact with the Google Map.
var map;
var mapContent;

// The recruitmentMap function sets up the Google Map and adds markers for each recruitment center.
function recruitmentMap() {

    // Set the start position of the map to the latitude and longitude of the third recruitment center in the array.
    var startPosition = LatitudeLongitude[3];

    // Set the zoom level and center position of the map.
    var centeredPosition = {
        center: startPosition,
        zoom: 2
    };

    // Create a new Google Map object and center it on the startPosition.
    map = new google.maps.Map(document.getElementById('map'), centeredPosition);
    
    // Create a new InfoWindow object to display the contact information for each recruitment center.
    mapContent = new google.maps.InfoWindow();
    
    // Add a marker for each recruitment center to the Google Map.
    for (var i = 0; i < LatitudeLongitude.length; i++) {
        pin(LatitudeLongitude[i], infoWindowContent[i]);
    }
}

// The pin function creates a marker on the Google Map for a given latitude and longitude, and displays the contact information for that recruitment center when the marker is clicked.
function pin(LatitudeLongitudeLocations, infoWindowContents) {
    // Create a new marker object on the Google Map at the LatitudeLongitudeLocations.
    var marker = new google.maps.Marker({
        position: LatitudeLongitudeLocations,
        map: map
    });
    //Opens InfoWindow when clicked
    marker.addListener('click', function () {
        mapContent.setContent(infoWindowContents);
        mapContent.open(map, this);
    });
}