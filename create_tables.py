import sqlite3

sql_exercise_table = """CREATE TABLE exercise (id INTEGER, name VARCHAR, detail VARCHAR, type INTEGER, ex_zone VARCHAR, level INTEGER, PRIMARY KEY (id));"""
sql_routine_table = """CREATE TABLE routine (id INTEGER, active_time INTEGER, type INTEGER, PRIMARY KEY (id));"""
sql_routine_exercise_table = """CREATE TABLE exercise (id INTEGER, id_routine INTEGER, id_exercise INTEGER, PRIMARY KEY (id), FOREIGN KEY (id_routine) REFERENCES routine(id), FOREIGN KEY (id_exercise) exercise(id));"""

sql_insert_exercises_muscle = """
INSERT INTO exercise (id, name, type, ex_zone, level) values (1, "Puente de glúteos", "Acostarse en el piso, apoyar pies en el piso con las caderas apoyadas en el suelo, subir cadera apretando los glúteos, repetir", 1, piernas, 1);
INSERT INTO exercise (id, name, type, ex_zone, level) values (2, "Sentadilla", "Pararse con las piernas abiertas a lo ancho de las caderas, apuntar pies hacia afuera y luego intentar sentarse en el piso, repetir", 1, piernas, 1);
INSERT INTO exercise (id, name, type, ex_zone, level) values (3, "Peso muerto libre", "Pararse comodamente para luego agacharse con las espalda recta hasta tocar el piso con las manos, repetir", 1, piernas, 1);
INSERT INTO exercise (id, name, type, ex_zone, level) values (4, "Estocada", "Pararse comodamente para luego llevar una rodilla al piso flexionando y manteniendo el equilibrio en la pierna contraria, repetir", 1, piernas, 2);
INSERT INTO exercise (id, name, type, ex_zone, level) values (5, "Sentadilla sumo", "Pararse con las piernas muy abiertas, como un sumo, apuntar pies hacia afuera y luego intentar sentarse en el piso, repetir", 1, piernas, 2);
INSERT INTO exercise (id, name, type, ex_zone, level) values (6, "Puente de glúteos con una pierna", "Acostarse en el piso, apoyar un pie en el piso con las caderas apoyadas en el suelo, subir cadera apretando los glúteos, repetir", 1, piernas, 2);
INSERT INTO exercise (id, name, type, ex_zone, level) values (7, "Sentadilla con salto", Pararse con las piernas abiertas a lo ancho de las caderas, apuntar pies hacia afuera, intentar sentarse en el piso, subir tan fuerte que se levantan los pies del suelo, repetir", 1, piernas, 3);
INSERT INTO exercise (id, name, type, ex_zone, level) values (8, "Peso muerto con una pierna", "Pararse comodamente en una pierna para luego agacharse con las espalda recta hasta tocar el piso con las manos, repetir", 1, piernas, 3);
"""

conn = sqlite3.connect('AA_db.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE exercise (id INTEGER, name VARCHAR,  INTEGER, ex_zone vARCHAR, level INTEGER, PRIMARY KEY (id))')
conn.commit()

conn.close()
