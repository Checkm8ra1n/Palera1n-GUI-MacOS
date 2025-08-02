import SwiftUI

struct InstructionsView: View {
    var body: some View {
        VStack(spacing: 30) {
            
            // Rootful Block
            VStack(alignment: .leading, spacing: 10) {
                Text("Rootful Mode")
                    .font(.title2)
                    .fontWeight(.bold)
                    .foregroundColor(.blue)
                
                Text("• Deprecated mode for new tweaks, better to use Rootless.")
                Text("• To install Rootful, first click on Create FakeFS (BindFS is for 16GB devices).")
                Text("• Once you finish the process, you can proceed with the Boot Only button.")
            }
            .padding()
            .background(Color.blue.opacity(0.1))
            .cornerRadius(12)
            .frame(maxWidth: .infinity, alignment: .leading)
            
            // Rootless Block
            VStack(alignment: .leading, spacing: 10) {
                Text("Rootless Mode")
                    .font(.title2)
                    .fontWeight(.bold)
                    .foregroundColor(.green)
                
                Text("• The easiest and fastest option.")
                Text("• Just use the Boot button, keep your device connected to the network, and enjoy.")
            }
            .padding()
            .background(Color.green.opacity(0.1))
            .cornerRadius(12)
            .frame(maxWidth: .infinity, alignment: .leading)
        }
        .padding()
        .frame(maxWidth: 600)
    }
}

#Preview {
    InstructionsView()
}
