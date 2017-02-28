define(function (require) {

    var $ = require('jquery');
    var Mustache = require('mustache');

    var Renderer = function (params) {
        this.template = params.template;
        this.data = params.data || {};
        this.container = params.container || $(document);
        this.alwaysClean = params.clean || false;
        this.callback = params.callback;
        this.templateid = params.templateid;
        if (params.auto_activate) {
            this.activate(this.alwaysClean);
        }
    }

    Renderer.prototype.activate = function (clean) {
        this.alwaysClean = clean || this.alwaysClean;
        var renderedTemplate = Mustache.render(this.template, this.data);
        if (this.alwaysClean) {
            this.container.empty();
        }

        this.container.append(renderedTemplate);
        if (this.callback) {
            this.callback(renderedTemplate);
        }
    }

    Renderer.prototype.deactivate = function () {
        this.container.find(this.template).remove();
    }

    return Renderer;
});
