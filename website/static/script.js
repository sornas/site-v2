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

    // Clicking on the page removes the sidebar
    let article = document.querySelector("article");
    article.onclick = () =>  {
        document.querySelector("#nav-trigger-toggle").checked = false;
    };

    // Sliding for side menu
    let body = document.querySelector("body");
    let prev_touches = [];
    let pos_frame_count = 0;
    let neg_frame_count = 0;
    body.ontouchmove = (e) => {
        let touches = [];
        let inc_pos_frame = false;
        let inc_neg_frame = false;
        // TODO(ed): This should probably be in EM, but that requires fancy pants stuff.
        let threshold = 0.25; // pixels / ms
        for (let i = 0; i < e.touches.length; i++) {
            let curr = { x: e.touches[i].pageX, y: e.touches[i].pageY, t: e.timeStamp};
            touches.push(curr);

            if (prev_touches.length > i) {
                let prev = prev_touches[i];
                let delta_t = prev.t - curr.t;
                let delta_x = (prev.x - curr.x) / delta_t;
                let delta_y = (prev.y - curr.y) / delta_t;
                if (Math.abs(delta_x) > 3 * Math.abs(delta_y)) {
                    e.preventDefault();
                    if (delta_x > threshold) {
                        inc_pos_frame = true;
                        pos_frame_count++;
                    } else if (delta_x < -threshold) {
                        inc_neg_frame = true;
                        neg_frame_count++;
                    }
                }
            }
        }
        if (!inc_pos_frame)
            pos_frame_count = 0;
        if (!inc_neg_frame)
            neg_frame_count = 0;
        prev_touches = touches;
        let nav_toggle = document.querySelector("#nav-trigger-toggle");
        if (neg_frame_count > 2) {
            nav_toggle.checked = false;
        }
        if (pos_frame_count > 2) {
            nav_toggle.checked = true;
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

    // Super secret easter egg
    let secret_password = "LiTHe kod är bäst";
    let secret_password_progress = 0;
    document.querySelector("body").onkeypress = function(e) {
        if (e.key == "s") {
            let nav_toggle = document.querySelector("#nav-trigger-toggle");
            nav_toggle.checked = !nav_toggle.checked;
        }
        if (e.key == "l") {
            let lang = document.querySelector("#toggle-lang");
            lang.click();
        }
        if (e.key == "t") {
            let theme = document.querySelector("#toggle-theme");
            theme.click();
        }
        if (e.key == secret_password[secret_password_progress]) {
            secret_password_progress++;
            if (secret_password_progress == secret_password.length) {
                document.write("<h1>I know ;)</h1>");
            }
        } else {
            secret_password_progress = 0;
        }
        this.dispatchEvent(e);
    };
};
