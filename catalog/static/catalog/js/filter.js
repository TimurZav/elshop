function sortDown() {
    updateList('down');
}

function sortUp() {
    updateList('up');
}

function updateList(direction) {
    let tockens = document.getElementsByName('csrfmiddlewaretoken')
    let xhr = new XMLHttpRequest();
    xhr.open('GET', '/catalog/filter?' + "csrf_token=" + tockens[0].value + "&direction=" + direction +
    "&category=telephones");
    xhr.send();

    xhr.onloadend = function() {
        if (xhr.status == 200) {
            let oldList = document.querySelector('.card-group');
            oldList.innerHTML = '';
            let phonesList = JSON.parse(xhr.responseText);
            for (phone of phonesList) {
                let li = document.createElement('div');
                li.innerHTML =
                "<div class='row g-0'> <div class='col-md-6'> <div class='card-body'><h5 class='card-title'>"
                 + phone.fields.name +
                "</h5><p class='card-text'>"
                 + phone.fields.description +
                 "<p class='card-text'><small class='text-muted'>" + phone.fields.price + "</small></p></div></div></div>"
//                li.innerHTML = phone.fields.name;
                oldList.appendChild(li)
            }
        }
    }
}
