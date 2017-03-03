require([
    'jquery',
    'utils/renderer',
    'utils/clock',
    'utils/cookie'
], function($, $R, clock, cookie) {
    var avatar = 'https://freeiconshop.com/wp-content/uploads/edd/person-flat.png';

    var profile = new $R({
        container : $('.nav-chip-container'),
        template : $('#nav-chip-template').html(),
        auto_activate: true,
        data: {
            full_name: "Kev Cal",
            avatar_url: avatar
        }
    });
    var lastRec = vars.content.records.slice(-1)[0] || {};
    lastRec = (lastRec.active)? lastRec : {};
    console.log(lastRec);
    var timecard = new $R({
        container : $('.timecard'),
        template : $('#timecard').html(),
        auto_activate: true,
        data: {
            today: lastRec.in,
            total: "",
            uuid: lastRec.uuid,
            active: lastRec.active
        },
        callback: function (template) {
            clock();
            $(this.container).on('click', '.time' ,function(e) {
                var uuid = $(this).data('uuid');
                $.ajax({
                    type: "POST",
                    data: {
                        csrfmiddlewaretoken: cookie('csrftoken'),
                        uuid: uuid
                    },
                    url: "/timein",
                    success: function (code) {
                        console.log(code);
                    }
                });
            });
            var logContainer = $(".logs")
            vars.content.records.forEach(function(obj) {
                logContainer.append(
                    "<tr class="+(obj.active || "")+">" +
                        "<td>" + obj.uuid + "</td>" +
                        "<td>" + (obj.time || "----") + "</td>" +
                        "<td>" + obj.in + "</td>" +
                        "<td>" + (obj.out || "-------") + "</td>" +
                    "</tr>"
                );
            });
        }
    });

});
