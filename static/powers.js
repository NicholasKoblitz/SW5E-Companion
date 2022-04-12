const alignment = document.querySelector("#alignment")
const powerSelection = document.querySelectorAll(".power-selection")
// console.log(powerSelection)

// for(let i of powerSelection) {
//     console.log(i)
    // for(let j of i.options) {
    //     if(j.classList[0] == 'dark') {
    //         console.log(j)
    //         j.hidden = true
    //     }
    // }


function align(evt) {

    if(evt.target.value == "universal") {
        for(let item of powerSelection) {
            for(let i of item.options) {
                i.hidden = false
                    if("universal" != i.classList[0]) {
                        i.hidden = true
                }
            } 
        }
    }
    else if(evt.target.value == "light") {
        for(let item of powerSelection) {
            for(let i of item.options) {
                i.hidden = false
                    if("light" != i.classList[0]) {
                        i.hidden = true
                }
            } 
        }
    }
    else if(evt.target.value == "dark") {
        for(let item of powerSelection) {
            for(let i of item.options) {
                i.hidden = false
                    if("dark" != i.classList[0]) {
                        i.hidden = true
                }
            } 
        }
    }
}

alignment.addEventListener("change", align)