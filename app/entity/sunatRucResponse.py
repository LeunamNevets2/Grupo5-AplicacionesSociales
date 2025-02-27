class EmpresaDTO:
    def __init__(self,resultado, ruc, nombre, estado, condicion, direccion, distrito, provincia, departamento):
        self.resultado = resultado
        self.ruc = ruc
        self.nombre = nombre
        self.estado = estado
        self.condicion = condicion
        self.direccion = direccion
        self.distrito = distrito
        self.provincia = provincia
        self.departamento = departamento

    def to_dict(self):
        return {
            "resultado": self.resultado,
            "ruc": self.ruc,
            "nombre": self.nombre,
            "estado": self.estado,
            "condicion": self.condicion,
            "direccion": self.direccion,
            "distrito": self.distrito,
            "provincia": self.provincia,
            "departamento": self.departamento
        }