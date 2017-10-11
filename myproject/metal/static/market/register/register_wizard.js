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
});

var isRegisterAsSupplier = false;

function hideSupplierSteps() {

    $('#iconStep2').hide();
    $('#iconStep3').hide();
    $('#iconStep4').hide();

}

function showAllSteps(){

    $('#iconStep2').show();
    $('#iconStep3').show();
    $('#iconStep4').show();

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