<?php

function get_hosting_info() {
  include('database_conn.php');
  $query = "SELECT adherent_id, lxc_id, domaine_name, email 
            FROM lxc JOIN auth_user ON auth_user.id=lxc.adherent_id
            ORDER BY date_created DESC;";
  $result = pg_query($conn, $query);
  $arr = pg_fetch_all($result);
  pg_close($conn);
  return $arr;
}

function display_data_hosting($arr) {
  foreach($arr as $item) {
    echo '
    <div class="col-3 col-4-medium col-6-small">
      <section class="box style1">
        <span class="icon featured fa-comments-o"></span>
        <h3>'.$item["domaine_name"].'</h3>
        <p></p>
        <ul>
          <!--
          <li>ADH ID: '.$item["adherent_id"].'</li>
          <li>LXC ID: '.$item["lxc_id"].'</li>
          -->
          <li><a href="https://'.$item["domaine_name"].'.hosting.minet.net">Accéder au site</a></li>
          <li><a href="mailto:'.$item["email"].'">Envoyer un email</a></li>
        </ul>
      </section>
    </div>';
  }
} 

?>
