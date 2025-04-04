const socket = io();

socket.on('update', (data) => {
  const grid = document.getElementById("grid");
  grid.innerHTML = "";

  for (let y = 2; y >= 0; y--) {
    const row = document.createElement("div");
    row.style.display = "flex";

    for (let x = 0; x <= 2; x++) {
      const cell = document.createElement("div");
      cell.style.width = "80px";
      cell.style.height = "80px";
      cell.style.border = "1px solid black";
      cell.style.display = "flex";
      cell.style.alignItems = "center";
      cell.style.justifyContent = "center";

      const isEMV = data.emv[0] === x && data.emv[1] === y;
      const light = data.lights.find(l => l.position[0] === x && l.position[1] === y);

      if (isEMV) {
        cell.textContent = "🚑";
      } else if (light) {
        cell.style.backgroundColor = light.state === "green" ? "lightgreen" : "lightcoral";
        cell.textContent = light.role[0].toUpperCase();
      }

      row.appendChild(cell);
    }

    grid.appendChild(row);
  }

  const log = document.getElementById("log");
  log.innerHTML = data.log.map(line => `<div>${line}</div>`).join("");
});