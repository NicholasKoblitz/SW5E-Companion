const tabs = document.querySelector(".character-tabs")
const tab = document.querySelectorAll(".tab")
const abilities = document.querySelector(".abilities")
const features = document.querySelector(".features")
const character = document.querySelector(".character")
const equipment = document.querySelector(".equipment")
const powers = document.querySelector(".powers")
const proficiencies = document.querySelector(".proficiencies")

const featArrow = document.querySelectorAll(".fa-arrow-down")



// Tab events

function select(evt) {
    console.dir(evt.target)

    for(let i of tab) {
        i.classList.remove("select-tab")
    }


    if(evt.target.id !== "ability") {
        abilities.classList.add("hidden")
    }
    else if(evt.target.id === "ability") {
        abilities.classList.remove("hidden")
    }


    if(evt.target.id !== "feature") {
        features.classList.add("hidden")
    }
    else {
        features.classList.remove("hidden")
    }


    if(evt.target.id !== "character") {
        character.classList.add("hidden")
    }
    else {
        character.classList.remove("hidden")
    }

    if(evt.target.id !== "equipment") {
        equipment.classList.add("hidden")
    }
    else {
        equipment.classList.remove("hidden")
    }

    if(evt.target.id !== "powers") {
        powers.classList.add("hidden")
    }
    else {
        powers.classList.remove("hidden")
    }

    if(evt.target.id !== "proficiencies") {
        proficiencies.classList.add("hidden")
    }
    else {
        proficiencies.classList.remove("hidden")
    }

    evt.target.parentNode.classList.toggle("select-tab")
    
}

tabs.addEventListener("click", select)

// Feature Events

function dropdown(evt) {
    console.dir(evt.target.parentNode.parentNode.childNodes)
    let feat = evt.target.parentNode.parentNode.parentNode.childNodes[3]
    let span = evt.target.parentNode
    if(evt.target.classList[1] === "fa-plus") {
        feat.classList.remove("hidden")
        feat.style.position = "relative"
        evt.target.remove(evt.target)
        newEle = document.createElement("i")
        newEle.classList = "fa-solid fa-minus"
        span.append(newEle)
    }
    else if(evt.target.classList[1] === "fa-minus") {
        feat.classList.add("hidden")
        feat.style.position = "absolute"
        evt.target.remove(evt.target)
        newEle = document.createElement("i")
        newEle.classList = "fa-solid fa-plus"
        console.log(span)
        span.append(newEle)
    }
    else if(evt.target.parentNode.parentNode.id === "bg-feat") {
        feat.classList.remove("hidden")
        feat.style.position = "relative"
        evt.target.remove(evt.target)
        newEle = document.createElement("i")
        newEle.classList = "fa-solid fa-minus"
        span.append(newEle)
    }
    else if(evt.target.parentNode.parentNode.id === "species-feat") { 
    feat.classList.remove("hidden")
    feat.style.position = "relative"
    evt.target.remove(evt.target)
    newEle = document.createElement("i")
    newEle.classList = "fa-solid fa-minus"
    span.append(newEle)
    }
    else if(evt,target.parentNode.parentNode.id === "force-power") {
        feat.classList.remove("hidden")
    feat.style.position = "relative"
    evt.target.remove(evt.target)
    newEle = document.createElement("i")
    newEle.classList = "fa-solid fa-minus"
    span.append(newEle)
    }
    else if(evt,target.parentNode.parentNode.id === "bg-feat-2") {
        feat.classList.remove("hidden")
    feat.style.position = "relative"
    evt.target.remove(evt.target)
    newEle = document.createElement("i")
    newEle.classList = "fa-solid fa-minus"
    span.append(newEle)
    }
}

features.addEventListener("click", dropdown)
powers.addEventListener("click", dropdown)


// Powers Events

function addPower(evt) {
    console.dir(evt.target)
}

powers.addEventListener("click", addPower)