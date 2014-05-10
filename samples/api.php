<?php
	$api_keys = array('serie'=>'Serie');
function sort_array(&$array, $key) {
    $sort_keys = array();

    foreach ($array as $key2 => $entry) {
        $sort_keys[$key2] = $entry[$key];
    }


    return array_multisort($sort_keys, SORT_DESC, $array);
}

// ==========
// Paramètres
// ==========
    // Capteurs
    $keys = array();
    if(!empty($_GET['capteur'])) {
        foreach(explode(',', $_GET['capteur']) as $capteur) {
            $keys[array_search($capteur, $api_keys)] = $capteur;
        }
    }
    else {
        $keys = $api_keys;
    }

// Récupération des données
    $data = array();
    foreach($keys as $key=>$capteur) {
        if(file_exists($key.'.data')) {
            $data[$capteur] = json_decode(gzinflate(file_get_contents($key.'.data')), true);
        }
    }

// Tri par timestamp
foreach($keys as $key=>$capteur) {
    sort_array($data[$capteur], 'timestamp');
}

if(!empty($_GET['n'])) {
	foreach($data as $key=>$value) {
		$data[$key] = array_slice($data[$key], 0, intval($_GET['n']));
	}
}

// Envoi des données
        file_put_contents('sample3', json_encode($data));
    exit();
