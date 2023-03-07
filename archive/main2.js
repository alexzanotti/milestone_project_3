//EmailJS function
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
}


function sendmail() {
    // object to collect the users name, email and message
    var content = {
        from_name: document.getElementById("name").value,
        from_email: document.getElementById("email").value,
        query: document.getElementById("query").value,
        message: document.getElementById("message").value
    };
    // variable for both the emailjs serviceID and templateID
    const serviceID = "service_m38yb2j";
    const templateID = "template_ki89pno";
    // send the email
    emailjs.send(serviceID, templateID, content)
}