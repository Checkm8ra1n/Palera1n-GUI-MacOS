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

                Text("Palera1n GUI")
                    .font(.system(size: 32, weight: .bold, design: .rounded))
                    .foregroundColor(.white)
                    .padding(.bottom, 5)

                Text("Unofficial Project!")
                    .font(.headline)
                    .foregroundColor(.red)
                    .padding(.bottom, 20)

                VStack(spacing: 10) {
                    Text("Rootful Mode")
                        .font(.title2)
                        .fontWeight(.semibold)
                        .foregroundColor(.blue)

                    HStack(spacing: 20) {
                        Button("Create FakeFS") {
                            runScript(arguments: ["-f", "-c"])
                        }
                        .buttonStyle(ModeButtonStyle(backgroundColor: .blue))

                        Button("Create BindFS") {
                            runScript(arguments: ["-f", "-B"])
                        }
                        .buttonStyle(ModeButtonStyle(backgroundColor: .blue))

                        Button("Boot Only") {
                            runScript(arguments: ["-f"])
                        }
                        .buttonStyle(ModeButtonStyle(backgroundColor: .blue))

                        Button("Force Revert") {
                            runScript(arguments: ["-f", "--force-revert"])
                        }
                        .buttonStyle(ModeButtonStyle(backgroundColor: .blue))
                    }
                }
                .padding(.bottom, 20)

                VStack(spacing: 10) {
                    Text("Rootless Mode")
                        .font(.title2)
                        .fontWeight(.semibold)
                        .foregroundColor(.green)

                    HStack(spacing: 20) {
                        Button("Boot") {
                            runScript(arguments: ["-l"])
                        }
                        .buttonStyle(ModeButtonStyle(backgroundColor: .green))

                        Button("Force Revert") {
                            runScript(arguments: ["-l", "--force-revert"])
                        }
                        .buttonStyle(ModeButtonStyle(backgroundColor: .green))

                        Button("Exit Recovery") {
                            runScript(arguments: ["-n"])
                        }
                        .buttonStyle(ModeButtonStyle(backgroundColor: .green))
                    }
                }

                HStack {
                    Button("Don't know which to use?") {
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
