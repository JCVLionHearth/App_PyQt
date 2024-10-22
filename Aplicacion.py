import sys #módulo sys
from PyQt5 import uic, QtWidgets # módulo uic y Qtwidgets
from funciones import cifrar, descifrar # importo las funciones creadas en funciones.py
from PyQt5.QtWidgets import QMessageBox # Importo el cuadro de mensaje para las alertas

# Se carga el archivo .ui hecho en Qt Designer
qtCreatorFile = "ventana.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)



class VentanaPrincipal (QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
                # Conección de botones con las funciones
        self.pushButton.clicked.connect(self.cifrar_datos)
        self.pushButton_2.clicked.connect(self.descifrar_datos)

    #funciones para validar que los valores ingresados sean números y que sean de 6 digitos
    def cifrar_datos(self):
        numero = self.lineEdit.text()
        if len(numero) != 6 or not numero.isdigit():
            self.show_error("Debe ingresar un número de 6 dígitos")
            return
        
        cifrado = cifrar(int(numero)) # Aquí se ejecuta la función cifrar y muestra el valor en el objeto:label
        self.label.setText(f"Número cifrado: {cifrado}")
    
    def descifrar_datos(self):
        numero = self.lineEdit_2.text()
        if len(numero) != 6 or not numero.isdigit():
            self.show_error("Debe ingresar un número de 6 dígitos")
            return
        
        descifrado = descifrar(int(numero)) # Aquí se ejecuta la función descifrar y muestra el valor en el objeto:label_2
        self.label_2.setText(f"Número decodificado: {descifrado}")
    
    # función de mensaje de alerta
    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = VentanaPrincipal()
    window.show()
    sys.exit(app.exec_())