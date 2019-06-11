window.onload = () => {
	// Themes
	let body = document.getElementsByTagName("body")[0];
	let theme_icon = document.getElementById("toggle-theme");
	if (body.className === "dark") {
		theme_icon.src = "/static/img/theme-to-light.png";
	} else {
		theme_icon.src = "/static/img/theme-to-dark.png";
	}

	theme_icon.onclick = () => {
		let theme = body.className;
		if (theme === "dark") {
			body.className = "light";
		} else {
			body.className = "dark";
		}
		window.localStorage.setItem("theme", body.className);
		theme_icon.src = "/static/img/theme-to-" + theme + ".png";
	};

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

	/*
	let x = 0;
	let y = 0;
	let itter = 0;

	let wait_a_bit = () => {
		setTimeout(new_circle, 2000 * Math.random() + 2000);
	};

	let new_circle = () => {
		itter = 10;
		x = Math.random() * canvas.width;
		y = Math.random() * canvas.height;
		let c = random_color();
		ctx.fillStyle = "rgba(" + c.r + ", " + c.g + ", " + c.b + ", 0.001)";
		window.requestAnimationFrame(draw);
	};
	let draw = (timestamp) => {
		itter--;
		if (itter == 0) wait_a_bit();
		ctx.beginPath();
		ctx.arc(x, y, canvas.width / 2, 0, 2 * Math.PI);
		ctx.fill();
		window.requestAnimationFrame(draw);
	};
	new_circle();
	*/
};
