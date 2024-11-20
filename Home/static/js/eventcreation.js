document.getElementById('location-selector').addEventListener('change', function () {
    const container = document.querySelector('.location-container');
    if (this.value === 'offline') {
        container.innerHTML = `
            <input type="text" class="location-input" placeholder="Enter offline address">
        `;
    } else {
        container.innerHTML = `
            <select class="location-type" id="location-selector">
                <option value="online">Online Link</option>
                <option value="offline">Offline Address</option>
            </select>
        `;
        document.getElementById('location-selector').addEventListener('change', arguments.callee);
    }
});