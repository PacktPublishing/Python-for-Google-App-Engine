(function (window) {
  "use strict";

  // create a channel and connect the socket
  var setupChannel = function(token) {
    var channel = new goog.appengine.Channel(token);
    var socket = channel.open();

    socket.onopen = function() {
      console.log('Channel opened!');
    };

    socket.onmessage = function (msg) {
      window.alert(msg.data);
    };

    socket.onerror = function(err) {
      // reconnect on timeout
      if (err.code == 401) {
        init();
      }
    };

    socket.onclose = function() {
      console.log('goodbye');
    };
  };

  // get channel token from the backend and connect
  var init = function() {
    var tokenReq = new XMLHttpRequest();
    tokenReq.onload = function () {

      var token = JSON.parse(this.responseText).token;
      setupChannel(token);

    };
    tokenReq.open("get", "/notify_token", true);
    tokenReq.send();
  };

  init();

}(this));
