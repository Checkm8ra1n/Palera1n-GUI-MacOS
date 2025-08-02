import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QMessageBox
)
from PySide6.QtGui import QPixmap, QPalette, QColor, QLinearGradient, QBrush, QFont
from PySide6.QtCore import Qt, QProcess
import shutil



class Palera1nGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Palera1n GUI")
        self.setFixedSize(600, 700)

        self.setupUI()
        self.setGradientBackground()

    def setupUI(self):
        layout = QVBoxLayout()

        # Logo
        logo = QLabel()
        pixmap = QPixmap("Palera1n.png").scaled(180, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo)

        # Title
        title = QLabel("Palera1n GUI")
        title.setFont(QFont("Arial", 28, QFont.Bold))
        title.setStyleSheet("color: white;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Subtitle
        subtitle = QLabel("Unofficial Project!")
        subtitle.setStyleSheet("color: red; font-size: 18px;")
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)

        layout.addSpacing(25)

        # Rootful Section
        rootful_title = QLabel("Rootful Mode")
        rootful_title.setFont(QFont("Arial", 20, QFont.Bold))
        rootful_title.setStyleSheet("color: #66ccff;")
        rootful_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(rootful_title)

        rootful_buttons = self.createButtonRow([
            ("Create FakeFS", ["-f", "-c"]),
            ("Create BindFS", ["-f", "-B"]),
            ("Boot Only", ["-f"]),
            ("Force Revert", ["-f", "--force-revert"]),
        ], color="#007BFF")
        layout.addLayout(rootful_buttons)
        layout.addSpacing(30)

        # Rootless Section
        rootless_title = QLabel("Rootless Mode & Exit Recovery")
        rootless_title.setFont(QFont("Arial", 20, QFont.Bold))
        rootless_title.setStyleSheet("color: #66ff66;")
        rootless_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(rootless_title)

        rootless_buttons = self.createButtonRow([
            ("Boot", ["-l"]),
            ("Force Revert", ["-l", "--force-revert"]),
            ("Exit Recovery", ["-n"]),
        ], color="#28a745")
        layout.addLayout(rootless_buttons)

        # Instructions button aligned right
        instr_layout = QHBoxLayout()
        instr_layout.addStretch()
        help_btn = QPushButton("Don't know which to use?")
        help_btn.setStyleSheet("background-color: gray; color: white; padding: 6px 18px; border-radius: 12px; font-weight: bold;")
        help_btn.clicked.connect(self.showInstructions)
        instr_layout.addWidget(help_btn)
        layout.addLayout(instr_layout)

        self.setLayout(layout)

    def createButtonRow(self, button_defs, color):
        row = QHBoxLayout()
        for label, args in button_defs:
            btn = QPushButton(label)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: white;
                    padding: 12px;
                    border-radius: 10px;
                    font-weight: bold;
                }}
                QPushButton:hover {{
                    background-color: #555;
                }}
            """)
            btn.clicked.connect(lambda _, a=args: self.runScript(a))
            row.addWidget(btn)
        return row

    def runScript(self, arguments):
        import shutil
        python_path = shutil.which("python3") or "python3"
        palera1n_path = "Palera1n.py"  # o percorso assoluto

        cmd = [python_path, palera1n_path] + arguments
        terminal = shutil.which("gnome-terminal")
        if terminal:
            full_cmd = [terminal, "--"] + cmd
            print("Running:", full_cmd)
            # terminal + args
            QProcess.startDetached(full_cmd[0], full_cmd[1:])
        else:
            print("gnome-terminal not found, running without terminal")
            QProcess.startDetached(cmd[0], cmd[1:])



    def showInstructions(self):
        QMessageBox.information(self, "Instructions",
            "Rootful mode:\n"
            "- Deprecated for new tweaks, better to use Rootless.\n"
            "- First click on 'Create FakeFS' (or 'BindFS' for 16GB devices).\n"
            "- Then click 'Boot Only'.\n\n"
            "Rootless mode:\n"
            "- Easiest and fastest. Just click 'Boot' and make sure your device is on the network."
        )

    def setGradientBackground(self):
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#3a7bd5"))
        gradient.setColorAt(1.0, QColor("#6a3093"))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setAutoFillBackground(True)
        self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Palera1nGUI()
    window.show()
    sys.exit(app.exec())
