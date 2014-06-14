
(function(){
	
	var graph = document.getElementById('graph_values')
	  , size = 12 // @keyframes slidein
	  , border = 2 // #graph_values .rect
	  ;
	
	function addRect(nth, height) {
		var div = document.createElement('div');
		var blank = document.createElement('div');
		var color = document.createElement('div');
		graph.appendChild(div);
		div.appendChild(blank);
		div.appendChild(color);

		div.className = 'rect';
		div.style.width = size + 'px';

		color.className = 'color ' + (height > 33.3 ? (height >= 66.7 ? 'red-day' : 'orange-day') : 'yellow-day');
		color.style.width = size + 'px';
		color.style.height = height + '%';

		blank.className = 'blank';
		blank.style.width = size + 'px';
		blank.style.height = (100 - height) + '%';
	}
	
	for (var i = 0 ; i < 50 ; i++) {
		addRect(i, 40 * (Math.sin(i/1.) + 1.1));
	}

	var req = new XMLHttpRequest();
	function update() {
		req.open('GET', '[URL]', true);
		req.onreadystatechange = function() {
	        if (req.readyState == 4) {
	            var data = JSON.parse(req.responseText);
	            for(var i = 0 ; i < data.length ; ++i) {
	            	addRect(data[i].power)
	            }
	        }
	    }

		setTimeout(update, 1000);
	}

	
})();



