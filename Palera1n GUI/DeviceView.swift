import SwiftUI

struct DeviceView: View {
    @State private var deviceModel: String = "N/A"
    @State private var iosVersion: String = "N/A"
    @State private var isSupported: Bool = false
    @State private var statusColor: Color = .red

    var body: some View {
        VStack {
            Text("Model: \(deviceModel)")
            Text("iOS Version: \(iosVersion)")
            Text("Supported: \(isSupported ? "Yes" : "No")")
                .foregroundColor(isSupported ? .green : .red)

            Button("Check Device Info") {
                checkDeviceInfo()
            }
        }
        .padding()
    }

    func checkDeviceInfo() {
        let task = Process()
        task.launchPath = "/opt/local/bin/ideviceinfo"
        task.arguments = []

        let pipe = Pipe()
        task.standardOutput = pipe

        task.terminationHandler = { _ in
            let data = pipe.fileHandleForReading.readDataToEndOfFile()
            if let output = String(data: data, encoding: .utf8) {
                parseDeviceInfo(output)
            }
        }

        task.launch()
    }

    func parseDeviceInfo(_ output: String) {
        let lines = output.split(separator: "\n").map { String($0) }
        var model: String?
        var version: String?
        
        for line in lines {
            if line.contains("ProductType:") {
                model = String(line.split(separator: ":")[1]).trimmingCharacters(in: .whitespaces)
            }
            if line.contains("ProductVersion:") {
                version = String(line.split(separator: ":")[1]).trimmingCharacters(in: .whitespaces)
            }
        }

        deviceModel = model ?? "N/A"
        iosVersion = version ?? "N/A"
        checkSupport()
    }

    func checkSupport() {
        let supportedModels = ["iPad6,11", "iPad6,12", "iPad7,5", "iPad7,6", "iPad7,12", "iPad7,11", "iPad5,3", "iPad5,4", "iPad5,1", "iPad5,2", "iPad6,7", "iPad6,8", "iPad6,4", "iPad6,3", "iPad7,1", "iPad7,2"]
        
        // Check for iPhone models in range
        if deviceModel.starts(with: "iPhone"), let modelNumber = deviceModel.components(separatedBy: ",").last, let majorVersion = Int(modelNumber) {
            let majorModel = deviceModel.components(separatedBy: ",")[0].dropFirst(6) // Extract the iPhone model number
            if let modelInt = Int(majorModel) {
                if modelInt >= 7 && modelInt <= 10 { // iPhone 7,2 to iPhone 10,6 range
                    isSupported = true
                    statusColor = .green
                    return
                }
            }
        }

        // Check if the iPad is in the supported list
        if supportedModels.contains(deviceModel) {
            isSupported = true
            statusColor = .green
        } else {
            isSupported = false
            statusColor = .red
        }
    }
}
