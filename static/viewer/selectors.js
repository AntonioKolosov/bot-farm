// @ts-nocheck
// Selectors
const smallSelectorBtn = document.querySelector('#small-font-size-selector')
const mediumSelectorBtn = document.querySelector('#medium-font-size-selector')
const largeSelectorBtn = document.querySelector('#large-font-size-selector')

const enSelectorBtn = document.querySelector('#en-language-selector')
const heSelectorBtn = document.querySelector('#he-language-selector')
const ruSelectorBtn = document.querySelector('#ru-language-selector')


let currentFontSize = 'M'

const changeFontSize = (size) => {
  currentFontSize = size

  if (size === 'S') {
    smallSelectorBtn.classList.add('current-font-size')
    mediumSelectorBtn.classList.remove('current-font-size')
    largeSelectorBtn.classList.remove('current-font-size')
  }
  if (size === 'M') {
    mediumSelectorBtn.classList.add('current-font-size')
    smallSelectorBtn.classList.remove('current-font-size')
    largeSelectorBtn.classList.remove('current-font-size')
  }

  if (size === 'L') {
    largeSelectorBtn.classList.add('current-font-size')
    smallSelectorBtn.classList.remove('current-font-size')
    mediumSelectorBtn.classList.remove('current-font-size')
  }

  console.log(currentFontSize)

  if (currentFontSize != size) {
    currentFontSize = size
    console.log(currentFontSize)
  }

  // /* auto-focus the input field */
  // chatInput.focus()
}

smallSelectorBtn.onclick = () => changeFontSize('S')
mediumSelectorBtn.onclick = () => changeFontSize('M')
largeSelectorBtn.onclick = () => changeFontSize('L')


let currentLanguage = 'Ru'

const changeLanguage = (lang) => {
  document.documentElement.dir = (lang === 'He') ? 'rtl' : 'ltr';
  currentLanguage = lang

  if (lang === 'En') {
    enSelectorBtn.classList.add('current-language')
    heSelectorBtn.classList.remove('current-language')
    ruSelectorBtn.classList.remove('current-language')
  }
  if (lang === 'He') {
    heSelectorBtn.classList.add('current-language')
    enSelectorBtn.classList.remove('current-language')
    ruSelectorBtn.classList.remove('current-language')
  }

  if (lang === 'Ru') {
    ruSelectorBtn.classList.add('current-language')
    enSelectorBtn.classList.remove('current-language')
    heSelectorBtn.classList.remove('current-language')
  }

  if (currentLanguage != lang) {
    currentLanguage = lang
    console.log(currentLanguage)
  }
}

enSelectorBtn.onclick = () => changeLanguage('En')
heSelectorBtn.onclick = () => changeLanguage('He')
ruSelectorBtn.onclick = () => changeLanguage('Ru')
