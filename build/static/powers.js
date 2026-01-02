const alignment = document.querySelector("#alignment")
const techPowers = document.querySelector("#tech-powers")
const powerSelection = document.querySelectorAll(".power-selection")
const powerSelectionTech = document.querySelectorAll(".power-selection-tech")


if(alignment !== null) {
    function align(evt) {

        if(evt.target.value === "universal-0") {
            for(let item of powerSelection) {
                for(let i of item.options) {
                    i.hidden = false
                        if("universal-0" !== i.classList[0]) {
                            i.hidden = true
                    }
                } 
            }
        }
        else if(evt.target.value === "light-0") {
            for(let item of powerSelection) {
                for(let i of item.options) {
                    i.hidden = false
                        if("light-0" !== i.classList[0]) {
                            i.hidden = true
                    }
                } 
            }
        }
        else if(evt.target.value === "dark-0") {
            for(let item of powerSelection) {
                for(let i of item.options) {
                    i.hidden = false
                        if("dark-0" !== i.classList[0]) {
                            i.hidden = true
                    }
                } 
            }
        }
        else if(evt.target.value === "universal-1") {
            for(let item of powerSelection) {
                for(let i of item.options) {
                    i.hidden = false
                        if("universal-1" !== i.classList[0]) {
                            i.hidden = true
                    }
                } 
            }
        }
        else if(evt.target.value === "light-1") {
            for(let item of powerSelection) {
                for(let i of item.options) {
                    i.hidden = false
                        if("light-1" !== i.classList[0]) {
                            i.hidden = true
                    }
                } 
            }
        }
        else if(evt.target.value === "dark-1") {
            for(let item of powerSelection) {
                for(let i of item.options) {
                    i.hidden = false
                        if("dark-1" !== i.classList[0]) {
                            i.hidden = true
                    }
                } 
            }
        }
    }
    
    alignment.addEventListener("change", align)
}
else if(alignment === null) {
    function tech(evt) {
        if(evt.target.value === "at-will") {
            for(let item of powerSelectionTech) {
                for(let i of item.options) {
                    i.hidden = false
                        if("at-will" !== i.classList[0]) {
                            i.hidden = true
                    }
                } 
            }
        }
        else if(evt.target.value === "1st") {
            for(let item of powerSelectionTech) {
                for(let i of item.options) {
                    i.hidden = false
                        if("1st" !== i.classList[0]) {
                            i.hidden = true
                    }
                } 
            }
        }
    }
    
    techPowers.addEventListener("change", tech)
}





