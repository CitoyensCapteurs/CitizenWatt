<?php
$mysql_host = "localhost";
$mysql_db = "citizenwatt";
$mysql_user = "";
$mysql_pass = "";

if(is_file('last')) {
    $last_id = file_get_contents('last');
}
else {
    $last_id = -1;
}
$last_id = (int) $last_id;

$dbh = new PDO('mysql:host='.$mysql_host.';dbname='.$mysql_db, $mysql_user, $mysql_pass);

$data = array();

$query = $dbh->query('SELECT id, time, power FROM measures WHERE id > '.$last_id.' ORDER BY id DESC');
foreach($query->fetchAll() as $row) {
    if(empty($data)) { $last_id = $row['id']; }
    $data[] = array('power' => $row['power']);
}

file_put_contents('last', $last_id);

exit(json_encode($data));
