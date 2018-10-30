function show_ports(base64_data) {
  var data_json = atob(base64_data);
  var data_array = JSON.parse(data_json)
  var msg = '';
  data_array.forEach(function(element) {
    msg=msg.concat('Port ');
    msg=msg.concat(element["port"]);
    msg=msg.concat('\t\t');
    msg=msg.concat(element["state"]);
    msg=msg.concat('\t\t');
    msg=msg.concat(element["name"]);
    msg=msg.concat('\n');
  });
  alert(msg);
}
