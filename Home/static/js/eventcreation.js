document.getElementById('ticket-input').addEventListener('input', function () {
    const ticketPrice = parseFloat(this.value);
    const ticketType = ticketPrice === 0 ? "Free" : "Paid";

   
    console.log(`Ticket Type: ${ticketType} (${ticketPrice})`);
});



