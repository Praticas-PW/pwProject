

document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('left');
    secondYear.style.display =  "none";
    thirdYear.style.display =  "none";
})

function showHideDivs(number){
    if(number == 0){
        secondYear.style.display =  "none";
        thirdYear.style.display =  "none";
        firstYear.style.display =  "";
    }
    if(number == 1){
        firstYear.style.display =  "none";
        secondYear.style.display =  "";
        thirdYear.style.display =  "none";
    }
    if(number == 2){
        firstYear.style.display =  "none";
        secondYear.style.display =  "none";
        thirdYear.style.display =  "";
    }
}

var a = 2;

function behind(){
    if(a > 1){
        a = 0;
    }else if(a-1 < 0){
        a = 0;
    }else{
        a--;
    }
    console.log(a);
    showHideDivs(a);
}

function next(){
    if(a > 1){
        a = 0;
    }else{
        a++;
    }
    console.log(a);

    showHideDivs(a);
}
