//
//  ContentView.swift
//  Palera1n GUI
//
//  Created by Checkm8Croft on 27/09/24, modified by timi2506 on 20/10/24
//
import SwiftUI

struct ContentView: View {
    var body: some View {
        ZStack {
            // Full-screen gradient background
            LinearGradient(gradient: Gradient(colors: [.blue, .purple]),
                           startPoint: .top,
                           endPoint: .bottom)
                .ignoresSafeArea() // Make sure background spans the entire window
            
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
                
                Group {
                    Text("Rootful Mode")
                        .font(.title2)
                        .fontWeight(.semibold)
                        .foregroundColor(.white)
                    
                    HStack(spacing: 20) {
                        customButton(title: "Create FakeFS", action: { runScript(arguments: ["-f", "-c"]) })
                        customButton(title: "Create BindFS", action: { runScript(arguments: ["-f", "-B"]) })
                        customButton(title: "Boot Only", action: { runScript(arguments: ["-f"]) })
                        customButton(title: "Force Revert", action: { runScript(arguments: ["-f", "--force-revert"]) })
                    }
                    .padding(.bottom, 20)
                    
                    Text("Rootless and Exit Recovery")
                        .font(.title2)
                        .fontWeight(.semibold)
                        .foregroundColor(.white)
                    
                    HStack(spacing: 20) {
                        customButton(title: "Boot", action: { runScript(arguments: ["-l"]) })
                        customButton(title: "Force Revert", action: { runScript(arguments: ["-l", "--force-revert"]) })
                        customButton(title: "Exit Recovery", action: { runScript(arguments: ["-n"]) })
                    }
                }
            }
            .padding()
            .frame(width: 600)
        }
    }
    
    func runScript(arguments: [String]) {
        let scriptPath = Bundle.main.path(forResource: "Palera1n", ofType: "py")!
        let task = Process()
        task.launchPath = "/usr/bin/env"
        task.arguments = ["python3", scriptPath] + arguments
        task.launch()
    }
    
    // Custom Button with no grey background
    func customButton(title: String, action: @escaping () -> Void) -> some View {
        Button(action: action) {
            Text(title)
                .font(.headline)
                .frame(width: 120, height: 40)
                .foregroundColor(.white)
                .background(Color.blue.opacity(0.8))
                .cornerRadius(10)
                .shadow(radius: 5)
        }
        .buttonStyle(PlainButtonStyle()) // Removes default button style to avoid grey background
    }
}

#Preview {
    ContentView()
}
