// @ts-nocheck
// Be interactions
const BE_LOCATOR = 'messintegrator.onrender.com';
// const BE_LOCATOR = '9bc5-129-159-137-238.ngrok-free.app';

const url = `wss:${BE_LOCATOR}/ws`
const ws = new WebSocket(url);
// Get data
// ws.onmessage = function(event) {
//     // const subtitle = document.getElementById('play')
//     // const content = document.createTextNode(event.data)
//     const index = Number(event.data);
//     console.log(index)
//     messageIndex = index;
//     createNewMessage()
// };

// Get data from backend
async function fetchData(lang = 'ru') {
  const url = `https://${BE_LOCATOR}/webdata/${lang}`;
  const response = await fetch(url);
  if (response.ok) {
      const result = await response.json();  
      // now do something with the result
      // console.log("RESULT", result);
      return result
  } else {
      alert(response.status);
      return {}
  }
}

