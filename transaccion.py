import uuid
import json

class Transaccion(json.JSONEncoder):

    def __init__(self, dni_cliente, tipo_movimiento, monto_movimiento, estado, nombre_comercio):
        self.transaccion_id = str(uuid.uuid4())
        self.dni_cliente = dni_cliente
        self.tipo_movimiento = tipo_movimiento
        self.monto_movimiento = int(monto_movimiento)
        self.estado = estado
        self.nombre_comercio = nombre_comercio

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def crear_archivo(self, transaccion):
        archivo = open(f'./data/{self.transaccion_id}.json', "w")
        archivo.write(str(transaccion.toJSON()))
        archivo.close()

    def comprobacion(self):
        if self.monto_movimiento < 100000:
            return ("El movimiento no requiere comprobacion")
        else:
            return ("Se debe solicitar documentación que requiera la justificacion del movimiento")


