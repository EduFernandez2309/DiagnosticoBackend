from src.database.db import get_connection
from .entities.Proyecto import Proyecto

class ProyectoModel():

    @classmethod
    def get_proyectos(cls):
        try:
            connection = get_connection()

            proyectos = []

            with connection.cursor() as cursor:
                cursor.execute('select pr.*, tp.nombre as tipo_proyecto from proyecto pr inner join tipo_proyecto tp on pr.tipo_proyecto_id=tp.id')
                resultset=cursor.fetchall()

                for row in resultset:
                    proyecto = Proyecto(row[0], row[1], row[2].strftime("%Y-%m-%d"), row[3], row[4], row[5])
                    proyectos.append(proyecto.get_to_JSON(row[6]))

            return proyectos
        except Exception as ex:
            raise Exception(ex) 
        finally:
            connection.close()

    @classmethod
    def insert_proyecto(cls, data):
        connection = None
        try:
            connection = get_connection()

            proyecto = Proyecto(id = None, nombre=data['nombre'], fecha_registro = data['fecha_registro'], costo =data['costo'], tipo_proyecto_id=data['tipo_proyecto_id'], integrantes_minimo=data['integrantes_minimo'])

            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO proyecto (nombre, fecha_registro, costo, tipo_proyecto_id, integrantes_minimo) VALUES (%s, %s, %s, %s, %s)',
                               (proyecto.nombre, proyecto.fecha_registro, proyecto.costo, proyecto.tipo_proyecto_id, proyecto.integrantes_minimo))
                connection.commit()
                return proyecto.to_JSON()
        except Exception as ex:
            raise Exception(ex) 
        finally:
            if connection:
                connection.close()

    @classmethod
    def update_proyecto(cls, proyecto_id, data):
        connection = None
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('UPDATE proyecto SET nombre = %s, costo = %s, tipo_proyecto_id = %s, integrantes_minimo = %s WHERE id = %s',
                               (data['nombre'], data['costo'], data['tipo_proyecto_id'], data['integrantes_minimo'], proyecto_id))
                connection.commit()
        except Exception as ex:
            raise Exception(ex) 
        finally:
            if connection:
                connection.close()

    @classmethod
    def delete_proyecto(cls, proyecto_id):
        connection = None
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM proyecto WHERE id = %s', (proyecto_id,))
                connection.commit()
        except Exception as ex:
            raise Exception(ex) 
        finally:
            if connection:
                connection.close()