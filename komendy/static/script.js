let rotatev = 90

function rotate() {
    let x = document.body
    x.style.transform = 'rotate(' + rotatev + 'deg)';
    rotatev += 90
}