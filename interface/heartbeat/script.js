

var rawLogo ='\
<?xml version="1.0" encoding="UTF-8" standalone="no"?> \
<!-- Created with Inkscape (http://www.inkscape.org/) --> \
 \
<svg \
   xmlns:dc="http://purl.org/dc/elements/1.1/" \
   xmlns:cc="http://creativecommons.org/ns#" \
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" \
   xmlns:svg="http://www.w3.org/2000/svg" \
   xmlns="http://www.w3.org/2000/svg" \
   version="1.1" \
   width="210mm" \
   height="297mm" \
   id="svg6878"> \
  <defs \
     id="defs6880" /> \
  <metadata \
     id="metadata6883"> \
    <rdf:RDF> \
      <cc:Work \
         rdf:about=""> \
        <dc:format>image/svg+xml</dc:format> \
        <dc:type \
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" /> \
        <dc:title></dc:title> \
      </cc:Work> \
    </rdf:RDF> \
  </metadata> \
  <g \
     id="root"> \
    <g \
       transform="matrix(2.6627604,0,0,-2.6627604,-430.62674,1372.6864)" \
       id="g4619" \
       style="color:#000000;fill:#ffd35d;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:1;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate"> \
      <path \
         d="m 343.281,185.348 -91.508,-11.028 -0.281,28.098 91.524,11.027 0.265,-28.097 z" \
         id="path4556" \
         style="color:#000000;fill:#ffd35d;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:1;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate" /> \
      <path \
         d="m 343.84,140.363 -91.504,-11.023 -0.285,28.09 91.523,11.023 0.266,-28.09 z" \
         id="path4558" \
         style="color:#000000;fill:#ffd35d;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:1;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate" /> \
      <path \
         d="m 299.336,338.77 c -2.035,14.011 2.348,26.503 2.348,26.503 26.558,15.583 26.414,46.852 26.648,53.27 2.57,3.953 13.246,6.328 13.246,6.328 -31.238,7.117 -44.683,-44.281 -45.398,-71.308 -1.071,-40.18 28.738,-58.551 62.902,-37.653 41.734,25.528 52.785,72.176 44.508,104.676 l 21.785,20.738 c 18.414,-50.515 -0.988,-102.828 -34.148,-127.336 -66.465,-49.117 -105.985,-5.933 -109.782,14.481 -9.617,-3.578 -18.578,-4.738 -26.14,-4.098 -14.649,1.246 -26.399,8.817 -31.469,21.098 -18.445,44.676 25.699,79.375 27.445,80.961 l 7.278,-9.317 -7.926,8.77 7.957,-8.746 c -0.305,-0.278 -36.774,-34.492 -22.973,-62.828 8.449,-17.332 34.098,-4.176 42.524,1.781 -1.86,74.945 52.55,100.93 68.793,73.539 4.339,-7.316 6.914,-55.57 -47.157,-90.531 l -0.441,-0.328 z" \
         id="path4560" \
         style="color:#000000;fill:#ffd35d;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:1;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate" /> \
      <path \
         d="m 305.863,258.863 c -58.449,1.383 -109.23,46.032 -109.23,110.637 0,63.582 50.555,107.457 109.023,107.457 29.727,0 58.367,-11.66 77.602,-31.394 l 19.797,19.402 c -25,25.207 -59.657,40.828 -97.965,40.828 -76.192,0 -137.965,-61.773 -137.965,-137.977 0,-76.203 62.695,-139.57 138.883,-139.57 36.789,0 71.129,14.617 95.863,38.082 l -20.617,19.656 c -18.785,-17.023 -46.473,-27.808 -75.391,-27.121" \
         id="path4562" \
         style="color:#000000;fill:#ffd35d;fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:1;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate" /> \
    </g> \
  </g> \
</svg> \
';



(function () {

	var draw = SVG('holder');
	
	var gr1 = draw.gradient('radial', function(stop) {
		stop.at(0, '#717171', 0.5)
		stop.at(1, '#717171', 1)
	})

	var curveData = [];
	var curve = draw.polyline([]).fill('none').stroke({ color: "#ffd35d", width: 2 });

	var heart = draw.group();
	
	var c1 = heart.circle(150);
	c1.fill(gr1);
	c1.center(0, 0);

	var cur = heart.circle(10);
	cur.center(-70, 0);
	cur.fill("#ffd35d");
	cur.hide();
	
	var c2 = heart.circle(150);
	c2.center(0, 0);
	c2.fill("#424242");
	
	var logo = heart.svg(rawLogo).get('root');
	logo.scale(0.1);
	logo.move(-40, -53);
	logo.fill("#ffd35d");
	
	heart.move(320, 240);
	curve.move(320, 240);
	
	
	var theta = 0;
	function beat () {
		theta += (Math.random() - 0.5) * 0.3 * Math.PI;
		cur.move(-Math.cos(theta) * 70, Math.sin(theta) * 70);

		curveData = curveData
			.filter(function (v) { return v[0] < 400; })
			.map(function (v) { return [v[0] + 10, v[1]]; })
			.concat([[200, theta]])
		;
		curve.animate(300, '>', 400).plot(curveData.map(function (v) {
			return [320-Math.cos(v[1]) * v[0], 240 + Math.sin(v[1]) * v[0]];
		}).concat([[320-Math.cos(theta) * 70, 240 + Math.sin(theta) * 70]]));

		logo.animate(300, '>', 400).fill("#ff9d33");
		cur.animate(300, '>', 400).dmove(-Math.cos(theta) * 125, Math.sin(theta) * 125);
		c1.animate(300, '>', 400).radius(200)
		.after(function () {
			logo.animate(300, '>').fill("#ffd35d");
			cur.animate(300, '>').dmove(Math.cos(theta) * 125, - Math.sin(theta) * 125);
			c1.animate(300, '>').radius(75)
			.after(beat);
		});
	}
	beat();

})()


