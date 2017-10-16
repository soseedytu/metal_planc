var vmRegistration = ko.validatedObservable({

    company_uen: ko.observable('').extend({ required: true, number: true}), // txt_company_uen
    company_name: ko.observable('').extend({ required: true }), // txt_company_name
    contact_number: ko.observable('').extend({ required: true }), // txt_contact_number
    tags: ko.observable([]).extend({ required: false }), //
    user_name: ko.observable('').extend({ required: true }), // txt_user_name
    title: ko.observable('').extend({ required: true }), // txt_job_title
    email_address: ko.observable('').extend({ required: true, email: true }), // txt_email_addr
    password: ko.observable('').extend({ required: true }), // txt_password
    services: ko.observable([]).extend({ required: false }), //
    register_as_supplier: ko.observable(false)

});

var vmLevel1Elements = function(){
    this.service_Id = ko.observable('');
    this.service_Name = ko.observable('');
    this.parent_Id = ko.observable('');
    this.level = ko.observable(0);

    // Whenever the category changes, reset the product selection
    this.service_Id.subscribe(function() {
        self.product(undefined);
    });
};

$(document).ready(function () {
    // enable validation
    ko.validation.init();
    // bind view model to form
    ko.applyBindings(vmRegistration);

    // show all error messages
    var result = ko.validation.group(vmRegistration, {deep: true});
    vmRegistration.isValid();
    result.showAllMessages(true);

    hideSupplierSteps();

    var chkRegAsSup = $('#chkRegisterAsSupplier');
    chkRegAsSup.on('click', function (e) {
        var isChecked = chkRegAsSup.prop('checked');
        isRegisterAsSupplier = isChecked;

        if (isRegisterAsSupplier) {
            showAllSteps();
        }
        else {
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

        register_form_validation();

        var isSubmitButton = $(this).data('issubmitbutton');

        if (isSubmitButton == 1) return false;

        showNextStep();

    });
    $(".prev-step").click(function (e) {

        var $active = $('.wizard .nav-tabs li.active');

        if (isRegisterAsSupplier) {
            prevTab($active);
        }
        else {
            $active.parent().children().first().removeClass('disabled');
            first($active);
        }

    });

    // Get Service
    $(document).on('click', '.chk_service', function () {
        //$('.chk_service').on('click', function(event) {
        update_Next_Level_Services($(this));
    });

    // Submit post on submit
    $('.btnSubmit').on('click', function (event) {
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        register_user($(this));
    });


    // register validation
    register_form_validation();
});

var isRegisterAsSupplier = false;

function showNextStep() {
    var $active = $('.wizard .nav-tabs li.active');

    if (isRegisterAsSupplier) {
        $active.next().removeClass('disabled');
        nextTab($active);
    }
    else {
        $active.parent().children().last().removeClass('disabled');
        lastTab($active);
    }
}

function hideSupplierSteps() {

    $('#iconStep2').hide();
    $('#iconStep3').hide();
    $('#iconStep4').hide();
    $('#btnNext').hide();
    $('#btnSubmit').show();

    $('#selTags').hide();

    $('.wizard .wizard-inner .nav-tabs li').css('width', '50%');
}

function showAllSteps() {

    $('#iconStep2').show();
    $('#iconStep3').show();
    $('#iconStep4').show();
    $('#btnNext').show();
    $('#btnSubmit').hide();

    $('#selTags').show();

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
    var data = collect_form_data()
    console.log(data);

    var result = register_form_validation(); //validate_form();

    console.log(result);


    var isValid = vmRegistration.isValid();

    if(isValid == false)
    {
        alert('Please fix errors in registration data.')
        return false;
    }

    showNextStep();

    data.csrfmiddlewaretoken =  $('input[name=csrfmiddlewaretoken]').val();

    // Save

    $.ajax({
        url: form.prop('action'), // the endpoint
        type: "POST", // http method
        data: data, // data sent with the post request

        // handle a successful response
        success: function (json) {
            // remove the value from the input

            // move to last anchor
            $('#completeAnchor').removeClass('disabled');
            $('#completeAnchor').click();

            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

//  get service by id
//  1
function update_Next_Level_Services(source_checkbox) {
    var ischecked = source_checkbox.prop('checked');
    var serviceId = source_checkbox.val();
    var renderin = source_checkbox.data('renderin');
    var parentText = source_checkbox.data('parenttext');
    var thisText = source_checkbox.data('thistext');
    var thisStep = source_checkbox.data('step');

    if (thisStep == 4) return false; // if final step do not do ajax call

    if (ischecked) {
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
    } else {
        // remove next level
        $('.child-of-' + serviceId).detach();
    }

}

function update_destination_element(elementId, json, parentText, thisText, thisStep, serviceId) {

    var nextStep = thisStep + 1;

    var textSeparator = '';
    if (parentText != '') {
        textSeparator = ' > ';
    }

    var targetElement = $('#' + elementId);
    //targetElement.empty();

    var containerOpening = '<div class="box box-solid box-default child-of-' + serviceId + '">\n' +
        '            <div class="box-header with-border">\n' +
        '              <h3 class="box-title">' + parentText + textSeparator + thisText + '</h3>\n' +
        '            </div>\n' +
        '            <!-- /.box-header -->\n' +
        '            <div class="box-body">';
    var containerClosing = '</div>\n' +
        '            <!-- /.box-body -->\n' +
        '          </div>';

    var openingElement = '<div class="form-group"><label>';
    var closingElement = '</label></div>';
    var finalElment = containerOpening;

    json.forEach(function (element) {
        // console.log(element.Id);
        // console.log(element.Service_Name);

        var checkboxElement = '<input ' +
            'class="chk_service" ' +
            'data-thistext="' + element.Service_Name + '" ' +
            'data-parenttext="' + thisText + '" ' +
            'data-renderin="step4_list" ' +
            'data-step="' + nextStep + '" ' +
            'type="checkbox" ' +
            'value="' + element.Id + '" /> ' +
            element.Service_Name;

        if (element.Parent_Service__Id != undefined && nextStep == 4) {
            var startRow = "<div class='row'>";
            var endRow = "</div>";

            var widthCtl = "<div class='col-md-3'><label>supported width</label><input id='txt_min_width_" + element.Id + "' type='input' placeholder='min width' title='Please provide min width that you can support.' /><input id='txt_max_width_" + element.Id + "' type='input' placeholder='max width' title='Please provide max width that you can support.' /></div>";
            var heightCtl = "<div class='col-md-3'><label>supported height</label><input id='txt_min_height_" + element.Id + "' type='input' placeholder='min height' title='Please provide min height that you can support.' /><input id='txt_max_height_" + element.Id + "' type='input' placeholder='max height' title='Please provide max height that you can support.'  /></div>";
            var thicknessCtl = "<div class='col-md-3'><label>supported thickness</label><input id='txt_min_thickness_" + element.Id + "' type='input' placeholder='min thickness' title='Please provide min thickness that you can support.' /><input id='txt_max_thickness_" + element.Id + "' type='input' placeholder='max thickness' title='Please provide max thickness that you can support.' /></div>";

            checkboxElement = "<div class='col-md-3'>" + checkboxElement + "</div>";
            checkboxElement = startRow + checkboxElement;
            checkboxElement = checkboxElement + widthCtl + heightCtl + thicknessCtl;
            checkboxElement = checkboxElement + endRow;

        }


        finalElment = finalElment + openingElement + checkboxElement + closingElement;
        finalElment = finalElment + "<hr style='border-bottom: 1px solid gray'/>";

    });

    finalElment = finalElment + containerClosing;

    targetElement.append(finalElment);

}

function collect_form_data() {

    var data = ko.toJS(vmRegistration);

    // data.company_uen = ''; // txt_company_uen
    // data.company_name = ''; // txt_company_name
    // data.contact_number = ''; // txt_contact_number
    data.tags = $(".select2").val(); //
    // data.user_name = ''; // txt_user_name
    // data.job_title = ''; // txt_job_title
    // data.email_address = ''; // txt_email_addr
    // data.password = ''; // txt_password
    data.services = []; //
    // data.register_as_supplier = $('#chkRegisterAsSupplier').prop('checked');

    var step4_checkboxes = $('*[data-step="4"]');

    step4_checkboxes.each(function (i, element) {

        if (element.checked) {
            var id = element.value;

            var minWidth = $('#txt_min_width_' + id).val();
            var minHeight = $('#txt_min_height_' + id).val();
            var minThickness = $('#txt_min_thickness_' + id).val();
            var maxWidth = $('#txt_max_width_' + id).val();
            var maxHeight = $('#txt_max_height_' + id).val();
            var maxThickness = $('#txt_max_thickness_' + id).val();

            var supplier_svs = {
                service_id: id,
                min_width: minWidth,
                min_height: minHeight,
                min_thickness: minThickness,
                max_width: maxWidth,
                max_height: maxHeight,
                max_thickness: maxThickness,
            };

            data.services.push(supplier_svs);
        }

    });

    return data;

}

function register_form_validation() {
    console.log(ko.toJS(vmRegistration));
    return vmRegistration.isValid();
}