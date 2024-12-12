function markAsRead(element, notificationId) {

    fetch(`/mark_notification_read/${notificationId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json',
        },
    })
    .then((response) => {
        if (response.ok) {
            element.classList.remove('unread');
            element.dataset.unread = "false";

            // Update the unread count
            const unreadTab = document.getElementById('unread-tab');
            let unreadCount = parseInt(unreadTab.innerText.match(/\d+/)) || 0;
            unreadTab.innerText = `Unread (${Math.max(0, unreadCount - 1)})`;
        }
    });
}
