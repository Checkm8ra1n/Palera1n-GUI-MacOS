import sys
import subprocess
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QSpacerItem, QSizePolicy
)
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor
from PySide6.QtCore import Qt


def run_palera1n(arguments):
    try:
        subprocess.Popen(["python3", "Palera1n.py"] + arguments)
    except Exception as e:
        print(f"Error running Palera1n.py: {e}")


class InstructionsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instructions")
        self.setFixedSize(450, 220)

        layout = QVBoxLayout()

        rootful = QLabel("Rootful Mode:\n"
                         "Deprecated mode for new tweaks. Use only if necessary.\n"
                         "Use 'Create FakeFS' (or 'BindFS' for 16GB devices), then 'Boot Only'.")
        rootful.setWordWrap(True)
        rootful.setStyleSheet("color: #2A73FF; font-weight: bold;")
        layout.addWidget(rootful)

        rootless = QLabel("Rootless Mode:\n"
                          "Recommended for modern jailbreaks.\n"
                          "Simply click 'Boot', make sure your device is connected to the network.")
        rootless.setWordWrap(True)
        rootless.setStyleSheet("color: #1DC690; font-weight: bold;")
        layout.addWidget(rootless)

        self.setLayout(layout)


class Palera1nGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Palera1n GUI")
        self.setFixedSize(600, 500)

        # Background like SwiftUI
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#0c0c0e"))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        # Image
        image = QLabel()
        image_path = os.path.join(os.path.dirname(__file__), "palera1n.png")
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            image.setPixmap(pixmap)
            image.setAlignment(Qt.AlignCenter)
            layout.addWidget(image)

        # Title
        title = QLabel("Palera1n GUI")
        title.setFont(QFont("Arial", 24, QFont.Bold))
        title.setStyleSheet("color: white;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        subtitle = QLabel("Unofficial Project")
        subtitle.setStyleSheet("color: red;")
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)

        # Rootful section
        layout.addLayout(self.create_section(
            "Rootful Mode", "#2A73FF",
            [("Create FakeFS", ["-f", "-c"]),
             ("Create BindFS", ["-f", "-B"]),
             ("Boot Only", ["-f"]),
             ("Force Revert", ["-f", "--force-revert"])]
        ))

        # Rootless section
        layout.addLayout(self.create_section(
            "Rootless Mode", "#1DC690",
            [("Boot", ["-l"]),
             ("Force Revert", ["-l", "--force-revert"]),
             ("Exit Recovery", ["-n"])]
        ))

        # Bottom right button
        bottom_row = QHBoxLayout()
        bottom_row.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        instructions_btn = QPushButton("Instructions")
        instructions_btn.clicked.connect(self.show_instructions)
        bottom_row.addWidget(instructions_btn)
        layout.addLayout(bottom_row)

        self.setLayout(layout)

    def create_section(self, title, color, buttons):
        section_layout = QVBoxLayout()

        label = QLabel(title)
        label.setFont(QFont("Arial", 16, QFont.Bold))
        label.setStyleSheet(f"color: {color};")
        section_layout.addWidget(label)

        btn_row = QHBoxLayout()
        for btn_text, args in buttons:
            btn = QPushButton(btn_text)
            btn.setStyleSheet(f"""
                background-color: {color};
                color: white;
                border-radius: 10px;
                height: 40px;
            """)
            btn.clicked.connect(lambda _, a=args: run_palera1n(a))
            btn_row.addWidget(btn)

        section_layout.addLayout(btn_row)
        return section_layout

    def show_instructions(self):
        self.instructions_window = InstructionsWindow()
        self.instructions_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Palera1nGUI()
    window.show()
    sys.exit(app.exec())
