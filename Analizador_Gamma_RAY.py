import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QHBoxLayout, QWidget, QSpinBox, QScrollArea
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

### Función para preprocesar la imagen
def preprocess_image(image_path, target_size=(128, 128)):
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_bound = np.array([30, 50, 50])
    upper_bound = np.array([80, 255, 255])
    mask = cv2.inRange(hsv_img, lower_bound, upper_bound)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=2)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.medianBlur(mask, 5)
    gray_img = cv2.resize(gray_img, target_size) / 255.0
    mask = cv2.resize(mask, target_size) / 255.0
    return img, gray_img, mask

#### Función para analizar la línea verde y extraer el centro
def analyze_green_line(img, mask):
    contours, _ = cv2.findContours((mask * 255).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        for contour in contours:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                return cX
    return None

###### Función para clasificar la gráfica con rangos personalizados Aqui es posible cambiar la tendecia a detectar
def classify_graph(cX, image_width, user_range):
    adjusted_range = (user_range / 140) * image_width
    if cX < adjusted_range:
        return 'Productiva'
    elif cX > image_width - adjusted_range:
        return 'Productiva'
    else:
        return 'No Productiva'

# Funciones de IU donde se 
class ImageAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Análisis de GR en R.E")
        self.setGeometry(100, 100, 600, 700)  #ancho por largo 600x700
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QHBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        
        # Área de visualización de imagen
        self.image_display = QLabel()
        self.image_display.setFixedWidth(600)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.image_display)
        
        self.main_layout.addWidget(self.scroll_area)
        
        ###### Controles de análisis
        self.control_widget = QWidget()
        self.control_layout = QVBoxLayout()
        self.control_widget.setLayout(self.control_layout)
        self.main_layout.addWidget(self.control_widget)
        
        self.label = QLabel("Cargue un registro para analizar")
        self.control_layout.addWidget(self.label)
        
        self.upload_button = QPushButton("Cargar Imagen")
        self.upload_button.clicked.connect(self.upload_image)
        self.control_layout.addWidget(self.upload_button)
        
        self.analyze_button = QPushButton("Analizar")
        self.analyze_button.clicked.connect(self.analyze_image)
        self.control_layout.addWidget(self.analyze_button)
        
        self.result_label = QLabel("")
        self.control_layout.addWidget(self.result_label)
        
        ###### Añadido del QSpinBox para ajustar los rangos
        self.range_label = QLabel("Rango (0-140):")
        self.control_layout.addWidget(self.range_label)
        
        self.range_spinbox = QSpinBox()
        self.range_spinbox.setRange(0, 140)  
        self.range_spinbox.setValue(80)  ##### Valor por defecto cambiado a 80
        self.range_spinbox.valueChanged.connect(self.update_line_position)
        self.control_layout.addWidget(self.range_spinbox)
        
        self.image_path = None
        self.original_img = None

  ################ carga de imagen
    def upload_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Abrir Imagen", "", "Imagen (*.png *.jpg *.bmp)")
        if file_path:
            self.image_path = file_path
            img, _, _ = preprocess_image(file_path)
            self.original_img = img
            self.display_image(img)

    def display_image(self, img):
        q_img = QImage(img.data, img.shape[1], img.shape[0], img.strides[0], QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(q_img)
        self.image_display.setPixmap(pixmap.scaled(self.scroll_area.width(), self.scroll_area.height(), Qt.KeepAspectRatio))

    def update_line_position(self):
        if self.original_img is not None:
            user_range = self.range_spinbox.value()
            adjusted_x = int((user_range / 140) * self.original_img.shape[1])
            img_with_line = self.original_img.copy()
            
            # Dibujar la línea
            cv2.line(img_with_line, (adjusted_x, 0), (adjusted_x, img_with_line.shape[0]), (0, 0, 255), 2)
            
            # Mostrar la imagen actualizada
            self.display_image(img_with_line)

    def analyze_image(self):
        if self.image_path:
            img, gray_img, mask = preprocess_image(self.image_path)
            cX = analyze_green_line(img, mask)
            if cX is not None:
                image_width = 128
                user_range = self.range_spinbox.value()  # Obtener el rango desde el QSpinBox
                classification = classify_graph(cX, image_width, user_range)
                self.result_label.setText(f'Centro de la Línea Verde: ({cX})\nClasificación de la Gráfica: {classification}')
            else:
                self.result_label.setText("No se detectó la línea verde.")
        else:
            self.result_label.setText("No se seleccionó ninguna imagen.")

########## Ejecucion la aplicación ############
app = QApplication(sys.argv)
window = ImageAnalyzer()
window.show()
sys.exit(app.exec_())
