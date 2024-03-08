import pymysql.cursors
from flask import Flask, jsonify, request   #Importando librerias

def connection_mysql():                            #Funcion declarando la conexion a la base de datos
    connection = pymysql.connect(host='localhost',
                                 user ='root',
                                 password='',
                                 database='bs_usuario',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


app = Flask(__name__)

@app.route('/usuarios/crear', methods=["POST"])     #Recurso para crear usuario en la base de datos
def create():             
    data = request.get_json()
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
            cursor.execute(sql, (data['email'], data['password']))

        connection.commit()

        return jsonify({
            'message': 'CREACIÓN EXITOSA'

        }), 201
    
@app.route('/usuarios/consultar', methods=["GET"])     #Recurso para visualizar los usuarios registrados en la base de datos
def READ():             
    connection = connection_mysql()

 
    with connection.cursor() as cursor:

        sql = "SELECT id, email, password from users"
        cursor.execute(sql)

    result = cursor.fetchall()

    return jsonify({
        'data': result

    }), 200
    

@app.route('/usuarios/eliminar', methods=["DELETE"]) #Eliminar por ID el usuario
def delete():             
    data = request.get_json()
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            sql = "DELETE FROM users WHERE ID = %s"
            cursor.execute(sql, (data['ID'],))

        connection.commit()

        return jsonify({
            'message': 'ELIMINACION EXITOSA'

        }), 200
    

@app.route('/usuarios/actualizar', methods=["PUT"])    #Actualizar por el ID el correo
def Update():             
    data = request.get_json()
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:

            sql = "UPDATE users SET email = %s WHERE ID = %s"
            cursor.execute(sql, (data['email'], data['ID']))

        connection.commit()

        return jsonify({
            'message': 'ACTUALIZACIÓN EXITOSA'

        }), 200
   

   

if __name__ == '__main__':
    app.run(debug=True)




