// Test

console.log("Test Base.js");

//?Menu Toogle 


// Menu Icon 

function toggleSidebar() {
    let sidebar = document.querySelector('#sidebar');
    if (window.innerWidth < 1024) {
        sidebar.style.transform = (sidebar.style.transform === 'translateX(0px)') ? 'translateX(-300px)' : 'translateX(0px)';
    }
}

document.addEventListener('click', function(event) {
    if (window.innerWidth < 1024) {
        let sidebar = document.querySelector('#sidebar');
        let menuIcon = document.querySelector('#menuIcon');
        let isClickInsideSidebar = sidebar.contains(event.target);
        let isClickInsideMenuIcon = menuIcon.contains(event.target);

        if (!isClickInsideSidebar && !isClickInsideMenuIcon) {
            sidebar.style.transform = 'translateX(-300px)';
        }
    }
});

// Notifications 

function toggleNotification() {
    let sidebar = document.querySelector('#notifications');
    
        sidebar.style.transform = (sidebar.style.transform === 'translateX(0px)') ? 'translateX(300px)' : 'translateX(0px)';
    
}

document.addEventListener('click', function(event) {
    
        let sidebar = document.querySelector('#notifications');
        let menuIcon = document.querySelector('#notificationsIcon');
        let isClickInsideSidebar = sidebar.contains(event.target);
        let isClickInsideMenuIcon = menuIcon.contains(event.target);

        if (!isClickInsideSidebar && !isClickInsideMenuIcon) {
            sidebar.style.transform = 'translateX(300px)';
        }
    
});
let closeNotificationsBar = document.getElementById("closeNotificationsBar");
closeNotificationsBar.addEventListener("click",function(){
    let sidebar = document.querySelector('#notifications');
    sidebar.style.transform = 'translateX(300px)';
})
// Toogle Acocunt

function toggleAccount() {
    let sidebar = document.querySelector('#accountSidebar');
    
        sidebar.style.transform = (sidebar.style.transform === 'translateX(0px)') ? 'translateX(300px)' : 'translateX(0px)';
    
}

document.addEventListener('click', function(event) {
    
        let sidebar = document.querySelector('#accountSidebar');
        let menuIcon = document.querySelector('#account');
        let isClickInsideSidebar = sidebar.contains(event.target);
        let isClickInsideMenuIcon = menuIcon.contains(event.target);

        if (!isClickInsideSidebar && !isClickInsideMenuIcon) {
            sidebar.style.transform = 'translateX(300px)';
        }
    
});
// let c = document.getElementById("closeNotificationsBar");
// closeNotificationsBar.addEventListener("click",function(){
//     let sidebar = document.querySelector('#notifications');
//     sidebar.style.transform = 'translateX(300px)';
// })
//? Sidebar js 

// Get all sidebar tabs
const sidebarTabs = document.querySelectorAll('#sidebar > .tab');

// Loop through each tab and add click event listener
sidebarTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        // Remove 'bg-[#202020]' class from all tabs
        sidebarTabs.forEach(t => {
            t.classList.remove('bg-[#202020]');
        });

        // Add 'bg-[#202020]' class to the clicked tab
        tab.classList.add('bg-[#202020]');

        // Redirect to the corresponding page based on tab id
        const tabId = tab.id;
        redirectToPage(tabId);
    });
});

// Function to redirect to corresponding page based on tab id
function redirectToPage(tabId) {
    // Implement redirection logic based on tab id
    switch (tabId) {
        case 'home':
            window.location.href = '/templates/index.html'; // Replace 'home.html' with actual URL of your home page
            break;
        case 'members':
            window.location.href = '/templates/members.html'; // Replace 'members.html' with actual URL of your members page
            break;
        case 'products':
            window.location.href = '/templates/products.html'; // Replace 'products.html' with actual URL of your products page
            break;
        case 'mailing':
            window.location.href = '/templates/mailing.html'; // Replace 'mailing.html' with actual URL of your mailing page
            break;
        case 'analytics':
            window.location.href = '/templates/analytics.html'; // Replace 'analytics.html' with actual URL of your analytics page
            break;
        case 'attendance':
            window.location.href = '/templates/attendance.html'; // Replace 'attendance.html' with actual URL of your attendance page
            break;
        case 'store':
            window.location.href = '/templates/store.html'; // Replace 'attendance.html' with actual URL of your attendance page
            break;
        case 'settings':
            window.location.href = '/templates/settings.html'; // Replace 'attendance.html' with actual URL of your attendance page
            break;
        default:
            break;
    }
}

