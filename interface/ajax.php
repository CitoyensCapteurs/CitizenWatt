<?php
if(is_file('last')) {
    $last_id = file_get_contents('last');
}
else {
    $last_id = -1;
}

$dbh = new PDO('mysql:host=localhost;dbname=citizenwatt', 'root', 'toto');

$data = array()

foreach($dbh->query('SELECT * from values WHERE id > '.$last_id.' ORDER BY id DESC') as $row) {
    $data[] = array('power' => $row['power']);
}

exit(json_encode($data));
