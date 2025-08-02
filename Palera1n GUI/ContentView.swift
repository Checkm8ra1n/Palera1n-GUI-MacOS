import SwiftUI

struct ModeButtonStyle: ButtonStyle {
    var backgroundColor: Color
    var foregroundColor: Color = .white

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.headline)
            .frame(width: 120, height: 40)
            .foregroundColor(foregroundColor)
            .background(backgroundColor.opacity(configuration.isPressed ? 0.6 : 0.8))
            .cornerRadius(10)
            .shadow(radius: 5)
            .opacity(configuration.isPressed ? 0.9 : 1)
    }
}

struct ContentView: View {
    @State private var showInstructions = false

    var body: some View {
        ZStack {
            LinearGradient(gradient: Gradient(colors: [.blue, .purple]),
                           startPoint: .top,
                           endPoint: .bottom)
                .ignoresSafeArea()

            VStack(spacing: 20) {
                Image("Palera1n")
                    .resizable()
                    .frame(width: 150, height: 150)
                    .cornerRadius(15)
                    .shadow(radius: 10)
                    .padding(.top, 40)

                Text(NSLocalizedString("app_title", comment: "App Title"))
                    .font(.system(size: 32, weight: .bold, design: .rounded))
                    .foregroundColor(.white)
                    .padding(.bottom, 5)

                Text(NSLocalizedString("unofficial_project", comment: "Unofficial project text"))
                    .font(.headline)
                    .foregroundColor(.red)
                    .padding(.bottom, 20)

                VStack(spacing: 10) {
                    Text(NSLocalizedString("rootful_title", comment: "Rootful Title"))
                        .font(.title2)
                        .fontWeight(.semibold)
                        .foregroundColor(.blue)

                    HStack(spacing: 20) {
                        Button(NSLocalizedString("create_fakefs", comment: "Create FakeFS")) {
                            runScript(arguments: ["-f", "-c"])
                        }
                        .buttonStyle(ModeButtonStyle(backgroundColor: .blue))

                        Button(NSLocalizedString("create_bindfs", comment: "Create BindFS")) {
                            runScript(arguments: ["-f", "-B"])
                        }
                        .buttonStyle(ModeButtonStyle(backgroundColor: .blue))

                        Button(NSLocalizedString("boot_only", comment: "Boot Only")) {
                            runScript(arguments: ["-f"])
                        }
                        .buttonStyle(ModeButtonStyle(backgroundColor: .blue))

                        Button(NSLocalizedString("force_revert", comment: "Force Revert")) {
                            runScript(arguments: ["-f", "--force-revert"])
                        }
                        .buttonStyle(ModeButtonStyle(backgroundColor: .blue))
                    }
                }
                .padding(.bottom, 20)

                VStack(spacing: 10) {
                    Text(NSLocalizedString("rootless_title", comment: "Rootless Title"))
                        .font(.title2)
                        .fontWeight(.semibold)
                        .foregroundColor(.green)

                    HStack(spacing: 20) {
                        Button(NSLocalizedString("boot", comment: "Boot")) {
                            runScript(arguments: ["-l"])
                        }
                        .buttonStyle(ModeButtonStyle(backgroundColor: .green))

                        Button(NSLocalizedString("force_revert", comment: "Force Revert")) {
                            runScript(arguments: ["-l", "--force-revert"])
                        }
                        .buttonStyle(ModeButtonStyle(backgroundColor: .green))

                        Button(NSLocalizedString("exit_recovery", comment: "Exit Recovery")) {
                            runScript(arguments: ["-n"])
                        }
                        .buttonStyle(ModeButtonStyle(backgroundColor: .green))
                    }
                }

                HStack {
                    Button(NSLocalizedString("instruction_button", comment: "Show Instructions")) {
                        showInstructions = true
                    }
                    .foregroundColor(.white)
                    .padding(.top, 10)
                }
                .frame(maxWidth: .infinity, alignment: .trailing)
                .padding(.trailing)
            }
            .padding()
            .frame(width: 600)
        }
        .sheet(isPresented: $showInstructions) {
            InstructionsView()
                .background(Color.black)
        }
    }

    func runScript(arguments: [String]) {
        guard let scriptPath = Bundle.main.path(forResource: "Palera1n", ofType: "py") else {
            print("Script not found")
            return
        }

        let argsString = arguments.joined(separator: " ")
        let command = "python3 '\(scriptPath)' \(argsString)"
        
        let appleScript = """
        tell application "Terminal"
            activate
            if (count of windows) is 0 then
                do script "\(command)"
            else
                do script "\(command)" in front window
            end if
        end tell
        """
        
        let task = Process()
        task.launchPath = "/usr/bin/osascript"
        task.arguments = ["-e", appleScript]
        task.launch()
    }



}

#Preview {
    ContentView()
}
