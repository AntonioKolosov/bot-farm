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
  const closeButton = document.getElementById('close')
  const smallSize = document.getElementById('small-font-size-selector')
  const mediumSize = document.getElementById('medium-font-size-selector')
  const largeSize = document.getElementById('large-font-size-selector')
  const engLang = document.getElementById('en-language-selector')
  const hebLang = document.getElementById('he-language-selector')
  const rusLang = document.getElementById('ru-language-selector')

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
    updateCounter(-1);
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

  const updateCounter = (index) => {
    messCounter.innerHTML = (index + 1)  + ' / ' + subTitles.length 
  };

  const createNewMessage = () => {
    
    const message = subTitles[messageIndex];
    messageText = message.chank;

    /* Add message to DOM */
    const newMessageElement = createChatMessageElement(messageText, 'message' + messageIndex)
    chatMessages.innerHTML += newMessageElement;
    updateCounter(messageIndex);

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
    updateCounter(-1);
  };

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

  engLang.addEventListener('click', () => {
    fetchData('en').then( data => {
      const content = data.content;
      // The first line is the play Title
      const playTitle = data.content[0].chank
      chatHeader.innerHTML = playTitle;
      subTitles = content.slice(1);
      updateCounter(-1);
    });
  });

  hebLang.addEventListener('click', () => {
    fetchData('he').then( data => {
      const content = data.content;
      // The first line is the play Title
      const playTitle = data.content[0].chank
      chatHeader.innerHTML = playTitle;
      subTitles = content.slice(1);
      updateCounter(-1);
    });
  });

  rusLang.addEventListener('click', () => {
    fetchData().then( data => {
      const content = data.content;
      // The first line is the play Title
      const playTitle = data.content[0].chank
      chatHeader.innerHTML = playTitle;
      subTitles = content.slice(1);
      updateCounter(-1);
    });
  });
});
