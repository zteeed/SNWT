<?php

function get_hosting_info() {
  include('database_conn.php');
  $query = "SELECT adherent_id, lxc_id, domaine_name, email 
            FROM lxc JOIN auth_user ON auth_user.id=lxc.adherent_id;";
  $result = pg_query($conn, $query);
  $arr = pg_fetch_all($result);
  pg_close($conn);
  return $arr;
}

?>
