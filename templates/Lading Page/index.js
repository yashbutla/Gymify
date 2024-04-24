// testing JS File 

console.log("Welcome To Schoolify");

// Loader
let loader = document.getElementById("loader");
window.addEventListener("load", function () {
    loader.style.display = "none";
})

// Start Free Trail Button

let signUpBtn1 = document.getElementById("signupBtn1");
signUpBtn1.addEventListener("click",function(){
    window.location.assign("/Signup/signup.html");
});

let signUpBtn2 = document.getElementById("signupBtn2");
signUpBtn2.addEventListener("click",function(){
    window.location.assign("/Signup/signup.html");
})