window.onload = function() {
    const canvas = document.getElementById('grid');
    const ctx = canvas.getContext('2d');
    ctx.strokeStyle = "darkolivegreen";
    ctx.lineWidth = 4;

    // draw grid
    for (let i = 0; i<= 5; i++) {
        const x = i*40;
        ctx.moveTo(x, 0);
        ctx.lineTo(x, canvas.height);
        ctx.stroke();

        const y = i*40;
        ctx.moveTo(0, y);
        ctx.lineTo(canvas.width, y);
        ctx.stroke();
    }

    // draw images
    const p = ctx.lineWidth / 2; // padding
    for (let xCell = 0; xCell < 5; xCell++) {
        for (let yCell = 0; yCell < 5; yCell++) {
            const x = xCell * 40;
            const y = yCell * 40;
            const img = new Image();
            img.onload = function() {
                ctx.drawImage(img, x+p, y+p, 40-p*2, 40-p*2);
            };

            img.src = `https://dummyimage.com/40x40/000/fff&text=${xCell},${yCell}`;
        }
    }
};