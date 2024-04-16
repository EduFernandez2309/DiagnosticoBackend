class Proyecto():
    def __init__(self, id, nombre, fecha_registro, costo, tipo_proyecto_id, integrantes_minimo) -> None:
        self.id=id
        self.nombre=nombre
        self.fecha_registro=fecha_registro
        self.costo=costo
        self.tipo_proyecto_id=tipo_proyecto_id
        self.integrantes_minimo=integrantes_minimo


    def to_JSON(self, tipo_proyecto):
        return {
            'id':self.id,
            'nombre':self.nombre,
            'fecha_registro':self.fecha_registro,
            'costo':self.costo,
            'integrantes_minimo':self.integrantes_minimo,
            'tipo_proyecto':{
                'id':self.tipo_proyecto_id,
                'nombre':tipo_proyecto
            }
        }