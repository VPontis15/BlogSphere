const overlay = document.querySelector('.overlay')
const openDeletePostDialogBtns = document.querySelectorAll('.openDeletePostDialogBtns')

const optionsActionsDiv = document.querySelectorAll('.links-actions');
const deletePostMssg = document.querySelector('.delete-message')
const optionsBtn = document.querySelectorAll('.options-button');
const commentEditModalBtns = document.querySelectorAll('.editComment')
const commentEditModal = document.querySelector('.comment-form--modal')
const profilePic = document.getElementById('profile-pic')
const profileList = document.querySelector('.profile-links-nav');
const dialogDeletePost = document.querySelectorAll('.delete-dialog');
const closeDeleteModal = document.querySelectorAll('.cancel-delete-post')
const textAreaComment = document.querySelector('.comment-textarea')
const commentBtn = document.querySelector('.comment-btn')

closeDeleteModal.forEach((btn, index) =>{
  btn.style.color = 'purple'
 const currentCloseModalBtn = closeDeleteModal[index]
 const currentDialog =dialogDeletePost[index]
 console.log(index)
 currentCloseModalBtn.addEventListener('click', ()=>{
   currentDialog.close()
 })
 
 })


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
       
    })
})


openDeletePostDialogBtns.forEach((btn, index) =>{

const currentDialogBtn = openDeletePostDialogBtns[index]
const currentDialog =dialogDeletePost[index]
currentDialogBtn.addEventListener('click', ()=>{
  currentDialog.showModal()
})

})


textAreaComment.addEventListener('focus', ()=>{
  commentBtn.classList.remove('hidden')
 commentBtn.classList.add('fadeIn')


},true)



commentEditModalBtns.forEach((btn,index) => {
  currentEditModalBtn = commentEditModalBtns[index]
  currentEditModalBtn.addEventListener('click', ()=>{
    commentEditModal.showModal()
  })
})



