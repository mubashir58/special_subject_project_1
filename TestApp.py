import sys
from PyQt5.QtCore import QTimer, Qt, QPoint
from PyQt5.QtWidgets import (
    QApplication, QDialog, QFileDialog, QFrame, QLineEdit, QMessageBox, QProgressBar, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
)


class CustomHeader(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setFixedHeight(35)
        self.setStyleSheet("background-color: lightgray;")

        layout = QHBoxLayout()
        layout.setContentsMargins(5, 0, 5, 0)

        # Left-side app buttons
        self.search_btn = QPushButton("Search File")
        self.help_btn = QPushButton("Help")
        self.about_btn = QPushButton("About")

        for btn in [self.search_btn, self.help_btn, self.about_btn]:
            btn.setFixedHeight(25)
            btn.setStyleSheet("background-color: white; border: 1px solid black;")

        layout.addWidget(self.search_btn)
        layout.addWidget(self.help_btn)
        layout.addWidget(self.about_btn)
        layout.addStretch()

        self.search_btn.clicked.connect(parent.open_search_window)
        self.help_btn.clicked.connect(parent.open_help_window)
        self.about_btn.clicked.connect(parent.open_about_window)


        # Window control buttons
        self.minimize_btn = QPushButton("–")
        self.maximize_btn = QPushButton("□")
        self.close_btn = QPushButton("X")

        for btn in [self.minimize_btn, self.maximize_btn, self.close_btn]:
            btn.setFixedSize(25, 25)
            btn.setStyleSheet("background-color: white; border: 1px solid black;")

        layout.addWidget(self.minimize_btn)
        layout.addWidget(self.maximize_btn)
        layout.addWidget(self.close_btn)

        self.setLayout(layout)

        # Connections
        self.close_btn.clicked.connect(parent.close)
        self.minimize_btn.clicked.connect(parent.showMinimized)
        self.maximize_btn.clicked.connect(self.toggle_max_restore)

    def toggle_max_restore(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
        else:
            self.parent.showMaximized()

class BaseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.old_pos = None
        self.selected_files = []

    # === Перемещение окна ===
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = QPoint(event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.old_pos = None

    # === Общие методы, вызываемые CustomHeader ===
    def open_search_window(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select one or more log files",
            "",
            "Log Files (*.log);;All Files (*)"
        )
        if files:
            self.selected_files = files
            self.user_choice_window = UserChoiceWindow(files)
            self.user_choice_window.show()
            self.close()
        else:
            self.selected_files = []

    def open_help_window(self):
        self.help_window = HelpWindow()
        self.help_window.show()

    def open_about_window(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    def show_user_choice(self, parent_dialog):
        parent_dialog.accept()
        QMessageBox.information(self, "User's Choice", "You selected a file!")



class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMinimumSize(800, 600)
        self.selected_files = []  # переменная для хранения выбранных файлов

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.header = CustomHeader(self)
        layout.addWidget(self.header)

        # Main content label
        content_1 = QLabel("1. 'Search File' button opens the user directory to choose a file or files for analyzing")
        content_2 = QLabel("2. 'Help' button opens a new window where user can search error codes to find reasons and corrective actions")
        content_3 = QLabel("3. 'About' button shows the main information about system and mapping table's version")

        contents = [content_1,content_2, content_3]

        for content in contents: 
            content.setAlignment(Qt.AlignCenter)
            content.setStyleSheet("font-size: 16px;")
            layout.addWidget(content)

        self.setLayout(layout)
        self.setStyleSheet("background-color: #dcdcdc;")


class HelpWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: #dcdcdc;")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.header = CustomHeader(self)
        layout.addWidget(self.header)

        # Центрированный текстовый блок
        content_label = QLabel("Help content will be added here soon.")
        content_label.setAlignment(Qt.AlignCenter)
        content_label.setStyleSheet("font-size: 18px; padding: 40px;")

        layout.addWidget(content_label)
        self.setLayout(layout)


class AboutWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: #dcdcdc;")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.header = CustomHeader(self)
        layout.addWidget(self.header)

        # Центрированный текстовый блок
        content_label = QLabel("About content will be added here soon.")
        content_label.setAlignment(Qt.AlignCenter)
        content_label.setStyleSheet("font-size: 18px; padding: 40px;")

        layout.addWidget(content_label)
        self.setLayout(layout)


class UserChoiceWindow(BaseWindow):
    def __init__(self, selected_files):
        super().__init__()
        self.selected_files = selected_files
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: #dcdcdc;")

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(20)

        # === Заголовок ===
        self.header = CustomHeader(self)
        main_layout.addWidget(self.header)

        # === Центрированная панель с кнопками ===
        center_container = QWidget()
        center_layout = QVBoxLayout(center_container)
        center_layout.setAlignment(Qt.AlignCenter)

        panel = QFrame()
        panel.setStyleSheet("background-color: #bbbbbb; border: 2px solid gray;")
        panel.setFixedSize(300, 250)

        panel_layout = QVBoxLayout(panel)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(20)

        # Кнопки
        self.manual_btn = QPushButton("Manual")
        self.auto_btn = QPushButton("Auto")
        self.home_btn = QPushButton("Home")

        for btn in [self.manual_btn, self.auto_btn, self.home_btn]:
            btn.setFixedHeight(40)
            btn.setStyleSheet("background-color: white; border: 1px solid black; font-size: 16px;")
            panel_layout.addWidget(btn)

        center_layout.addWidget(panel)
        main_layout.addWidget(center_container, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)

        # Логика
        self.manual_btn.clicked.connect(self.open_manual)
        self.auto_btn.clicked.connect(self.open_auto)
        self.home_btn.clicked.connect(self.back_to_main)

    def open_manual(self):
        self.manual_window = ManualModeWindow(self.selected_files)
        self.manual_window.show()
        self.close()

    def open_auto(self):
        self.analysis_window = AnalyzingWindow(self.selected_files)
        self.analysis_window.show()
        self.close()


    def back_to_main(self):
        self.selected_files.clear()
        self.close()
        self.main_window = MainWindow()
        self.main_window.show()


class ManualModeWindow(BaseWindow):
    def __init__(self, selected_files):
        super().__init__()
        self.selected_files = selected_files
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: #dcdcdc;")

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(20)

        # Header
        self.header = CustomHeader(self)
        main_layout.addWidget(self.header)

        # Центрированный контейнер
        center_container = QWidget()
        center_layout = QVBoxLayout(center_container)
        center_layout.setAlignment(Qt.AlignCenter)

        panel = QFrame()
        panel.setFixedSize(400, 250)
        panel.setStyleSheet("background-color: #bbbbbb; border: 2px solid gray;")

        panel_layout = QVBoxLayout(panel)
        panel_layout.setContentsMargins(20, 20, 20, 20)
        panel_layout.setSpacing(20)

        # Input
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Input Search Text")  # ✅ дефолтный текст
        self.input_field.setStyleSheet("font-size: 16px; padding: 5px;")
        panel_layout.addWidget(self.input_field)

        # Кнопки
        button_row = QHBoxLayout()
        button_names = [("Start Search", self.start_search),
                        ("Back", self.go_back),
                        ("Home", self.go_home)]

        for name, handler in button_names:
            btn = QPushButton(name)
            btn.setFixedHeight(35)
            btn.setStyleSheet("background-color: white; border: 1px solid black; font-size: 14px;")
            btn.clicked.connect(handler)
            button_row.addWidget(btn)

        panel_layout.addLayout(button_row)
        center_layout.addWidget(panel)
        main_layout.addWidget(center_container, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)

    def start_search(self):
        self.analysis_window = AnalyzingWindow(self.selected_files)
        self.analysis_window.show()
        self.close()

    def go_back(self):
        self.user_choice_window = UserChoiceWindow(self.selected_files)
        self.user_choice_window.show()
        self.close()

    def go_home(self):
        self.selected_files.clear()
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

class AnalyzingWindow(BaseWindow):
    def __init__(self, selected_files):
        super().__init__()
        self.selected_files = selected_files
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: #dcdcdc;")

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)

        self.label = QLabel("Analyzing...")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.layout.addWidget(self.label)

        self.progress = QProgressBar()
        self.progress.setValue(0)
        self.progress.setFixedWidth(400)
        self.layout.addWidget(self.progress)

        # Кнопка Cancel — видна сразу
        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.setFixedHeight(35)
        self.cancel_btn.setStyleSheet("background-color: white; border: 1px solid black; font-size: 14px;")
        self.cancel_btn.clicked.connect(self.cancel_analysis)
        self.layout.addWidget(self.cancel_btn)


        # Кнопки скрытые по умолчанию
        self.btn_nothing = QPushButton("Nothing Found")
        self.btn_found = QPushButton("Found Result")
        for btn in (self.btn_nothing, self.btn_found):
            btn.setFixedHeight(35)
            btn.setStyleSheet("background-color: white; border: 1px solid black; font-size: 14px;")
            btn.setVisible(False)
            self.layout.addWidget(btn)

        self.btn_nothing.clicked.connect(self.open_nothing)
        self.btn_found.clicked.connect(self.open_result)

        self.setLayout(self.layout)

        # Таймер на 5 сек
        self.progress_value = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(100)  # 100мс → 50 шагов = 5 сек

    def update_progress(self):
        if self.progress_value < 100:
            self.progress_value += 2
            self.progress.setValue(self.progress_value)
        else:
            self.timer.stop()
            self.btn_nothing.setVisible(True)
            self.btn_found.setVisible(True)


    def open_nothing(self):
        self.nothing_window = NothingFoundWindow()
        self.nothing_window.show()
        self.close()

    def open_result(self):
        self.result_window = FoundResultWindow()
        self.result_window.show()
        self.close()

    def cancel_analysis(self):
        self.timer.stop()
        self.user_choice_window = UserChoiceWindow(self.selected_files)
        self.user_choice_window.show()
        self.close()


class NothingFoundWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nothing Found")
        self.resize(800, 600)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("No results found."))
        self.setLayout(layout)

class FoundResultWindow(BaseWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Found Results")
        self.resize(800, 600)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Results found and displayed here."))
        self.setLayout(layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
