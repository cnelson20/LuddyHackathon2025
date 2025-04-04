const socket = io();

socket.on('state_update', (data) => {
    document.getElementById('grid').innerText = JSON.stringify(data, null, 2);
});