class SunatRepresentanteLegal:
    def __init__(self, documento, dni, nombre, cargo, fecha, ruc):
        self.documento = documento
        self.dni = dni
        self.nombre = nombre
        self.cargo = cargo
        self.fecha = fecha
        self.ruc = ruc
            
    def to_dict(self):
        return {
            "documento": self.documento,
            "dni": self.dni,
            "nombre": self.nombre,
            "cargo": self.cargo,
            "fecha": self.fecha,
            "ruc": self.ruc
        }

class SunatRepresentanteLegalResponse:
    def __init__(self, success, data):
        self.success = success
        self.data = [SunatRepresentanteLegal(**rep) for rep in data] 
            
    def to_dict(self):
        return {
            "success": self.success,
            "data": [rep.to_dict() for rep in self.data]  # Convertir cada objeto en un diccionario
        }