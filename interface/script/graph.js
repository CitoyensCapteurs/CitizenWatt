
var URL = 'test.json'
  , MAX_POWER = 2500
  , UPDATE_TIMEOUT = 2000 // En millisecondes
  ;

(function(){
	
	var graph = document.getElementById('graph_values')
	  , now = document.getElementById('now')
	  , day = document.getElementById('day')
	  , sum = 0
	  , n_values = 0
	  , mean
	  , size = 12 // @keyframes slidein
	  , border = 2 // #graph_values .rect
	  ;
	
	function addRect(power) {
		var height = power / MAX_POWER * 100;
		var div = document.createElement('div');
		var blank = document.createElement('div');
		var color = document.createElement('div');
		graph.appendChild(div);
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
		now.innerHTML = power + 'W';

		++n_values;
		sum += power;
		mean = sum / n_values;
		var height = mean / MAX_POWER * 100;
		var color_class = (height > 33.3 ? (height >= 66.7 ? 'red' : 'orange') : 'yellow');
		day.className = 'blurry ' + color_class;
		day.innerHTML = Math.floor(mean) + 'W';

	}

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

		setTimeout(update, UPDATE_TIMEOUT);
	}

	update();

	
})();



