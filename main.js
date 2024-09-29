const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow () {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'), // opzionale, se hai un file preload
            contextIsolation: true,
            enableRemoteModule: false,
            nodeIntegration: true // Importante per usare Node.js nel tuo HTML
        }
    });

    win.loadURL('http://127.0.0.1:5000/'); // URL del tuo server Flask
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});
