
(function(){
	
	var graph = document.getElementById('graph')
	  , size = 12
	  , border = 2
	  ;
	
	function addRect(nth, height) {
		var div = document.createElement('div');
		graph.appendChild(div);
		div.className = 'rect ' + (height > 33.3 ? (height >= 66.7 ? 'red-day' : 'orange-day') : 'yellow-day');
		div.style.width = size + 'px';
		div.style.left = border + ((size + border) * nth) + 'px';
		div.style.height = height + '%';
	}
	
	for (var i = 0 ; i < 50 ; i++) {
		addRect(i, 40 * (Math.sin(i/1.) + 1.1));
	}
	
})();



