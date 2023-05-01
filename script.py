let myLocal = localStorage.getItem(myLocal);
if (myLocal) {
  console.log(myLocal);
}
let listik = document.querySelector('number').value;
let limit = document.querySelector('limit').value;

function prover(listik, limit) {
  if  1 <= listik <= 10;      
  }else {
    console.log(`Номер страницы вне диапазона от 1 до 10`);
  if 1 <= limit <= 10;     
  else {
    console.log(`Лимит вне диапазона от 1 до 10`);
}
 
 
} 

function testUrl(url, callback) {
  let xhr = new XMLHttpRequest();
  xhr.open(`GET`, url, true);
  
  xhr.onload = function() {
    if (xhr.status !=200) {
      console.log(`Статус ответа: `, xhr.status);
    } else {
      const result = JSON.parse(xhr.response);
      if (callback) {
        callback(result);
      }
    }
  };
  xhr.onerror = function() {
    console.log(`Ошибка! Статус ответа: `, xhr.status);
  };
  xhr.send();
 };
const resultNode = document.querySelector(`.j-resul`);
const btnNode =  document.querySelector(`.j-btn-request`);

function displayResult(apiData) {
  let card = ``;
  apiData.forEach(item => {
    const cardBlock = `
    <div class="card">
    <img src="${item.download_url}"
    class="card-image"
    />
    <p>${item.author}</p>
    </div>
    `;
    cards = cards + cardBlock
  })
  resultNode.innerHTML = cards;
}
btnNode.addEventListener(`click`, () => {
  useRequest(`https://picsum.photos/v2/list?page= + ${number} &limit= + ${limit}`, displayResult);
})
