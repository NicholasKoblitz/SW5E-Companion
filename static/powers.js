const alignment = document.querySelector("#alignment")
const powerSelection = document.querySelector(".power-selection")

function align(evt) {

    if(evt.target.value == "universal") {
        for(let item of powerSelection.options) {
            item.hidden = false
            if("universal" != item.classList[0]) {
                item.hidden = true
            }
        }
    }
    else if(evt.target.value == "light") {
        for(let item of powerSelection.options) {
            item.hidden = false
            if("light" != item.classList[0]) {
                item.hidden = true
            }
        }
    }
    else if(evt.target.value == "dark") {
        for(let item of powerSelection.options) {
            item.hidden = false
            if("dark" != item.classList[0]) {
                item.hidden = true
            }
        }
    }
}

alignment.addEventListener("change", align)