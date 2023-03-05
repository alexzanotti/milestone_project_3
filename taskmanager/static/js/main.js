//The location of the recruitment centres
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
}];


//The country, phone number and email address content for each recruitment centre
var infoWindowContent = [
'<h1>London</h1><p>Phone Number:</p><ul><li>1234567890</li></ul><p>Email Address:</p><ul><li>London@email.com</li></ul>',
'<h1>New York</h1><p>Phone Number:</p><ul><li>2345678901</li></ul><p>Email Address:</p><ul><li>NewYork@email.com</li></ul>',
'<h1>Sydney</h1><p>Phone Number:</p><ul><li>3456789012</li></ul><p>Email Address:</p><ul><li>Sydney@email.com</li></ul>',
'<h1>Dubai</h1><p>Phone Number:</p><ul><li>4567890123</li></ul><p>Email Address:</p><ul><li>Dubai@email.com</li></ul>',
'<h1>Rio</h1><p>Phone Number:</p><ul><li>5678901234</li></ul><p>Email Address:</p><ul><li>Rio@email.com</li></ul>',
];

// map and mapcontent variables
var map;
var mapContent;

// functions to create the map in index.html, set positioning and add the markers
function recruitmentMap() {

var startPosition = LatitudeLongitude[3];
var centeredPosition = {
    center: startPosition,
    zoom: 2
};

map = new google.maps.Map(document.getElementById('map'), centeredPosition);
mapContent = new google.maps.InfoWindow();
for (var i = 0; i < LatitudeLongitude.length; i++) {
    pin(LatitudeLongitude[i], infoWindowContent[i]);
}
}

function pin(LatitudeLongitudeLocations, infoWindowContents) {
//Creates marker based on the LatitudeLongitude of each country
var marker = new google.maps.Marker({
    position: LatitudeLongitudeLocations,
    map: map
});
//Opens InfoWindow when clicked
marker.addListener('click', function() {
    mapContent.setContent(infoWindowContents);
    mapContent.open(map, this);
});
}
function sendmail() {
    let fullName = document.getElementById("name").value;
    let userEmail = document.getElementById("email").value;
    let userQuery = document.getElementById("query").value;
    let userMessage = document.getElementById("message").value;

        var contactParams = {
            from_name: fullName,
            from_email: userEmail,
            query: userQuery,
            message: userMessage
        };

        emailjs.send('service_m38yb2j', 'template_ki89pno', contactParams).then(function (res) {})

      //the user will be re-directed to the contact_sent page upon submitting the contact form
      //location.href = '{{ url_for('contact_sent') }}';
}