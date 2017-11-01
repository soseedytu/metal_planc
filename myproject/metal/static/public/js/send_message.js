nameObj = null
emailObj = null
messageObj = null
nameRequiredObj = null
emailRequiredObj = null
messageRequiredObj = null
securityTokenObj = null
contactFormObj = null
emailFormatRequiredObj = null

function sendMessage(obj) {

    nameVal = nameObj.val();
    emailVal = emailObj.val();
    messageVal = messageObj.val();
    target_url = contactFormObj.prop('action')
    security_token =  securityTokenObj.val()

    var isValid = validate_input(nameVal, emailVal, messageVal);

    if (!isValid) return false;

    var message_data = {
        name: nameVal,
        email: emailVal,
        message: messageVal,
        csrfmiddlewaretoken: security_token
    };

    var element = "<div id=\"contactFormContainer\" class=\"col-md-8 col-md-offset-2\"><h3>Sending message.</h3></div>";
    $('#contactFormContainer').replaceWith(element)

    $.ajax({
        url: target_url, // the endpoint
        type: "POST", // http method
        data: message_data,
        // handle a successful response
        success: function (json) {
            // move to last anchor
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            var element = "";
            if(json.errors == "")
            {
                element = "<div id=\"contactFormContainer\" class=\"col-md-8 col-md-offset-2\"><h3>Successfully sent email to Metalpolis.</h3></div>"
            }
            else
            {
                element = "<div id=\"contactFormContainer\" class=\"col-md-8 col-md-offset-2\"><h3>Oops. Something went wrong.</h3></div>"
            }

            $('#contactFormContainer').replaceWith(element)

        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console

            var element = "<div id=\"contactFormContainer\" class=\"col-md-8 col-md-offset-2\"><h3>Oops. Something went wrong.</h3></div>";
            $('#contactFormContainer').replaceWith(element)
        }
    });
}

function register_events() {

    $(document).on('click', '#btnMessage', function () {
        sendMessage($(this))
    });

}

function validate_input(name, email, message) {

    var issues = 0;
    hideRequiredMessages();

    if (name.trim() == "") {
        nameRequiredObj.show();
        issues++;
    }

    if (email.trim() == "") {
        emailRequiredObj.show();
        issues++;
    }

    var isValidEmail = validEmail( email.trim() );
    if (isValidEmail == "") {
        emailFormatRequiredObj.show();
        issues++;
    }

    if (message.trim() == "") {
        messageRequiredObj.show();
        issues++;
    }

    if (issues == 0) {
        hideRequiredMessages();
    }

    return (issues == 0);
}

function validEmail(v) {
    var r = new RegExp("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?");
    return (v.match(r) == null) ? false : true;
}

function registerObjects() {

    nameObj = $('#txt_name')
    emailObj = $('#txt_email')
    messageObj = $('#txt_message')

    nameRequiredObj = $('#name_required')
    emailRequiredObj = $('#email_required')
    messageRequiredObj = $('#message_required')
    emailFormatRequiredObj = $('#email_format_required')

    contactFormObj = $('#contactForm')
    securityTokenObj = $('input[name=csrfmiddlewaretoken]')
}

function hideRequiredMessages() {
    nameRequiredObj.hide();
    emailRequiredObj.hide();
    messageRequiredObj.hide();
    emailFormatRequiredObj.hide();
}

$(document).ready(function () {

    registerObjects();
    register_events();
    hideRequiredMessages();

});