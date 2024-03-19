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

    /* Add message to DOM */
    const newMessageElement = createChatMessageElement(message, 'message' + messageIndex)
    chatMessages.innerHTML += newMessageElement;

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
  
});
