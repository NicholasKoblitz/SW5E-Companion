const btn = document.querySelectorAll(".delete-btn")

async function deleteEquipment(evt) {
    console.dir(evt.target.parentNode.childNodes)
    evt.target.parentNode.childNodes[1].remove()
}

for(let i of btn) {
    i.addEventListener("click", deleteEquipment)
}