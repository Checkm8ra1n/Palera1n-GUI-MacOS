import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Image("Palera1n")
                .resizable()
                .frame(width: 150, height: 150)
                .cornerRadius(10)
            Text("Palera1n GUI")
                .font(.title)
                .fontWeight(.bold)
                .padding()
            Text("Unofficial Project!")
                .foregroundColor(.red)
                .padding()
            Group {
                Text("Rootlful")
                    .padding()
                HStack {
                    Button("Create FakeFS") {
                        runScript(arguments: ["-f", "-c"])
                    }
                    Button("Create BindFS") {
                        runScript(arguments: ["-f", "-B"])
                    }
                    Button("Boot Only") {
                        runScript(arguments: ["-f"])
                    }
                    Button("Force Revert") {
                        runScript(arguments: ["-f", "--force-revert"])
                    }
                }
                .padding()
                Text("Rootless & More")
                    .padding()
                HStack {
                    Button("Boot") {
                        runScript(arguments: ["-l"])
                    }
                    Button("Force Revert") {
                        runScript(arguments: ["-l", "--force-revert"])
                    }
                    Button("Exit Recovery") {
                        runScript(arguments: ["-n"])
                    }
                }
            }
        }
        .padding()
        .frame(width: 512.0)
    }
    
    func runScript(arguments: [String]) {
        // Esegui lo script Python o il comando desiderato
        let scriptPath = Bundle.main.path(forResource: "Palera1n", ofType: "py")!
        let task = Process()
        task.launchPath = "/usr/bin/env"
        task.arguments = ["python3", scriptPath] + arguments
        
        task.launch()
    }
}

#Preview {
    ContentView()
}
