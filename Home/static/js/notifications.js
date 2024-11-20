function showTab(tabName) {
    const tabs = document.querySelectorAll(".tab");
    const notifications = document.querySelectorAll(".notifications");

    tabs.forEach(tab => tab.classList.remove("active"));
    notifications.forEach(notification => (notification.style.display = "none"));

    document.getElementById(tabName).style.display = "block";
    document.querySelector(`[onclick="showTab('${tabName}')"]`).classList.add("active");
}

function markAsRead(notificationCard) {
    if (notificationCard.classList.contains("unread")) {
        
        notificationCard.classList.remove("unread");
        notificationCard.removeAttribute("data-unread");
        notificationCard.style.backgroundColor = "#f9f9f9"; 

        
        unreadCount--;
        document.getElementById("unread-tab").innerText = `Unread (${unreadCount})`;

        
        if (document.getElementById("unread").style.display === "block") {
            notificationCard.style.display = "none";
        }
    }
}