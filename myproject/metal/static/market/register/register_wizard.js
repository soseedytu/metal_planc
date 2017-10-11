$(document).ready(function () {

    hideSupplierSteps();

    var chkRegAsSup = $('#chkRegisterAsSupplier');
    chkRegAsSup.on('click', function(e){
        var isChecked = chkRegAsSup.prop('checked');
        isRegisterAsSupplier = isChecked;

        if(isRegisterAsSupplier)
        {
            showAllSteps();
        }
        else
        {
            hideSupplierSteps();
        }
    });

    //Initialize tooltips
    $('.nav-tabs > li a[title]').tooltip();

    //Wizard
    $('a[data-toggle="tab"]').on('show.bs.tab', function (e) {

        var $target = $(e.target);

        if ($target.parent().hasClass('disabled')) {
            return false;
        }
    });

    $(".next-step").click(function (e) {

        var $active = $('.wizard .nav-tabs li.active');

        if(isRegisterAsSupplier)
        {
            $active.next().removeClass('disabled');
            nextTab($active);
        }
        else {
            $active.parent().children().last().removeClass('disabled');
            lastTab($active);
        }

    });
    $(".prev-step").click(function (e) {

        var $active = $('.wizard .nav-tabs li.active');

        if(isRegisterAsSupplier)
        {
            prevTab($active);
        }
        else
        {
            $active.parent().children().first().removeClass('disabled');
            first($active);
        }

    });

    // Submit post on submit
    $('#btnSubmit').on('click', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        register_user($(this));
    });
});

var isRegisterAsSupplier = false;

function hideSupplierSteps() {

    $('#iconStep2').hide();
    $('#iconStep3').hide();
    $('#iconStep4').hide();
    $('#btnNext').hide();
    $('#btnSubmit').show();

    $('.wizard .wizard-inner .nav-tabs li').css('width', '50%');
}

function showAllSteps(){

    $('#iconStep2').show();
    $('#iconStep3').show();
    $('#iconStep4').show();
    $('#btnNext').show();
    $('#btnSubmit').hide();

    $('.wizard .nav-tabs li').css('width', '20%');

}

function goToCompleteTab(elem) {
    $(elem).next().find('a[data-toggle="tab"]').click();
}

function nextTab(elem) {
    $(elem).next().find('a[data-toggle="tab"]').click();
}

function prevTab(elem) {
    $(elem).prev().find('a[data-toggle="tab"]').click();
}

function firstTab(elem) {
    $(elem).parent().children().first().find('a[data-toggle="tab"]').click();
}

function lastTab(elem) {
    $(elem).parent().children().last().find('a[data-toggle="tab"]').click();
}

function register_user(form) {
    console.log("create post is working!") // sanity check

    // Collect Data

    var frmData = {
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(), // essential data
        the_post : $('#post-text').val()
    };

    // Save

    $.ajax({
        url : form.prop('action'), // the endpoint
        type : "POST", // http method
        data : frmData, // data sent with the post request

        // handle a successful response
        success : function(json) {
            // remove the value from the input

            // move to last anchor
            $('#completeAnchor').removeClass('disabled');
            $('#completeAnchor').click();

            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};