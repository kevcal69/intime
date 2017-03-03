define(
    ['jquery'],
    function ($) {
    //Do setup work here
    var clock = clock || {
        init: function () {
            setInterval(clock.update, 1000);
        },
        update: function () {
            var d = new Date(),
            h = strPad(d.getHours()),
            m = strPad(d.getMinutes());
            s = strPad(d.getSeconds());
            var clock = $('#clock');
            clock.html( h + ':' + m + '<span> :' + s +'</span>');
        }
    }

    function strPad(n) {
        return String("00" + n).slice(-2);
    }
    return clock.init;
});
