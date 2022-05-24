
// Bouncing Ball

// v2: add gravity and reduce ball velocity by 1% everytime it hits a wall

const canvas = document.getElementById('game-board')
// canvas.addEventListener('click', mainLoop)
// use this click event to push a new ball object into an array of balls
const ctx = canvas.getContext('2d');
let stopBool = false;
const stopBalls = document.getElementById('stop-game');
stopBalls.addEventListener('click', stopGame);

let ball = {
    radius: 24,
    px: Math.random()*(canvas.getAttribute('width')-24),
    py: Math.random()*(canvas.getAttribute('height')-24),
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10
};

function drawBall() {
    ctx.beginPath();
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2*Math.PI, false);
    ctx.fillStyle = '#2f8050';
    ctx.fill();
};

if (stopBool == false) { function mainLoop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    //update the ball's position
    ball.px += ball.vx;
    ball.py += ball.vy;
    console.log(`x: ${ball.px}, y: ${ball.py}, xVel: ${ball.vx}, yVel: ${ball.vy}`)
    
    //chek if it hit a boundary
    if (ball.px <= 0+ball.radius || ball.px >= 500-ball.radius) {
        ball.vx *= -.8
        console.log(ball.vx);
    }
    if (ball.py > 500-ball.radius) {
        // vyMag = Math.abs(ball.vy) * .9;
        // vyDir = Math.sign(ball.vy);
        if (ball.vy > 0) {
            ball.vy *= -.85
        }
        ball.py = 500-ball.radius;
    }
    if (ball.py <= 0+ball.radius) {
        ball.vy *= -1
    }
    //update the ball's velocity

    ball.vy += 1;
    
    //draw the ball
    drawBall();
    if (Math.abs(ball.vx) < .005 && Math.abs(ball.vy) < .005 ) {
        return;
    }
    if (stopBool == false) {
        window.requestAnimationFrame(mainLoop);
}}};

function stopGame() {
    stopBool = true;
    console.log(stopBool)
}

window.requestAnimationFrame(mainLoop);