requirejs.config({
    baseUrl: '/assets/js',
    paths: {
        JQ: 'lib/jquery/jquery-3.1.1.min',
    },
    shim: {
        'JQuery': {
            deps: [],
            exports: 'JQuery'
        },
    }
});
