requirejs([
    'jquery',
    'site/utils/renderer',
], function ($, Render) {
        var variables = window.vars;
        var profile = new Render({
            container : $('.container-section'),
            template : $('#widget-template').html(),
            templateid: '#profile',
            auto_activate: true,
            data: {
                'fullname': variables.user.fname + ' ' + variables.user.lname
            },
            callback: function (template) {

            }
        });
    }
);
