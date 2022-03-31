const btn = document.querySelectorAll(".delete-btn")

await function deleteEquipment(evt) {
    console.dir(evt.target)
    evt.target.parentNode.remove()
    axios({
        method: "post",
        url: "/character/equipment/delete",
        data: {
            
        }
    })
}


for(let i of btn) {
    i.addEventListener("click", deleteEquipment)
}