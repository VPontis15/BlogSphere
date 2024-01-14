

const profilePic = document.getElementById('profile-pic')
const profileList = document.querySelector('.profile-links-nav');


profilePic.addEventListener('click', ()=>{
   

  profileList.classList.toggle('hidden')
})