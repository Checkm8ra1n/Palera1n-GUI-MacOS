import subprocess

def get_device_info():
    try:
        # Esegui il comando 'ideviceinfo'
        device_info_output = subprocess.check_output(["ideviceinfo"], universal_newlines=True)
        
        # Analizza l'output
        lines = device_info_output.strip().split("\n")
        device_model = None
        ios_version = None
        for line in lines:
            if line.startswith("ProductType:"):
                device_model = line.split(": ")[1]
            elif line.startswith("ProductVersion:"):
                ios_version = line.split(": ")[1]

        # Stampa per il debug
        print(f"Device Model: {device_model}, iOS Version: {ios_version}")
        
        return device_model, ios_version
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_device_info()
