const colors = {
	nightSky: '#001366',
	nightSkyTransparent: 'rgba(0, 19, 102, 0.05)'
}


const cnv = document.querySelector('canvas')

const ctx = cnv.getContext('2d')
const dim = { // dimensions of the canvas
	h: cnv.height,
	w: cnv.width
}

ctx.rect(0, 0, dim.w, dim.h)
ctx.fillStyle = colors.nightSky
ctx.fill()


// draw a goldenrod square on the canvas
// ctx.beginPath()
// ctx.rect(123, 123, 100, 100)
// ctx.fillStyle = 'goldenrod'
// ctx.fill()

// draw a goldenrod circle in the very center of the canvas
// ctx.beginPath()
// ctx.arc(dim.w / 2, dim.h / 2, 200, 0, Math.PI)
// ctx.fillStyle = 'goldenrod'
// ctx.fill()

// 100 multi-colored circles
// for (let i=0; i<100; i++) {
// 	ctx.beginPath()
// 	ctx.arc(Math.random() * dim.w, Math.random() * dim.h, 10 + Math.random() * 15, 0, 2 * Math.PI)
// 	ctx.fillStyle = `rgba(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255}, ${Math.random()})`
// 	ctx.fill()
// }

// starry sky
// for (let i=0; i<7500; i++) {
// 	ctx.beginPath()
// 	ctx.arc(Math.random() * dim.w, Math.random() * dim.h, Math.random() * 1.2, 0, 2 * Math.PI)
// 	ctx.fillStyle = 'white'
// 	ctx.fill()
// }

const moon = {
	x: 497,
	y: 352,
	r: 75,
	color: '#ebdb4c',
	vX: -0.5,
	vY: -0.75
}

const stars = []
for (let i=0; i<7500; i++) {
	stars.push({
		x: Math.random() * dim.w,
		y: Math.random() * dim.h,
		r: Math.random() * 1.2,
		vX: Math.random() * 3 - 1.5,
		vY: Math.random() * 3 - 1.5
	})
}

function drawMoon () {
	// clear the canvas
	// ctx.clearRect(0, 0, dim.w, dim.h)

	// draw the sky
	ctx.rect(0, 0, dim.w, dim.h)
	ctx.fillStyle = colors.nightSkyTransparent
	ctx.fill()

	// do not uncomment, will consume soul...
	// for (let i=0; i<7500; i++) {
	// 	ctx.beginPath()
	// 	ctx.arc(Math.random() * dim.w, Math.random() * dim.h, Math.random() * 1.2, 0, 2 * Math.PI)
	// 	ctx.fillStyle = 'white'
	// 	ctx.fill()
	// }

	// draw normal stars
	ctx.fillStyle = 'white'
	stars.forEach(star => {
		ctx.beginPath()
		ctx.arc(star.x, star.y, star.r, 0, 2 * Math.PI)
		ctx.fill()
	})

	// update 'star' positions
	stars.forEach(star => {
		star.x += star.vX
		star.y += star.vY
	})

	// update the moon's position
	moon.x += moon.vX
	moon.y += moon.vY

	// draw the moon
	ctx.beginPath()
	ctx.arc(moon.x, moon.y, moon.r, 0, 2 * Math.PI)
	ctx.fillStyle = moon.color
	ctx.fill()
	requestAnimationFrame(drawMoon)
}

// drawMoon()

const colorStars = []
for (let i=0; i<2500; i++) {
	const x = Math.random() * dim.w
	const y = Math.random() * dim.h
	stars.push({
		x,
		y,
		r: Math.random() * 3,
		vX: (dim.w / 2 - x) / 100,
		vY: (dim.h / 2 - y) / 100,
		color: `rgba(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255}, ${Math.random()})`
	})
}

function crazyStars () {
	// clear the canvas
	// ctx.clearRect(0, 0, dim.w, dim.h)

	// draw the sky
	ctx.rect(0, 0, dim.w, dim.h)
	ctx.fillStyle = 'rgba(0, 0, 0, 0.05)'
	ctx.fill()

	// do not uncomment, will consume soul...
	// for (let i=0; i<7500; i++) {
	// 	ctx.beginPath()
	// 	ctx.arc(Math.random() * dim.w, Math.random() * dim.h, Math.random() * 1.2, 0, 2 * Math.PI)
	// 	ctx.fillStyle = 'white'
	// 	ctx.fill()
	// }

	// draw normal stars
	// ctx.fillStyle = 'white'
	stars.forEach(star => {
		ctx.beginPath()
		ctx.arc(star.x, star.y, star.r, 0, 2 * Math.PI)
		ctx.fillStyle = star.color
		ctx.fill()
	})

	// update 'star' positions
	stars.forEach(star => {
		star.x += star.vX
		star.y += star.vY
	})


	requestAnimationFrame(crazyStars)
}

ctx.beginPath()
ctx.rect(0, 0, dim.w, dim.h)
ctx.fillStyle = '#000000'
ctx.fill()
crazyStars()


// use this to console.log click position as x,y coords of the canvas
// cnv.addEventListener('click', e => console.log(e.offsetX, e.offsetY))