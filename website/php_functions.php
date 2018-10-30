<?php

/* Adhérents/Développement/Production Functions */

function get_scan_info($table) {
  include('database/database_conn_localhost.php');
  $query = "SELECT c.id as catégorie_id, p.id as plages_ip_id, 
                   r.id as résultat_scan_id, c.name as catégorie, 
                   p.ip_mask, r.ip, r.port, r.state, r.name 
                   FROM résultat_scan AS r 
                     JOIN plages_ip as p ON p.id=r.id_plages_ip 
                     JOIN catégories AS c ON c.id=p.id_catégories 
            WHERE c.name='".$table."'
            ORDER BY r.id;";
  $result = pg_query($conn, $query);
  $arr = pg_fetch_all($result);
  pg_close($conn);
  return $arr;
}

function display_data_scan($arr) {
  $arr = group_on_ip($arr);
  foreach($arr as $host) {
    $url = "http://".$host[0]["ip"];
    $httpcode = 999;
    foreach ($host as $port) {
      if (intval($port["port"]) === 80) {
        $httpcode = http_code($url);
      }
    }
    echo '
    <div class="col-3 col-4-medium col-12-small">
      <section class="box style1">
        <span class="icon featured '.icon_up_down($httpcode).'"></span>
        <h3>'.$host[0]["ip"].'</h3>
        <p></p>
        <ul>
	';
        $num = count($host);
        echo '<li>'.$num.' port(s) ouvert(s)</li>';
	foreach ($host as $port) {
          // echo "<li>Port:".$port["port"]."\r".$port["state"]."\r<u>".$port["name"]."</u></li>";
          if (intval($port["port"]) === 80) {
            echo '<li>HTTP Code: '.$httpcode.'</li>';
            echo '<li><a href="'.$url.'">Accéder au site</a></li>';
          }
	}
        if ($httpcode === 999) {
          echo '<li>HTTP Code: ???</li>';
          echo '<li>Aucun site web configuré</li>';
        }
    echo '	
        </ul>
      </section>
    </div>';
  }
  return;
}

function group_on_ip($arr) {
  $return = array();
  foreach($arr as $val) {
      $return[$val["ip"]][] = $val;
  }
  return $return;
}

/* Hosting Functions */

function get_hosting_info() {
  include('database/database_conn_hosting.php');
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
 else if ($httpcode == 999) { 
   return "fa-question"; 
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
