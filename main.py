import sys
import conexionDB as DB
from PyQt6.QtWidgets import QApplication, QMainWindow
from mywindow import *

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        
        self.datosDb = DB.Manejo_datos()

        self.ui.pushButtonMostrar.clicked.connect(self.lista_productos)
        self.ui.pushButton_3.clicked.connect(self.busca_producto)
        self.ui.pushButton_4.clicked.connect(self.agrega_producto)
        self.ui.pushButton.clicked.connect(self.actualiza_producto)
        self.ui.pushButton_2.clicked.connect(self.elimina_producto)

        self.ui.tableWidget.setColumnWidth(0,120)
        self.ui.tableWidget.setColumnWidth(1,260)
        self.ui.tableWidget.setColumnWidth(2,160)
        self.ui.tableWidget.setColumnWidth(3,100)

    def lista_productos(self):	
        datos = self.datosDb.listar_productos()
        cant = len(datos)

        self.ui.tableWidget.setRowCount(cant)
        
        for i in range(cant):
            for j in range(4):
                self.ui.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(datos[i][j])))
    
    def agrega_producto(self):
        self.ui.label_9.clear()
        nombre = self.ui.lineEdit_InNP.text() 
        precio = self.ui.lineEdit_InPP.text() 
        cantidad = self.ui.lineEdit_InCP.text()
        const = (nombre and precio and cantidad) != ''
        
        if const:
            self.datosDb.insertar_producto(str(nombre), precio, cantidad) 
            self.ui.label_9.setText('Registro ingresado con éxito!')
            self.ui.lineEdit_InCP.clear()
            self.ui.lineEdit_InNP.clear()
            self.ui.lineEdit_InPP.clear()
        else:
             self.ui.label_9.setText('Datos incompletos!')

    def busca_producto(self):
        id_producto = self.ui.lineEdit.text()
        self.tuple_nombre = self.datosDb.buscar_producto(id_producto)
        print(self.tuple_nombre != None)
        if len(self.tuple_nombre) == 1:
            self.ui.label_5.setText('Registro encontrado. Puede actualizar.')  
        else: 
            self.ui.label_5.setText('Registro no encontrado.') 
        return 
    
    def actualiza_producto(self):
        print(self.tuple_nombre)
        if len(self.tuple_nombre) == 1:
            id_actA = self.tuple_nombre[0][0]
            nombreeditA = self.ui.lineEdit_2.text()
            precioeditA = self.ui.lineEdit_3.text()
            cantidadeditA = self.ui.lineEdit_4.text()
            cont = (nombreeditA and precioeditA and cantidadeditA) != '' 
            if cont:
                pro_actu = self.datosDb.actualizar_producto(nombreeditA,precioeditA,cantidadeditA,id_actA)

                if pro_actu == 1:
                    self.ui.label_5.setText('Registro Actualizado')
                    self.ui.lineEdit.clear()
                    self.ui.lineEdit_2.clear()
                    self.ui.lineEdit_3.clear()
                    self.ui.lineEdit_4.clear()
            else:
                self.ui.label_5.setText('Datos incompletos.')
        else:
            self.ui.label_5.setText('Registro no encontrado')

    def elimina_producto(self):
        id_producto = self.ui.lineEdit_5.text()
        if id_producto != '':
            cont = self.datosDb.eliminar_producto(id_producto)
            
            if cont == 1:
                self.ui.label.setText('Registro eliminado')
            else:
                self.ui.label.setText('Registro no encontrado')
        else:
            self.ui.label.setText('Dato incompleto')


if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = MyApp()
     window.show()
     sys.exit(app.exec())	
