window.onload = () => {
	// Themes
	let theme_toggle = document.getElementById("theme-trigger");
	let on = theme_toggle.value;
	theme_toggle.onchange = () => {
		if (theme_toggle.checked) {
			window.localStorage.setItem("theme", "light");
		} else {
			window.localStorage.setItem("theme", "dark");
		}
	}

	// Fancy header image.
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

	let current_color = Math.floor(Math.random() * colors.length);
	let color_offset = Math.floor(Math.random() * (colors.length - 1) + 1);
	let random_color = () => {
		current_color = (current_color + color_offset) % colors.length; 
		return colors[current_color];
	};

	for (let q = 0; q < 5; q++) {
		let x = Math.random() * canvas.width;
		let y = Math.random() * canvas.height;
		let c = random_color();
		ctx.fillStyle = "rgba(" + c.r + ", " + c.g + ", " + c.b + ", 0.2)";
		ctx.beginPath();
		ctx.arc(x, y, canvas.width / 2, 0, 2 * Math.PI);
		ctx.fill();
	}
};
