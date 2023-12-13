from flask import Flask,render_template,request,jsonify # importamos microframework de flask
from flask_cors import CORS
#import urllib.request


import io
import PIL.Image as Image

""" 
import numpy
import os
from werkzeug.utils import secure_filename
import json
import cv2 
"""

#import psycopg2
#import psycopg2.extras


import mysql.connector

#from flaskext.mysql import MySQL

app=Flask(__name__) # Creamos la instaclearncia de la clase flask (nombre del archivo)
#CORS(app)

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


class Persona:
    def __init__(self,host,user,password,database):
        self.conexion = mysql.connector.connect(
            database = database,
            host= host,
            user=user,
            password = password
        )
        
        self.cursor = self.conexion.cursor()
        self.cursor.execute(f"USE `{database}`")

    def traerpersonas(self):
        sql="select * from tabla_persona"
        self.cursor.execute(sql) 
        datos=self.cursor.fetchall()
        return datos

    def traer_cliente_por_id(self,idcliente):
        sql = f"SELECT * FROM tabla_persona WHERE id={idcliente};"
        self.cursor.execute(sql)
        cli = self.cursor.fetchone()
        return cli

    def agregar_cliente(self,dni,nombre,direccion,telefono):
            #,imagen):

            #img=conversion(imagen)
            
            #empPicture = imagen.read()

            #filename=convertToBinaryData(imagen)

            #sql="INSERT INTO `persona`.`tabla_persona` (`dni`,`nombre`,`direccion`,`telefono`,`foto`) VALUES (%s,%s,%s,%s,%s);"#.format(ddni=dni,dnombre=nombre,ddireccion=direccion,dtelefono=telefono,dimagen=imagen)
            sql="INSERT INTO `persona`.`tabla_persona` (`dni`,`nombre`,`direccion`,`telefono`) VALUES (%s,%s,%s,%s);"#.format(ddni=dni,dnombre=nombre,ddireccion=direccion,dtelefono=telefono,dimagen=imagen)
            valores = (dni,nombre,direccion,telefono)
            self.cursor.execute(sql,valores)

            self.conexion.commit()
            return True

    def modificar_cliente(self,codigo,dni,nombre,direccion,telefono):#,imagen):

        #img=conversion(imagen)
        
        #empPicture = imagen.read()

        #filename=convertToBinaryData(imagen)

        sql="UPDATE `persona`.`tabla_persona` SET `dni` = %s,`nombre` = %s, `direccion`=%s,`telefono`=%s WHERE `id`=%s;"

        valores = (dni,nombre,direccion,telefono,codigo)
        self.cursor.execute(sql,valores)

        self.conexion.commit()

        return True
    def eliminar_cliente(self,codigo):

        #img=conversion(imagen)
        
        #empPicture = imagen.read()

        #filename=convertToBinaryData(imagen)

        sql=f"DELETE FROM `persona`.`tabla_persona` WHERE `id`={codigo};"

        #valores = (codigo)

        self.cursor.execute(sql)

        self.conexion.commit()

        return True
    

conexion_persona=Persona(host="localhost",user="root",password="root",database="persona")
#mysql = MySQL()

# CONFIGURACIONES DE MI BASE DE DATOS

""" 
app.config.setdefault('MYSQL_DATABASE_HOST', 'localhost')
app.config.setdefault('MYSQL_DATABASE_PORT', 3306)
app.config.setdefault('MYSQL_DATABASE_USER', 'root')
app.config.setdefault('MYSQL_DATABASE_PASSWORD', 'root')
app.config.setdefault('MYSQL_DATABASE_DB', 'persona')
mysql.init_app(app)


mysql = MySQL()
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='movies_db'
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_PORT']=3306

mysql.init_app(app) # INICIALIZO LA CONEXION A LA BASE DE DATOS """

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alquilar')
def alquilar():
    return render_template("alquilar.html")

@app.route('/comprar')
def comprar():
    return render_template("comprar.html")

@app.route('/contacto')
def contact():
    return render_template("contacto.html")

@app.route('/servicios')
def services():
    return render_template("servicios.html")

@app.route('/clientes')
def clientes():
    return render_template("clientes.html")

