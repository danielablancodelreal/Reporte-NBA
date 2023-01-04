import os
from pyhtml2pdf import converter

path = os.path.abspath('pruebas.html')
converter.convert(f'file:///{path}', 'sample.pdf')