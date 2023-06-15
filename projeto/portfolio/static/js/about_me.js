
















document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('toggleDark');
    // // var getMyContainer = document.querySelector(".my_container");
    // // get.classList.toggle("my_containerDarck")
    toggle.addEventListener('click', function(){
        this.classList.toggle('bi-moon');
    });
})