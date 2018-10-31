function show_ports(base64_data) {
  var data_json = atob(base64_data);
  var data_array = JSON.parse(data_json)
  var msg = '<br /><ul>';
  data_array.forEach(function(element) {
    msg=msg.concat('<li>Port ');
    msg=msg.concat(element["port"]);
    msg=msg.concat('\t\t');
    msg=msg.concat(element["state"]);
    msg=msg.concat('\t\t');
    msg=msg.concat(element["name"]);
    msg=msg.concat('</li>');
  });
  msg=msg.concat('</ul>');
  swal({
    title: '<strong>Liste des port(s) ouvert(s)</strong>',
    type: 'info',
    html:
      msg,
    showCloseButton: true,
    showCancelButton: false,
    focusConfirm: false,
    confirmButtonText:
      '<i class="fa fa-thumbs-up"></i> OK!',
    confirmButtonAriaLabel: 'Thumbs up, great!',
  })
}
