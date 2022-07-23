import sys

from PyQt5 import QtWidgets, QtGui, QtCore

from ribbon import RibbonBar
from ribbon.utils import data_file_path

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setFont(QtGui.QFont("Times New Roman", 8))
    
    # Central widget
    window = QtWidgets.QMainWindow()
    window.setWindowIcon(QtGui.QIcon(data_file_path("icons/python.png")))
    centralWidget = QtWidgets.QWidget()
    window.setCentralWidget(centralWidget)
    layout = QtWidgets.QVBoxLayout(centralWidget)
    
    # Ribbon bar
    ribbonbar = RibbonBar()
    category = ribbonbar.addCategory("Category 1")
    panel = category.addPanel("Panel 1")
    panel.addLargeButton("A Large Button", QtGui.QIcon(data_file_path("icons/python.png")))
    panel.addMediumButton("A Medium Button", QtGui.QIcon(data_file_path("icons/python.png")))
    panel.addMediumButton("A Medium Button", QtGui.QIcon(data_file_path("icons/python.png")))
    panel.addSmallButton("A Medium Button", QtGui.QIcon(data_file_path("icons/python.png")))
    panel.addSmallButton("A Small Button", QtGui.QIcon(data_file_path("icons/python.png")))
    panel.addSmallButton("A Small Button", QtGui.QIcon(data_file_path("icons/python.png")))
    
    # Display a label in the main window
    label = QtWidgets.QLabel("Ribbon Test Window")
    label = QtWidgets.QLabel("Ribbon Test Window")
    label.setFont(QtGui.QFont("Arial", 20))
    label.setAlignment(QtCore.Qt.AlignCenter)
    
    # Add the ribbon bar and label to the layout
    layout.addWidget(ribbonbar, 0)
    layout.addWidget(label, 1)
    
    # Show the window
    window.resize(1800, 350)
    window.show()
    sys.exit(app.exec_())
    