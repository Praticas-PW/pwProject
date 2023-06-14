

function change(){
    var get = document.querySelector(".hdr");
    get.classList.toggle("hdrDarlk");

}

function changeMyContainer(){
    var get = document.querySelector(".my_container");
    get.classList.toggle("my_containerDark");

    get = document.querySelector(".name");
    get.classList.toggle("nameDark");   
}

function changeAboutMeContainer(){
    var get = document.querySelector(".about_me_container");
    get.classList.toggle("about_me_container_dark");
}




document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('toggleDark');
    // // var getMyContainer = document.querySelector(".my_container");
    // // get.classList.toggle("my_containerDarck")
    toggle.addEventListener('click', function(){
        this.classList.toggle('bi-moon');
        change();
        changeMyContainer();
        changeAboutMeContainer()
    });
})