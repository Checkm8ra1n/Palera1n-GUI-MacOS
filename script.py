from flask import Flask, jsonify, send_from_directory
import subprocess
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/create_fakefs', methods=['POST'])
def create_fakefs():
    return execute_command('palera1n -f -c; exit')

@app.route('/create_bindfs', methods=['POST'])
def create_bindfs():
    return execute_command('palera1n -f -B; exit')

@app.route('/boot_only', methods=['POST'])
def boot_only():
    return execute_command('palera1n -f; exit')

@app.route('/force_revert', methods=['POST'])
def force_revert():
    return execute_command('palera1n -f --force-revert; exit')

@app.route('/boot_rootless', methods=['POST'])
def boot_rootless():
    return execute_command('palera1n -l; exit')

@app.route('/force_revertl', methods=['POST'])
def force_revertl():
    return execute_command('palera1n -l --force-revert; exit')

@app.route('/exit_recovery', methods=['POST'])
def exit_recovery():
    return execute_command('palera1n -n; exit')

def execute_command(command):
    try:
        # Se il sistema è macOS
        if sys.platform.startswith('darwin'):
            # Aprire una nuova finestra del terminale e eseguire il comando
            subprocess.Popen(['osascript', '-e', f'tell application "Terminal" to do script "{command}"'])
        elif sys.platform.startswith('linux'):
            # Aprire una nuova finestra del terminale su Linux
            subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', command])
        
        return jsonify({'message': 'Command executed in a new terminal!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
