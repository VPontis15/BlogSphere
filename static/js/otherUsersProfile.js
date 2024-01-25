const followActionBtn = document.querySelector('.follow-status-icon');
const followPromptPopUp = document.querySelector('.follow-action');

const updateFollowStatus = (showPrompt, color, imageUrl) => {
  followPromptPopUp.style.display = showPrompt ? 'block' : 'none';
  followPromptPopUp.style.color = color;
  followActionBtn.src = imageUrl;
};

followActionBtn.addEventListener('mouseover', () => {
  if (followPromptPopUp.textContent == 'Follow') {
    updateFollowStatus(true, '#1d3580', unfollowSvgUrl);
  } else {
    updateFollowStatus(true, '#ba1642', followSvgUrl);
  }
});

followActionBtn.addEventListener('mouseout', () => {
  if (followPromptPopUp.textContent == 'Follow') {
    updateFollowStatus(false, '', followSvgUrl);
  } else {
    updateFollowStatus(false, '', unfollowSvgUrl);
  }
});
