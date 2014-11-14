'use strict';

var events = require('./events.js');

var entityMap = {
    'candidates': 'candidate',
    'committees': 'committee'
};

var callAPI = function(url) {
    return $.ajax({
        url: url,
        success: function(data) {
            console.log(data);
        }
    });
};

var buildURL = function(e) {
    var URL = 'rest/' + entityMap[e.category] + '?';
    for (field in e.filters) {
        if (e.filters.hasOwnProperty(field)) {
            URL += field + '=' + e.filters[field] + '&'
        }
    }

    return URL;
};

var filterLoadHandler = function(e) {
    var url = buildURL(e),
        promise = callAPI(url);

    promise.done(function(data) {
        e.data = data;
        events.emit('render:browse', e);
    });
};

module.exports = {
    init: function() {
        events.on('search:submitted', function(e) {
            var entities = [],
                promises = [],
                i, 
                len,
                entity;

            for (entity in entityMap) {
                if (entityMap.hasOwnProperty(entity)) {
                    entities.push(entityMap[entity]);
                }
            }

            len = entities.length;

            for (i = 0; i < len; i++) {
                promises.push(callAPI('rest/' + entities[i] + '?q=' + encodeURIComponent(e.query) + '&per_page=5'));
            }


            $.when.apply($, promises).done(function() {
                var i,
                    len = arguments.length;
                e.results = {};

                for (i = 0; i < len; i++) {
                    e.results[entities[i]] = arguments[i][0].results;   
                }

                events.emit('render:search', e);
            });
        });

        events.on('load:browse', function(e) {
            var promise = callAPI('rest/' + entityMap[e.category]);

            promise.done(function(data) {
                e.data = data;
                events.emit('render:browse', e);
            });
        });

        events.on('selected:filter', filterLoadHandler);
        events.on('removed:filter', filterLoadHandler);
        events.on('nav:pagination', filterLoadHandler);
    },

    // for unit tests
    buildURL: buildURL
};
