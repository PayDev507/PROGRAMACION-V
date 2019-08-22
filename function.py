import json
import datetime
import sys
import pymysql

serv = "XXXXX.XXXXX.us-east-1.rds.amazonaws.com"
name = "admin"
passw = "XXXXX"
dbnm = "XXXXX"

try:
    conn = pymysql.connect(serv, name, passwd=passw, db=dbnm)
except:
    sys.exit()

def lambda_handler(event, context):
 # OJO Un tipo de slot es una lista de valores que Amazon Lex utiliza para enseñar al modelo de 
 aprendizaje automático a reconocer los valores de un slot. Por ejemplo, 
 puede definir un tipo de slot llamado "Genres." Cada valor del tipo de 
 slot es el nombre de un género, "comedia", "aventura", "documentales", etc  
    cedula = event['currentIntent']['slots']['cedula']
    nombre = event['currentIntent']['slots']['nombre']
    apellido = event['currentIntent']['slots']['apellido']
    fecha_nacimiento = event['currentIntent']['slots']['fecha_nacimiento']
    departamento = event['currentIntent']['slots']['departamento']
    puesto = event['currentIntent']['slots']['puesto']
    salario = float(event['currentIntent']['slots']['salario'])
    
    with conn.cursor() as cur:
        cur.execute('INSERT INTO empleado VALUES("%s", "%s", "%s", "%s", "%s", "%s", %f)' % (cedula, nombre, apellido, fecha_nacimiento, departamento, puesto, salario))
        conn.commit()
    
    return {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": "Se ha creado el colaborador %s %s con exito" % (nombre, apellido)
            }
         }
    }

