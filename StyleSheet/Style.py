from PyQt5 import QtCore
class Style():
    def Style_Btn_On(self):
        # return """
        #             border-width: 2px;
        #             border-radius: 10px;
        #             border-color: beige;
        #             border: 2px solid black;
        #             background-color: green"""
        return """QPushButton {
                    background-color: rgb(100, 192, 86);
                    border: 2px solid grey;
					   border-left: 2px solid rgb(110, 144, 76);
                    border-right: 3px solid rgb(110, 144, 76);
					   border-bottom: 3px solid rgb(110, 144, 76);
                    border-radius: 10px;
                    padding-top: 5px;
                    color: rgb(226, 234, 216);
                    }

                QPushButton:hover{
                    background-color: rgb(46, 156, 49);
                    }

                QPushButton:pressed{
                    background-color: rgb(100, 192, 86);
                    border-top: 3px solid rgb(110, 144, 76);
                    padding-top: -5px;
                    border-bottom: none;
                    }"""
    
    def Style_Btn_Off(self):
        return """QPushButton {
                    background-color: rgb(154, 153, 150);
                    border: 2px solid grey;
						border-left: 2px solid rgb(119, 118, 123);
					   border-right: 3px solid rgb(94, 92, 100);
                    border-bottom: 3px solid rgb(94, 92, 100);
                    border-radius: 10px;
                    padding-top: 5px;
                    color: rgb(255, 255, 255);
                    }

                QPushButton:hover{
                    background-color: rgb(156, 144, 144);
                    }

                QPushButton:pressed{
                    background-color: rgb(154, 153, 150);
                    border-top: 3px solid rgb(94, 92, 100);
                    padding-top: -5px;
                    border-bottom: none;
                    }"""

    def Style_Btn_AM(self):
        return """QPushButton {
                    background-color: rgb(153, 193, 241);
                    border: 2px solid grey;
						border-left: 2px solid rgb(119, 118, 123);
					   border-right: 3px solid rgb(94, 92, 100);
                    border-bottom: 3px solid rgb(94, 92, 100);
                    border-radius: 10px;
                    padding-top: 5px;
                    color: rgb(0, 0, 0);
                    }

                QPushButton:hover{
                    background-color: rgb(98, 160, 234);
                    }

                QPushButton:pressed{
                    background-color: rgb(153, 193, 241);
                    border-top: 3px solid rgb(94, 92, 100);
                    padding-top: -5px;
                    border-bottom: none;
                    }"""

    def Style_Btn_PM(self):
        return """QPushButton {
                    background-color: orange;
                    border: 2px solid grey;
						border-left: 2px solid rgb(119, 118, 123);
					   border-right: 3px solid rgb(94, 92, 100);
                    border-bottom: 3px solid rgb(94, 92, 100);
                    border-radius: 10px;
                    padding-top: 5px;
                    color: rgb(0, 0, 0);
                    }

QPushButton:hover{
                    background-color: rgb(255, 163, 72);
                    }

                QPushButton:pressed{
                    background-color: orange;
                    border-top: 3px solid rgb(94, 92, 100);
                    padding-top: -5px;
                    border-bottom: none;
                    }"""

    def Style_SHOW(self):
        _translate = QtCore.QCoreApplication.translate
        return _translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#1c71d8;\">SHOW DIALOG</span></p></body></html>")

    def Style_notSHOW(self):
        _translate = QtCore.QCoreApplication.translate
        return _translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#ed333b;\">not SHOW DIALOG</span></p></body></html>")