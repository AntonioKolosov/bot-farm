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
  const messCounter = document.querySelector('.counter')
  const resetChatBtn = document.querySelector('.reset-chat-button')
  const settingSpan = document.querySelector('.settings-span')
  const closeButton = document.getElementById('close')
  const smallSize = document.getElementById('small-font-size-selector')
  const mediumSize = document.getElementById('medium-font-size-selector')
  const largeSize = document.getElementById('large-font-size-selector')


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

  const updateCounter = (index) => {
    messCounter.innerHTML = (index)  + ' / ' + subTitles.length
  };  

  const markMessage = () => {
    if (messageIndex === 0) {
      doMessageFirst(messageIndex)  
    }
    if ((messageIndex >= currentMessageIndexShift)) {   
      markMessageAsCurrernt(messageIndex - currentMessageIndexShift) 
      if (messageIndex > currentMessageIndexShift) {
        markMessageAsRegular(messageIndex - currentMessageIndexShift - 1)
      }
    }
  };

  const nextMessage = (e) => {
    e.preventDefault();
    
    let index = messageIndex - currentMessageIndexShift - 1;
    if (messageIndex < subTitles.length) {
      createNewMessage();
      messageIndex++;
      updateCounter(index + currentMessageIndexShift - 1);
    } 
    else if (messageIndex < subTitles.length + currentMessageIndexShift + 1) {
      messageIndex++;
      updateCounter(index + currentMessageIndexShift - 1);
    }
    else {
      index = -9999
    }
    
    sendMessageIndex(index).then( data => {
      console.log(index);
    })
  }

  const createInitialMessagesSubset = () => {
    for (let i = 0; i <= currentMessageIndexShift; i++) {
      createNewMessage();
      messageIndex++;
    }
    updateCounter(0);
  }

  const createNewMessage = () => {
    
    const message = subTitles[messageIndex];
    const messageText = message.chank;

    /* Add message to DOM */
    const newMessageElement = createChatMessageElement(messageText, 'message' + messageIndex)
    chatMessages.innerHTML += newMessageElement;
    markMessage();

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
  
  settingSpan.addEventListener('click', () => {
    const popup = document.getElementById('popup');
    popup.style.display = 'block';
  });

  closeButton.addEventListener('click', () => {
    const popup = document.getElementById('popup');
    popup.style.display = 'none';
  });

  smallSize.addEventListener('click', () => {
    const chatMessages = document.getElementById('chat-messages')
    chatMessages.style.fontSize = "0.95em";
  });

  mediumSize.addEventListener('click', () => {
    const chatMessages = document.getElementById('chat-messages')
    chatMessages.style.fontSize = "1.25em";
  });

  largeSize.addEventListener('click', () => {
    const chatMessages = document.getElementById('chat-messages')
    chatMessages.style.fontSize = "1.45em";
  });
});
