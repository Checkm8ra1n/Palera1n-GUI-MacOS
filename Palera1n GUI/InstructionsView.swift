import SwiftUI

struct InstructionsView: View {
    var body: some View {
        VStack(spacing: 30) {
            VStack(alignment: .leading, spacing: 10) {
                Text(NSLocalizedString("rootful_title", comment: "Rootful Title"))
                    .font(.title2)
                    .fontWeight(.bold)
                    .foregroundColor(.blue)

                Text("• \(NSLocalizedString("rootful_1", comment: "Rootful instruction 1"))")
                Text("• \(NSLocalizedString("rootful_2", comment: "Rootful instruction 2"))")
                Text("• \(NSLocalizedString("rootful_3", comment: "Rootful instruction 3"))")
            }
            .padding()
            .background(Color.blue.opacity(0.1))
            .cornerRadius(12)
            .frame(maxWidth: .infinity, alignment: .leading)

            VStack(alignment: .leading, spacing: 10) {
                Text(NSLocalizedString("rootless_title", comment: "Rootless Title"))
                    .font(.title2)
                    .fontWeight(.bold)
                    .foregroundColor(.green)

                Text("• \(NSLocalizedString("rootless_1", comment: "Rootless instruction 1"))")
                Text("• \(NSLocalizedString("rootless_2", comment: "Rootless instruction 2"))")
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
