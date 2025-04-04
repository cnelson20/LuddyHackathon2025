console.log("Hello, World!");

const canvas = document.getElementById("cid");
const ctx = canvas.getContext("2d");

img = new Image();
img.onload = () => {
	Promise.all([
		createImageBitmap(img),
	]).then((map) => {
		ctx.drawImage(map[0], 0, 0);
	});
}
img.src = "/static/images/bloommap.png";