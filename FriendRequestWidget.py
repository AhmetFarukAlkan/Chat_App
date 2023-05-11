from PyQt5.QtWidgets import QWidget
from Ui_FriendRequest import Ui_Form as form
class widget(QWidget, form):
    def __init__(self, parent=None):
        super(widget, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)