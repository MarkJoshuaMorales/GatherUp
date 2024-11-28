document.getElementById('location-selector').addEventListener('change', function handleLocationChange() {
    const container = document.querySelector('.location-container');
    const selectorValue = this.value;

    if (selectorValue === 'offline') {
        
        container.innerHTML = `
            <input type="text" class="location-input" placeholder="Enter On-site Address">
        `;
    } else if (selectorValue === 'online') {
        
        container.innerHTML = `
            <input type="text" class="location-input" placeholder="Enter Online Link">
        `;
    } else {
        
        container.innerHTML = `
            <select class="location-type" id="location-selector">
                <option value="online">Online Link</option>
                <option value="offline">On-site Address</option>
            </select>
        `;

        
        const newSelector = document.getElementById('location-selector');
        if (newSelector) {
            newSelector.addEventListener('change', handleLocationChange);
        }
    }
});

document.getElementById('ticket-input').addEventListener('input', function () {
    const ticketPrice = parseFloat(this.value);
    const ticketType = ticketPrice === 0 ? "Free" : "Paid";

   
    console.log(`Ticket Type: ${ticketType} (${ticketPrice})`);
});



