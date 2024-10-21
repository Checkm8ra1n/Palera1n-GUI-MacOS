//
//  Palera1n_GUIApp.swift
//  Palera1n GUI
//
//  Created by Checkm8Croft on 27/09/24.
//

import SwiftUI

@main
struct Palera1n_GUIApp: App {
    // Use an AppDelegate to manage window configurations
    @NSApplicationDelegateAdaptor(AppDelegate.self) var appDelegate
    
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

class AppDelegate: NSObject, NSApplicationDelegate {
    var window: NSWindow?
    
    func applicationDidFinishLaunching(_ notification: Notification) {
        if let window = NSApplication.shared.windows.first {
            // Set the window size to 2024x1500
            window.setContentSize(NSSize(width: 700, height: 600))
            window.styleMask.insert(.resizable) // Ensure the window is resizable
            window.center() // Center the window on the screen
        }
    }
}
