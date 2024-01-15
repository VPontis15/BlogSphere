const overlay = document.querySelector('.overlay')
const deleteBtns = document.querySelectorAll('.delete-button')

const optionsActionsDiv = document.querySelectorAll('.links-actions');
const deletePostMssg = document.querySelector('.delete-message')
const optionsBtn = document.querySelectorAll('.options-button');

const profilePic = document.getElementById('profile-pic')
const profileList = document.querySelector('.profile-links-nav');



profilePic.addEventListener('click', ()=>{
   

  profileList.classList.toggle('hidden')
})

document.addEventListener('click', (e) => {
   
    const isClosest = e.target.closest('.profile-links-nav');
  if (!isClosest || !profileList.classList.contains('.hidden')) {
   
    profileList.classList.add('.hidden')
  }
})

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




