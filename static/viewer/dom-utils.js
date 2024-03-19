// @ts-nocheck
// Create regular message
const createChatMessageElement = (message, id) => `
    <div class="message gray-bgr" id=${id}>
    <div class="message-text">${message.chank}</div>
    </div>
`
// Add top margin for shift to the bottom
const doMessageFirst = (index) => {
	const mess = document.querySelector(`#message${index}`)
	mess.classList.add('first-message') 
}
// Do font large and change background
const markMessageAsCurrernt = (index) => {
	const mess = document.querySelector(`#message${index}`)
	mess.classList.add('current-message') 
	mess.classList.remove('gray-bgr')  
	mess.classList.add('blue-bgr') 
}
// Do font normal and restore background
const markMessageAsRegular = (index) => {
	const mess = document.querySelector(`#message${index}`)
	mess.classList.remove('current-message')  
	mess.classList.remove('blue-bgr')  
	mess.classList.add('gray-bgr')  
}
