// @ts-nocheck
// Create regular message
const createChatMessageElement = (message, id) => `
	<div class="message multiline" id=${id}>
	<div class="message-text">${message}</div>
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

}
// Do font normal and restore background
const markMessageAsRegular = (index) => {
	const mess = document.querySelector(`#message${index}`)
	mess.classList.remove('current-message')
}
