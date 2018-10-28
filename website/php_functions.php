<?php

/* Adhérents Functions */

/* Hosting Functions */

function get_hosting_info() {
  include('database_conn_hosting.php');
  $query = "SELECT adherent_id, lxc_id, domaine_name, email 
            FROM lxc JOIN auth_user ON auth_user.id=lxc.adherent_id
            ORDER BY date_created DESC;";
  $result = pg_query($conn, $query);
  $arr = pg_fetch_all($result);
  pg_close($conn);
  return $arr;
}

function icon_up_down($httpcode) {
 if($httpcode == 200 || $httpcode == 302) {
   return "fa-check"; 
 }
 else { 
  return "fa-times"; 
 }
}

function http_code($url) {
  $handle = curl_init($url);
  curl_setopt($handle,  CURLOPT_RETURNTRANSFER, TRUE);
  // curl_setopt($handle, CURLOPT_CONNECTTIMEOUT, 1); 
  curl_setopt($handle, CURLOPT_TIMEOUT_MS, 100);
  $response = curl_exec($handle);
  $httpCode = curl_getinfo($handle, CURLINFO_HTTP_CODE);
  curl_close($handle);
  if ($httpCode===0) { $httpCode = 504; }
  return $httpCode;
}

function display_data_hosting($arr) {
  foreach($arr as $item) {
    $url = "https://".$item["domaine_name"].".hosting.minet.net";
    $httpcode = http_code($url);
    echo '
    <div class="col-3 col-4-medium col-12-small">
      <section class="box style1">
        <span class="icon featured '.icon_up_down($httpcode).'"></span>
        <h3>'.$item["domaine_name"].'</h3>
        <p></p>
        <ul>
          <!--
          <li>ADH ID: '.$item["adherent_id"].'</li>
          <li>LXC ID: '.$item["lxc_id"].'</li>
          -->
          <li>HTTP Code: '.$httpcode.'</li>
          <li><a href="'.$url.'">Accéder au site</a></li>
          <li><a href="mailto:'.$item["email"].'">Envoyer un email</a></li>
        </ul>
      </section>
    </div>';
  }
} 

?>
