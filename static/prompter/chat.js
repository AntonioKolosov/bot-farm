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
  tg.MainButton.onClick( ()=> {
      // The end title
      sendMessageIndex(-9999)
      tg.sendData('/end')
  });

  // Chat
  // Constants
  const chatHeader = document.querySelector('.chat-header')
  const chatMessages = document.querySelector('.chat-messages')
  const nextBtn = document.querySelector('.next-button')
  const resetChatBtn = document.querySelector('.reset-chat-button')

  // Define number of messages from bottom
  const currentMessageIndexShift = 2;

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
    // Show the first subset
    createInitialMessagesSubset()
  });

  const nextMessage = (e) => {
    e.preventDefault();
    
    let index = messageIndex - currentMessageIndexShift - 1;
    if (messageIndex < subTitles.length) {
      createNewMessage();
      messageIndex++;
    } else {
      index = -9999
    }
    
    sendMessageIndex(index).then( data => {
      console.log("sent", index);
    }) 
  }

  const createInitialMessagesSubset = () => {
    for (let i = 0; i <= currentMessageIndexShift; i++) {
      createNewMessage();
      messageIndex++;
    }
  }

  const createNewMessage = () => {
    
    const message = subTitles[messageIndex];

    /* Add message to DOM */
    const newMessageElement = createChatMessageElement(message, 'message' + messageIndex)
    chatMessages.innerHTML += newMessageElement;

    if (messageIndex === 0) {
      doMessageFirst(messageIndex)  
    }
     if ((messageIndex >= currentMessageIndexShift)) {   
      markMessageAsCurrernt(messageIndex - currentMessageIndexShift) 
      if (messageIndex > currentMessageIndexShift) {
        markMessageAsRegular(messageIndex - currentMessageIndexShift - 1)
      }
    }

    /*  Scroll to bottom of chat messages */
    chatMessages.scrollTop = chatMessages.scrollHeight
  }

  // Set event handlers
  nextBtn.addEventListener('click', nextMessage)

  resetChatBtn.addEventListener('click', () => {
    chatMessages.innerHTML = ''
    messageIndex = 0;
    createInitialMessagesSubset()
    sendMessageIndex(-10000).then( data => {
      console.log("sent", -10000);
    }) 
  })
  
});
