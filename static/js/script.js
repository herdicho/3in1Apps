const addAction = document.getElementById('addAction')
const cardAction = document.getElementById('cardAction')

addAction.addEventListener("click", () => {
    
    if (cardAction.getAttribute('class').includes('hide')) {
        cardAction.classList.remove('hide')
        addAction.innerHTML = "Tutup"
    } else {
        cardAction.classList.add('hide')
        addAction.innerText = "Tambah Aksi Baru"
    }
        
});






/*const card = document.getElementById('card-note')
const button = document.getElementsByClassName('btn-note')

for (let i = 0, len = button.length; i < len; i++) {
    button[i].onclick = function(){
        btnClicked(button[i])
    }    
}

function btnClicked(e) {

    if (e.innerText === "Clear"){
        e.innerText = "Unclear"
       changeCardStatusToClear(e)
    } else {
        e.innerText = "Clear"
        changeCardStatusToUnclear(e)
    }
}

function changeCardStatusToUnclear(e) {
    e.parentElement.parentElement.parentElement.parentElement.classList.remove('bg-success')
    se.parentElement.parentElement.parentElement.parentElement.classList.add('bg-warning')
}

function changeCardStatusToClear(e) {
    e.parentElement.parentElement.parentElement.parentElement.classList.remove('bg-warning')
    e.parentElement.parentElement.parentElement.parentElement.classList.add('bg-success')
 }*/


/*
 $(".btn-note").on('click', function () {
    $.post(
        '',
        {
          'condition': $(this).find('input').val(),
          'csrfmiddlewaretoken': '{{csrf_token}}'
        },
        function(data){
           console.log(data.response);
        }
  );    
  });
*/



         
