Common = {};

Common.bindUniversalSearchLookup = function () {
    // Reset universal search input due to chrome autofilling the text field
    // on back button
    $("#universal-search").val('');
    var self = this;
    self.isTypeaheadOpen = false;
    $.typeahead({
      input: "#universal-search",
      minLength: 0,
      maxItem: 0,
      order: "asc",
      dynamic: true,
      delay: 500,
      highlight: "any",
      display: [
          "path",
      ],
      template: function(query, item) {
        return ('<span>' + item.name + '</span>')
      },
      source: {
        users: {
          url: {
            type: "GET",
            url: '/autocomplete-query/',
            xhrFields: {
              withCredentials: true
            },
            data: {
              q: "{{query}}",
            }
          }
        }
      },
      callback: {
        onClickAfter: function (node, a, item, event) {
          self.isTypeaheadOpen = false;
          window.location.href = '/download-photo/' + item.id;
          $("#universal-search").val('');
        },
      }
    });
};


$(document).ready(function() {
  // Highlight in the navigation bar the active menu item.
  var path = window.location['pathname'];
  if (path == '/') {
    $('ul.navbar-nav li.home').addClass('active');
  } else if (path.substring(0, 19) == '/photologue/gallery') {
    $('ul.navbar-nav li.galleries').addClass('active');
  } else if (path.substring(0, 17) == '/photologue/photo') {
    $('ul.navbar-nav li.photos').addClass('active');
  }
  Common.bindUniversalSearchLookup();
});
