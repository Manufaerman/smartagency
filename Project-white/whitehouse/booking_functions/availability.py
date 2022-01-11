import datetime
from django.utils.timezone import get_current_timezone
from datetime import datetime


def check_availability(vivienda, fecha_entrada, fecha_salida ):
        
        dt = datetime.strptime(fecha_entrada, '%d-%m-%y')
        dt1 = datetime.strptime(fecha_salida, '%d-%m-%y')
        field_value = vivienda._meta.get_field("fecha_entrada")
        field_value = datetime.strptime(str(field_value), '%d-%m-%y')
        field_value1 = vivienda._meta.get_field("fecha_salida")
        field_value = datetime.strptime(str(field_value1), '%d-%m-%y')
        if dt and dt1 and vivienda:
                if field_value > dt1 or field_value1 < dt:
                        return True
                else:
                        return False
        else:
                return True
        