@app.route('/modificar')
def modificar():
    return render_template("modificar.html")

@app.route('/listado')
def listado():
    return render_template("listado.html")#jsonify(personas_json),200

@app.route('/metodos',methods=["GET"])
def lista():
    personas = conexion_persona.traerpersonas()
    personas_json = []
    for persona in personas:
        # if (persona[5] != None):
        #     #json_str = json.dumps({persona[5].decode('ISO-8859-1')})
        #     #json_str = persona[5]#
        #     json_str = persona[5].decode('ISO-8859-1')
        #     #Image.open(io.BytesIO(persona[5]))

        #     #imgen.show()

        #     #flatNumpyArray = numpy.array(persona[5])
        #     #grayImage = flatNumpyArray.reshape(300, 400,3)
        #     #cv2.imwrite('RandomGray.png', grayImage)

        # else:
        #     json_str = ''

        personas_json.append({
            "id" : persona[0],
            "dni" : persona[1],
            "nombre" : persona[2],
            "direccion" : persona[3],
            "telefono" : persona[4]
            #"foto" : json_str#persona[5].decode('utf-8')
        }) 
    
    #print(type(personas_json))
    return jsonify(personas_json),200

@app.route('/metodos',methods=["POST"])
def agregar_cliente():
    dni=request.form['dni']
    nombre=request.form['nombre']
    direccion=request.form['direccion']
    telefono=request.form['telefono']
    #imagen=request.files['imagen']
    #imagen.save(imagen.filename)
    #file_content = imagen.read() 
    #imagen.save(os.path.join('static/uploads', secure_filename(imagen.filename)))
    #photo_n = file_content.filename

    si_se_agrego = conexion_persona.agregar_cliente(dni,nombre,direccion,telefono)
    #,file_content)

    if si_se_agrego:
        return jsonify({"mensaje":"Cliente Agregado"}), 200
    else:
        return jsonify({"mensaje":"Error"}), 400
    #return jsonify(personas_json),200

@app.route("/clientes/<int:codigo>", methods=["GET"])
def traer_producto_por_id(codigo):
    personas = conexion_persona.traer_cliente_por_id(codigo)
    #epersonas_json = []
    if personas:
        """ if (persona[5] != None):
            #json_str = json.dumps({persona[5].decode('ISO-8859-1')})
            #json_str = persona[5]#
            json_str = persona[5].decode('ISO-8859-1')
            #Image.open(io.BytesIO(persona[5]))

            #imgen.show()

            #flatNumpyArray = numpy.array(persona[5])
            #grayImage = flatNumpyArray.reshape(300, 400,3)
            #cv2.imwrite('RandomGray.png', grayImage)

        else:
            json_str = '' """

        personas_json = {
            "id" : personas[0],
            "dni" : personas[1],
            "nombre" : personas[2],
            "direccion" : personas[3],
            "telefono" : personas[4]
            #"foto" : json_str#persona[5].decode('utf-8')
        }
        return render_template("modificar.html",datospersona=personas_json)#jsonify(personas_json), 200 #, 
        
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 400

@app.route("/modificar/<int:codigo>", methods=["PUT"])
def modificar_producto(codigo):    
    
    nombre = request.form['nombre']
    dni = request.form['dni']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    #imagen=request.files['imagen']
    #imagen.save(imagen.filename)
    #file_content = imagen.read() 

    si_se_modifico = conexion_persona.modificar_cliente(codigo, dni, nombre, direccion, telefono)#, file_content)
    if si_se_modifico:
        return jsonify({"mensaje": "Cliente modificado"}), 200
    else:
        return jsonify({"mensaje": "Error"}), 400

@app.route("/metodos/<int:codigo>", methods=["DELETE"])
def eliminar_cliente(codigo):    
    print(type(codigo))
    si_se_elimino = conexion_persona.eliminar_cliente(codigo)

    if si_se_elimino:
        return jsonify({"mensaje": "Cliente eliminado"}), 200
    else:
        return jsonify({"mensaje": "Error"}), 400

@app.route('/altas')
def altas():
    return render_template("altas.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000, debug=True)