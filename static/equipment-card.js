const btnOpen = document.querySelectorAll(".toggle-open")
const btnClose = document.querySelectorAll(".toggle-close")
// const i = document.querySelector(".item-detials")

// console.dir(i)

function toggleOpen(evt) {

    console.log(evt.target.parentNode.parentNode.childNodes[3])
    if(evt.target.classList[0] === "item-title") {
        evt.target.parentNode.parentNode.childNodes[3].classList.toggle("hidden")
        // i.classList.toggle("hidden")
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




