#!/usr/bin/node
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.com/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  });
});