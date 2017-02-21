requirejs([
    'jquery',
    'site/utils/renderer',
], function ($, Render) {

        var login = new Render({
            container : $('.container-section'),
            template : $('#login-template').html(),
            templateid: '#login'
        });

        login.activate();
    }
);
