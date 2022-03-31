const btnOpen = document.querySelectorAll(".toggle-open")
const btnClose = document.querySelectorAll(".toggle-close")

function toggleOpen(evt) {
    if(evt.target.classList[0] === "item-title") {
        evt.target.parentNode.parentNode.childNodes[3].classList.toggle("hidden")
    }
}

function toggleClose(evt) {
    if(evt.target.classList[2] === "fa-compress") {
        evt.target.parentNode.parentNode.classList.toggle("hidden")
    }
}

for(let i of btnOpen) {
    i.addEventListener("click", toggleOpen)

}

for(let j of btnClose) {
    j.addEventListener('click', toggleClose)
}




