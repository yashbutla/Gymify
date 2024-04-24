// // Testing 
// console.log("Welcome to Gymify - Index Page");

// // Menu Icon 

// function toggleSidebar() {
//     let sidebar = document.querySelector('#sidebar');
//     if (window.innerWidth < 1024) {
//         sidebar.style.transform = (sidebar.style.transform === 'translateX(0px)') ? 'translateX(-300px)' : 'translateX(0px)';
//     }
// }

// document.addEventListener('click', function(event) {
//     if (window.innerWidth < 1024) {
//         let sidebar = document.querySelector('#sidebar');
//         let menuIcon = document.querySelector('#menuIcon');
//         let isClickInsideSidebar = sidebar.contains(event.target);
//         let isClickInsideMenuIcon = menuIcon.contains(event.target);

//         if (!isClickInsideSidebar && !isClickInsideMenuIcon) {
//             sidebar.style.transform = 'translateX(-300px)';
//         }
//     }
// });