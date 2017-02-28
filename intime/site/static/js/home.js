require([
    'jquery',
    'utils/renderer'
], function($, $R) {
    var avatar = 'https://freeiconshop.com/wp-content/uploads/edd/person-flat.png';

    var profile = new $R({
        container : $('.nav-chip-container'),
        template : $('#nav-chip-template').html(),
        auto_activate: true,
        data: {
            full_name: "Kev Cal",
            avatar_url: avatar
        },
        callback: function (template) {
            var $template = $(template);
            $template.find('.logout').on('click', function() {
                console.log('fuck it');
            });
        }
    });

    var clock = clock || {
        el: {
            clock: document.getElementById('clock')
        },

        init: function () {
            setInterval(this.update, 1000);
        },
        update: function () {
            var d = new Date(),
            h = strPad(d.getHours()),
            m = strPad(d.getMinutes());
            s = strPad(d.getSeconds());

            clock.el.clock.innerHTML = h + ':' + m + '<span> :' + s +'</span>';
        }
    }

    function strPad(n) {
        return String("00" + n).slice(-2);
    }
    $(function () {
        clock.init();
    });
});
