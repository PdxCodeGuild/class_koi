let cnv = document.querySelector('canvas')
let ctx = cnv.getContext('2d')

let ball = {
    radius: 7,
    px: Math.random()*cnv.width,
    py: Math.random()*cnv.height,
    vx: (Math.random()),
    vy: (Math.random()),
}


function main_loop() {
    ctx.clearRect(0,0,cnv.width,cnv.height)
    ctx.beginPath()
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false)
    ctx.fillStyle = 'green'
    ctx.fill()
    ball.py += ball.vy
    ball.px += ball.vx
    ball.vy += 0.1
    ball.vy *= 0.99


    if (ball.py < 0 || ball.py > cnv.height){
        ball.vy *= -1
    }    
    if (ball.px < 0 || ball.px > cnv.height){
        ball.vx *= -1
    }

    // I want the ball to stop moving if its been on the ground for a while (add drag to x)
    // if (ball.vy < 0.001) {
    //     ball.vx = 0
    //     ball.vy = 0
    // }

   
    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);