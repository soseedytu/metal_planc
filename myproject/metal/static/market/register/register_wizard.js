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

        console.log($(".select2").val());

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

    // Get Service
    $(document).on('click', '.chk_service', function (){
    //$('.chk_service').on('click', function(event) {
        update_Next_Level_Services($(this));
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

//  get service by id
//  1
function update_Next_Level_Services(source_checkbox){
    var ischecked = source_checkbox.prop('checked');
    var serviceId = source_checkbox.val();
    var renderin = source_checkbox.data('renderin');
    var parentText = source_checkbox.data('parenttext');
    var thisText = source_checkbox.data('thistext');
    var thisStep = source_checkbox.data('step');

    if(thisStep == 4) return false; // if final step do not do ajax call

    if(ischecked) {
        // load data and upload
        $.ajax({
            url: '/supplier/service/' + serviceId, // the endpoint
            type: "GET", // http method

            // handle a successful response
            success: function (json) {
                // move to last anchor
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check

                update_destination_element(renderin, json, parentText, thisText, thisStep, serviceId);
            },

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }else{
        // remove next level
        $('.child-of-' + serviceId).detach();
    }

}

function update_destination_element(elementId, json, parentText, thisText, thisStep, serviceId) {

    var nextStep = thisStep + 1;

    var textSeparator = '';
    if(parentText != ''){
        textSeparator = ' > ';
    }

    var targetElement = $('#' + elementId);
    //targetElement.empty();

    var containerOpening = '<div class="box box-solid box-default child-of-'+ serviceId +'">\n' +
        '            <div class="box-header with-border">\n' +
        '              <h3 class="box-title">'+ parentText + textSeparator + thisText +'</h3>\n' +
        '            </div>\n' +
        '            <!-- /.box-header -->\n' +
        '            <div class="box-body">';
    var containerClosing = '</div>\n' +
        '            <!-- /.box-body -->\n' +
        '          </div>';

    var openingElement = '<div class="form-group"><label>';
    var closingElement = '</label></div>';
    var finalElment = containerOpening;

    json.forEach(function(element) {
        // console.log(element.Id);
        // console.log(element.Service_Name);

        var checkboxElement = '<input ' +
            'class="chk_service" ' +
            'data-thistext="'+ element.Service_Name +'" ' +
            'data-parenttext="'+ thisText +'" ' +
            'data-renderin="step4_list" ' +
            'data-step="'+ nextStep +'" ' +
            'type="checkbox" ' +
            'value="'+ element.Id +'" /> ' +
            element.Service_Name;

        finalElment = finalElment + openingElement + checkboxElement + closingElement;

    });

    finalElment = finalElment + containerClosing;

    targetElement.append(finalElment);

}

