<?php

function get_hosting_info() {
  $query = "select lxc_id, domaine_name, email from lxc JOIN auth_user ON auth_user.id=lxc.adherent_id;";
  return $arr;
}

?>
