// @ts-nocheck
document.addEventListener('DOMContentLoaded', () => {
  // TG interaction
  tg = Telegram.WebApp
  tg.ready();
  tg.expand();
  tg.MainButton.hide();
  tg.MainButton.setParams({
      text: "END"
  });

  // Chat
  // Constants
  const chatHeader = document.querySelector('.chat-header')
  const chatMessages = document.querySelector('.chat-messages')
  const messCounter = document.querySelector('.counter')
  const settingSpan = document.querySelector('.settings-span')

  // Initialization
  chatHeader.innerHTML = '';
  let subTitles = [];
  let messageIndex = 0;

  fetchData().then( data => {
    const content = data.content;
    // The first line is the play Title
    const playTitle = data.content[0].chank
    chatHeader.innerHTML = playTitle;
    subTitles = content.slice(1);
    messCounter.innerHTML = subTitles.length-1 + '/' + messageIndex
  });

  ws.onmessage = function(event) {
    // const subtitle = document.getElementById('play')
    // const content = document.createTextNode(event.data)
    const index = Number(event.data);
    console.log(index)
    if (index === -10000) {
      resetMessanger();
    } else {
      messageIndex = index;
      createNewMessage()
    }
};

  const createNewMessage = () => {
    
    const message = subTitles[messageIndex];
    messageText = message.chank;

    /* Add message to DOM */
    const newMessageElement = createChatMessageElement(messageText, 'message' + messageIndex)
    chatMessages.innerHTML += newMessageElement;
    messCounter.innerHTML = subTitles.length + '/' + messageIndex 

    if (messageIndex === 0) {
      doMessageFirst(messageIndex)  
    }
     if ((messageIndex >= 0)) {   
      markMessageAsCurrernt(messageIndex) 
      if (messageIndex > 0) {
        markMessageAsRegular(messageIndex - 1)
      }
    }

    /*  Scroll to bottom of chat messages */
    chatMessages.scrollTop = chatMessages.scrollHeight
  }


  const resetMessanger =  () => {
    chatMessages.innerHTML = ''
    messageIndex = 0;
  }

  settingSpan.addEventListener('click', () => {
    console.log('Settings')
  })

});
