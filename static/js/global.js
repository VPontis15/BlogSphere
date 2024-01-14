const overlay = document.querySelector('.overlay')
const deleteBtns = document.querySelectorAll('.delete-button')

const optionsActionsDiv = document.querySelectorAll('.links-actions');

const optionsBtn = document.querySelectorAll('.options-button');




optionsBtn.forEach((btn, index )=> {
    const  currentOptionsActionsDiv = optionsActionsDiv[index]
    currentOptionsActionsDiv.classList.add('hidden');
    btn.addEventListener('click', ()=> {
        optionsActionsDiv.forEach(option =>{
                option.classList.add('hidden')
        })
        currentOptionsActionsDiv.classList.toggle('hidden')
       console.log('clicked')
    })
})




// deleteBtns.forEach((btn )=> {
//     btn.addEventListener('click', (e) => {
//     e.preventDefault()
//     overlay.classList.remove('hidden')
//     console.log('data')
//     })
    
// })
