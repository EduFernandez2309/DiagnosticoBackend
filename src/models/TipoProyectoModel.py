from src.database.db import get_connection
from .entities.TipoProyecto import TipoProyecto

class TipoProyectoModel():

    @classmethod
    def get_tipos_proyecto(cls):
        try:
            connection = get_connection()

            tipos_proyecto = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT id, nombre FROM tipo_proyecto')
                resultset = cursor.fetchall()

                for row in resultset:
                    tipo_proyecto = TipoProyecto(row[0], row[1])
                    tipos_proyecto.append(tipo_proyecto.to_JSON())

            return tipos_proyecto
        except Exception as ex:
            raise Exception(ex) 
        finally:
            connection.close()

    @classmethod
    def insert_tipo_proyecto(cls, data):
        connection = None
        try:
            connection = get_connection()

            tipo_proyecto = TipoProyecto(id=None, nombre=data['nombre'])

            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO tipo_proyecto (nombre) VALUES (%s)', (tipo_proyecto.nombre,))
                connection.commit()
                return tipo_proyecto.to_JSON()
        except Exception as ex:
            raise Exception(ex) 
        finally:
            if connection:
                connection.close()

    @classmethod
    def update_tipo_proyecto(cls, tipo_proyecto_id, data):
        connection = None
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('UPDATE tipo_proyecto SET nombre = %s WHERE id = %s', (data['nombre'], tipo_proyecto_id))
                connection.commit()
        except Exception as ex:
            raise Exception(ex) 
        finally:
            if connection:
                connection.close()

    @classmethod
    def delete_tipo_proyecto(cls, tipo_proyecto_id):
        connection = None
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM tipo_proyecto WHERE id = %s', (tipo_proyecto_id,))
                connection.commit()
        except Exception as ex:
            raise Exception(ex) 
        finally:
            if connection:
                connection.close()
