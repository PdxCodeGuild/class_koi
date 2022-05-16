let cnv = document.querySelector('.ballworld')
let ctx = cnv.getContext("2d")

let width = cnv.width
let height = cnv.height

let x = document.getElementById('x')
let y = document.getElementById('y')

let ball = {
    radius: 20*Math.random(),
    px: Math.random()*width,
    py: Math.random()*height,
    vx: (2*Math.random()-1)*5,
    vy: (2*Math.random()-1)*5,
}

let colors = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'purple',
]

let i = 0

while (ball.radius < 4){
    ball.radius = 20*Math.random()
}

function mainLoop () {
    ctx.clearRect(0,0,width,height)
    ctx.beginPath()
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false)
    ctx.fillStyle = colors[i]
    ctx.fill()

    if ((ball.px += ball.vx > ball.radius) || (ball.px += ball.vx < width - ball.radius)) {
        ball.px += ball.vx
    } else if (ball.px += ball.vx > width - ball.radius) {
    } else {
        ball.px = ball.radius
    }

    if ((ball.py += ball.vy > ball.radius) || (ball.py += ball.vy < height - ball.radius)) {
        ball.py += ball.vy
    } else if (ball.py += ball.vy > height - ball.radius) {
        ball.py = height - ball.radius
    } else {
        ball.py = ball.radius
    }

    if (ball.px < ball.radius) {
        ball.px = ball.radius
    } else if (ball.px > width - ball.radius) {
        ball.px = width - ball.radius
    }

    if (ball.py < ball.radius) {
        ball.py = ball.radius
    } else if (ball.py > height - ball.radius) {
        ball.py = height - ball.radius
    }

    if (ball.py <= ball.radius || ball.py >= height - ball.radius) {
        ball.vy *= -.9
        ball.vx *= .9
        i++
    } else {
        ball.vy += 0.1
        ball.vy *= 0.99
    }
    if (ball.px <= ball.radius || ball.px >= width - ball.radius) {
        ball.vx *= -.9
        ball.vy *= .9
        i++
    }
    
    if (ball.py <= ball.radius || ball.py >= height - ball.radius) {
        ball.vy *=.9
    }
    
    if (i == colors.length) {
        i = 0
    }
    
    window.requestAnimationFrame(mainLoop)
}


window.requestAnimationFrame(mainLoop)


