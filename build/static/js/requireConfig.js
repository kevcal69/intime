requirejs.config({
    baseUrl: '/assets/js',
    paths: {
        jquery: 'lib/jquery/jquery-3.1.1.min',
        mustache: 'lib/mustache/mustache.min'
    },
    shim: {
        'jquery': {
            deps: [],
            exports: 'jquery'
        },
    }
});
