window.onload = () => {

	let canvas = document.getElementById("fancy-pants-graphics");
	canvas.width = canvas.offsetWidth;
	canvas.height = canvas.offsetHeight;
	let ctx = canvas.getContext("2d");

	let colors = [
		{ r: 0,   g: 0,   b: 255 },
		{ r: 255, g: 255,   b: 0 },
		{ r: 0,   g: 255, b: 0 },
		{ r: 255, g: 0,   b: 255 },
	];

	let paint = () => {
		let x = Math.random() * canvas.width;
		let y = Math.random() * canvas.height;
		let c = colors[Math.floor(Math.random() * colors.length)];
		ctx.fillStyle = "rgba(" + c.r + ", " + c.g + ", " + c.b + ", 0.5)";
		ctx.beginPath();
		ctx.arc(x, y, canvas.width / 2, 0, 2 * Math.PI);
		ctx.fill();
	}

	window.requestAnimationFrame(() => {
		for (let i = 0; i < 10; i++) {
			paint();
		}
		window.requestAnimationFrame(step);
	});

	let next = 0;
	let itter = 0;
	let step = (timestamp) => {
		if (timestamp > next) {
			next = timestamp + 5000;
			itter++;
			if (itter > 100) return;
			paint();
		}
		window.requestAnimationFrame(step);
	};
	
};
