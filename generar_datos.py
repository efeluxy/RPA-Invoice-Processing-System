import os
import random
from fpdf import FPDF
from email.message import EmailMessage

# Configuración de carpetas (según tu estructura)
base_dir = os.getcwd()
pdf_dir = os.path.join(base_dir, "Alta_Clientes_Bot", "Data", "PDFs")
email_dir = os.path.join(base_dir, "Alta_Clientes_Bot", "Data", "Emails")

os.makedirs(pdf_dir, exist_ok=True)
os.makedirs(email_dir, exist_ok=True)

# Datos de prueba (Lista simplificada de los 30 registros)
clientes = [
    ("Tech Solutions SL", "B12345678", 1200.50), ("Juan Pérez García", "12345678Z", 350.00),
    ("Muebles Modernos SA", "A87654321", 4500.00), ("Ana López", "87654321X", 800.00),
    ("Innovación Digital", "B11223344", 1500.00), ("Tech Solutions SL", "B12345678", 200.00), # Duplicado
    ("Construcciones Norte", "A99887766", 12000.00), ("Laura Martín", "11223344V", 150.00),
    ("Logística Rápida", "B55667788", 600.00), ("Pedro Ruiz", "99887766H", 300.00),
    ("Sistemas Globales", "A44332211", 2500.00), ("Marketing 360", "B66778899", 900.00),
    ("Elena Gómez", "22334455J", 120.00), ("Juan Pérez García", "12345678Z", 100.00), # Duplicado
    ("Serviclim SA", "A12121212", 550.00), ("Beta Startups", "B98989898", 3000.00),
    ("Carlos Soria", "55443322Q", 400.00), ("Limpiezas Brillantes", "B33445566", 200.00),
    ("Alpha Code", "B77788899", 5000.00), ("María Sánchez", "66554433K", 150.00),
    ("Hostelería El Paso", "A22233344", 1200.00), ("Auto Repuestos", "B44455566", 75.50),
    ("Innovación Digital", "B11223344", 450.00), # Duplicado
    ("Luis Torres", "99988877L", 600.00), ("Green Energy", "A55566677", 8500.00),
    ("Sara Mola", "33322211P", 250.00), ("Ferretería Central", "B10101010", 45.90),
    ("Consultores Asociados", "A20202020", 1800.00), ("David Villa", "77766655R", 3000.00),
    ("Print Fast", "B30303030", 80.00), ("Andrea Jimenez", "18223344S", 1500.00)
]

print("Generando 30 facturas y correos...")

for i, (nombre, nif, importe) in enumerate(clientes, start=1):
    # 1. Crear el PDF Estructurado
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Encabezado (siempre igual posición = Estructurado)
    pdf.cell(200, 10, txt="FACTURA SIMPLIFICADA", ln=1, align='C')
    pdf.ln(10)
    
    # Campos Clave (Labels fijos para que UiPath los encuentre)
    pdf.cell(200, 10, txt=f"Numero de Factura: FAC-{2024000+i}", ln=1)
    pdf.cell(200, 10, txt=f"Fecha: 24/01/2026", ln=1)
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Cliente: {nombre}", ln=1)
    pdf.cell(200, 10, txt=f"NIF: {nif}", ln=1) # El robot buscará la etiqueta "NIF:"
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Total a Pagar: {importe:.2f} EUR", ln=1)
    
    filename_pdf = f"Factura_{i}_{nif}.pdf"
    path_pdf = os.path.join(pdf_dir, filename_pdf)
    pdf.output(path_pdf)

    # 2. Crear el Email (.eml) y adjuntar el PDF
    msg = EmailMessage()
    msg['Subject'] = f"Factura pendiente - {nombre} - Ref: FAC-{2024000+i}"
    msg['From'] = "robot@uipath-test.com"
    msg['To'] = "admin@empresa.com"
    msg.set_content(f"Hola,\n\nAdjunto encontrarás la factura FAC-{2024000+i} correspondiente al cliente {nombre}.\n\nSaludos.")

    # Adjuntar PDF
    with open(path_pdf, 'rb') as f:
        file_data = f.read()
        file_name = filename_pdf
    msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

    # Guardar email
    path_email = os.path.join(email_dir, f"Email_{i}.eml")
    with open(path_email, 'wb') as f:
        f.write(msg.as_bytes())

print("¡Listo! Archivos generados en Data/PDFs y Data/Emails.")