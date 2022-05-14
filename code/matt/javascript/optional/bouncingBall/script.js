let cnv = document.querySelector('.ballworld')
let ctx = cnv.getContext("2d")

let width = cnv.width
let height = cnv.height

let x = document.getElementById('x')
let y = document.getElementById('y')

let ball = {
    radius: 6,
    px: Math.random()*width,
    py: Math.random()*height,
    vx: (2*Math.random()-1)*5,
    vy: (2*Math.random()-1)*5,
};

function mainLoop () {
    ctx.clearRect(0,0,width,height)
    ctx.beginPath()
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false)
    ctx.fillStyle = 'green'
    ctx.fill()

    if ((ball.px += ball.vx > ball.radius) || (ball.px += ball.vx < width - ball.radius)) {
        ball.px += ball.vx
    } else {
        ball.px = ball.radius
    }

    if ((ball.py += ball.vy > ball.radius) || (ball.py += ball.vy < height - ball.radius)) {
        ball.py += ball.vy
    } else if (ball.py += ball.vy >= height - ball.radius) {
        ball.py = height - ball.radius
    } else {
        ball.py = ball.radius
    }

    if (ball.py <= ball.radius || ball.py >= height - ball.radius) {
        ball.vy *= -.9
        ball.vx *= .99
    } else {
        ball.vy += 0.1
        ball.vy *= 0.99
    }
    if (ball.px <= ball.radius || ball.px >= width - ball.radius) {
        ball.vx *= -.9
        ball.vy *= .99
    }


    x.innerHTML = `X ${ball.px}`
    y.innerHTML = `Y ${ball.py}`
    
    window.requestAnimationFrame(mainLoop)
}


window.requestAnimationFrame(mainLoop)


