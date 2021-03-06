
var URL = 'ajax.php'
  , MAX_POWER = 3500
  , UPDATE_TIMEOUT = 2000 // En millisecondes
  ;
var start_time= Math.round((new Date().getTime()) / 1000);

(function(){

	var graph = document.getElementById('graph')
	  , graph_vertical_axis = document.getElementById('graph_vertical_axis')
	  , graph_values = document.getElementById('graph_values')
	  , now = document.getElementById('now')
	  , day = document.getElementById('day')
	  , sum = 0
	  , n_values = 0
	  , mean
	  , size = 12 // @keyframes slidein
	  , border = 2 // #graph_values .rect
	  ;

    function kWh_to_euros(energy) {
        return Math.round(100*(0.2317 + (0.1367 * energy)))/100;
    }

	function addRect(power) {
		var height = parseInt(power) / MAX_POWER * 100;
		var div = document.createElement('div');
		var blank = document.createElement('div');
		var color = document.createElement('div');
		graph_values.appendChild(div);
		div.appendChild(blank);
		div.appendChild(color);

		div.className = 'rect';
		div.style.width = size + 'px';

		var color_class = (height > 33.3 ? (height >= 66.7 ? 'red' : 'orange') : 'yellow');
		color.className = 'color ' + color_class + '-day';
		color.style.width = size + 'px';
		color.style.height = height + '%';

		blank.className = 'blank';
		blank.style.width = size + 'px';
		blank.style.height = (100 - height) + '%';

		now.className = 'blurry ' + color_class;
		now.innerHTML = Math.floor(power) + 'W';

		++n_values;
		sum += parseInt(power);
		total = sum * UPDATE_TIMEOUT / 3600 / 1000000;
		height = total / MAX_POWER * 100;
		color_class = (height > 33.3 ? (height >= 66.7 ? 'red' : 'orange') : 'yellow');
		day.className = 'blurry ' + color_class;
        var timestamp = Math.round((new Date().getTime()) / 1000);
		day.innerHTML = Math.round(total * 1000)/1000 + 'kWh (' + kWh_to_euros(total)+'€)';

		var max_values = Math.floor(graph.clientWidth / (size + border));
		if (n_values >= max_values) {
			graph_values.removeChild(graph_values.firstChild)
		}

	}


	function addVerticalGraduation(power) {
		var height = parseInt(power) / MAX_POWER * 100;
		var span = document.createElement('span');
		graph_vertical_axis.appendChild(span);

		span.style.bottom = height + '%';
		span.innerHTML = power + "W";
	}

	addVerticalGraduation(MAX_POWER * 0.00);
	addVerticalGraduation(MAX_POWER * 0.33);
	addVerticalGraduation(MAX_POWER * 0.66);
	addVerticalGraduation(MAX_POWER * 1.00);

	var req = new XMLHttpRequest();
	function update() {
		req.open('GET', URL, true);
		req.send();
		req.onreadystatechange = function() {
	        if (req.readyState == 4) {
	            var data = JSON.parse(req.responseText);
	            for(var i = 0 ; i < data.length ; ++i) {
	            	addRect(data[i].power);
	            }
	        }
	    }
	// Uncomment for debugging
        // addRect(Math.random() * MAX_POWER);

		setTimeout(update, UPDATE_TIMEOUT);
	}

	update();


})();



