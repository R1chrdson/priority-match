alternatives_list = document.getElementById("alternatives-list");
add_alternative_button = document.getElementById("alternative_add_button");

add_alternative_button.addEventListener("click", function (e) {
    l = alternatives_list.getElementsByTagName('li').length
    if (l >= 10)
        return

    var li = document.createElement("li");
    li.innerHTML = "<input class=\"alternative-text\" placeholder=\"Введіть назву альтернативи\"> " +
        "<button>X</button>"
    b = li.getElementsByTagName("button")[0]
    b.addEventListener('click', remove_alternative)
    alternatives_list.appendChild(li);
});

function remove_alternative(e) {
    l = alternatives_list.getElementsByTagName('li').length
    if (l <= 1)
        return
    e.target.parentNode.remove()
}

add_alternative_button.click()