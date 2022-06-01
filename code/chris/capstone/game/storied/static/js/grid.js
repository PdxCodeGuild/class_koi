window.onload = function() {
    const canvas = document.getElementById('grid');
    const ctx = canvas.getContext('2d');
    ctx.strokeStyle = "green";
    ctx.lineWidth = 4;

    // draw grid
    for (let i = 0; i<= 10; i++) {
        const x = i*60;
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
        ctx.stroke();

        const y = i*60;
        ctx.moveTo(0,y);
        ctx.lineTo(canvas.width, y);
        ctx.stroke();
    }

}