const toggle = document.getElementById('toggleDark');

function change(){
    var get = document.querySelector(".hdr");
    get.classList.toggle("hdrDarlk");
}

function changeMyContainerSkills(){
    var get = document.querySelector(".my_container_skills");
    get.classList.toggle("my_container_skills_dark");
}


// // var getMyContainer = document.querySelector(".my_container");
// // get.classList.toggle("my_containerDarck")
toggle.addEventListener('click', function(){
    this.classList.toggle('bi-moon');
    change();
    changeMyContainerSkills();
    

});