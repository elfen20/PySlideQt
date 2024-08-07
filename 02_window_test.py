# Create a window with qt
import sys
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QKeyEvent, QResizeEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

# main window class
class MainForm(QMainWindow):
    
    onKeyPressed = Signal(int)

    def __init__(self):
        super().__init__()
        self.resize(500,500)

        self.lHello = QLabel(self)
        self.lHello.setText("Hello World")

        self.onKeyPressed.connect(self.qFormKeyPressed)

        self.show()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        self.onKeyPressed.emit(event.key())
        return super().keyPressEvent(event)
    
    def toggleFullScreen(self):
        print(self.windowState())
        if self.windowState() == Qt.WindowState.WindowFullScreen:
            self.showNormal()
        else:
            self.showFullScreen()

    @Slot()
    def qFormKeyPressed(self, key: int):
        # print(f"Key pressed: [{key}]")
        match key:
            case Qt.Key.Key_F11:
                self.toggleFullScreen()
            case Qt.Key.Key_Escape:
                self.close()

# main function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MainForm()
    sys.exit(app.exec())