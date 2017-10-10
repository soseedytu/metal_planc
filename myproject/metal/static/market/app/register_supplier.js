//Encoding UTF8
var vm = (function () {
    var countryText = ko.observable(null);
    var selectedCountry = ko.observable();

    var countryList = [
         { code: 'IS', name: 'Iceland', localName: 'Ísland' },
         { code: 'GB', name: 'Great Britain', localName: '' },
         { code: 'US', name: 'USA', localName: '' },
         { code: 'AE', name: 'UNITED ARAB EMIRATES', localName: 'دولة الإمارات العربية المتحدة' },
         { code: 'IE', name: 'IRELAND', localName: 'Éire' },
         { code: 'IL', name: 'ISRAEL', localName: 'מְדִינַת יִשְׂרָאֵל' },
         { code: 'IM', name: 'ISLE OF MAN', localName: 'Ellan Vannin' },
         { code: 'IQ', name: 'BRITISH INDIAN OCEAN TERRITORY', localName: 'Chagos Islands' },
         { code: 'JP', name: 'JAPAN', localName: '' }
    ];

    var vm = {
        countryText: countryText,
        selectedCountry: selectedCountry,
        countryList: countryList,
    };
    return vm;
})();

vm.selectedCountry.subscribe(function () {
    //Example on how we can use subscription to update data on our bound data, not that we actually need it for this example but include it to show how it is done.
    vm.countryText((vm.selectedCountry() ? (vm.selectedCountry().localName ? vm.selectedCountry().localName : vm.selectedCountry().name) : ''));
}, vm);

//Preset the first country in the list as the selected datum, showing of the two-way binding to the control
this.vm.selectedCountry(vm.countryList[0]);

ko.applyBindings(vm);