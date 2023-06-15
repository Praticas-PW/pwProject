
function changeblogHeader(){
    var get = document.querySelector(".blogHeader");
    get.classList.toggle("blogHeader_dark");

}

function inputTexut(){
    var get = document.querySelector(".inputText");
    get.classList.toggle("inputText_dark");

}



document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('toggleDark');
    // // var getMyContainer = document.querySelector(".my_container");
    // // get.classList.toggle("my_containerDarck")
    toggle.addEventListener('click', function(){
        this.classList.toggle('bi-moon');
        changeblogHeader();
        inputTexut();
    });
})