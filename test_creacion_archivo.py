from transaccion import Transaccion
import json

def test_creacion_archivo():
        tsc_a = Transaccion(dni_cliente=45990339, tipo_movimiento="CONSUMO", monto_movimiento=2000, estado="RECHAZADO"
                                              , nombre_comercio="MUSIMUNDO")
        tsc_a.crear_archivo(tsc_a)
        tsc_b = Transaccion(45990339, "CONSUMO", 2000, "APROBADO", "MUSIMUNDO")
        tsc_b.crear_archivo(tsc_b)
        tsc_c = Transaccion(30949303, "CASH_IN", 50000, "APROBADO", "PAGOFACIL")
        tsc_c.crear_archivo(tsc_c)

def test_monto_movimiento():
        transaccion_a = Transaccion(dni_cliente=45990339, tipo_movimiento="CONSUMO", monto_movimiento=200000, estado="APROBADO", nombre_comercio="DISCO")
        print(transaccion_a.comprobacion())

def test_json_movimiento():
        transaccion_a = Transaccion(30949303, 'CASH_IN', 500, 'APROBADO', 'PAGOFACIL')
        movimiento_to_dict = json.loads(transaccion_a.toJSON())
        print(movimiento_to_dict.keys())
        print(movimiento_to_dict.items())
        tipomovimiento = movimiento_to_dict.get('tipo_movimiento')
        print(tipomovimiento)



test_monto_movimiento()
test_json_movimiento()
test_creacion_archivo()
