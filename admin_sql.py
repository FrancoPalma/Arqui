import sqlite3

conn = sqlite3.connect('tables1.sqlite')
cur = conn.cursor()
cur.execute(
    'CREATE TABLE Routine (id INTEGER PRIMARY KEY, active_time INTEGER, rest_time INTEGER, total_time INTEGER, type int)')
cur.execute(
    'CREATE TABLE Routine_exercise (id INTEGER PRIMARY KEY, id_routine INTEGER, id_ex int, minute int)')
cur.execute(
    'CREATE TABLE Exercise (id INTEGER PRIMARY KEY, name VARCHAR , detail VARCHAR, type INTEGER, ex_zone VARCHAR, level int)')

#MUSCULATURA - Piernas
# nivel 1
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Puente","Recuéstate boca arriba con tus rodillas flexionadas. Contrae tus músculos abdominales. Eleva la cadera del suelo hasta que la cadera esté en línea con las rodillas y los hombros", 1, "Piernas", 1)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Sentadilla","Flexiona las rodillas y baja el cuerpo manteniendo la verticalidad, luego regresa a la posición erguida", 1, "Piernas", 1)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Peso muerto libre","Colócate de pie con las piernas separadas a la anchura de los hombros, flexiona las rodillas manteniendo la espalda totalmente recta. Empieza a descender utilizando las caderas", 1, "Piernas", 1)')

# nivel 2
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Lunge","Esté de pie con las manos en puño apoyadas en la cintura y las piernas ligeramente separadas. Luego de un paso hacia delante", 1, "Piernas", 2)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Sentadilla sumo","Separa las piernas para que los talones estén con una distancia amplia. Baja hasta que las caderas estén en la misma línea, a la misma altura que las rodillas", 1, "Piernas", 2)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Puente con una pierna","Acuéstese boca arriba con los brazos a los lados, las rodillas dobladas y los pies apoyados en el suelo. Levante una pierna y levante las caderas tan alto como pueda. Baja las caderas, repite y luego cambia de pierna", 1, "Piernas", 2)')

# nivel 3
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Sentadilla con salto","Esté de pie con los pies juntos, y coloca las manos sobre los muslos. Flexiona las rodillas, salta y separa los pies en pleno salto. Déjate caer con los pies separados a una distancia mayor que los hombros, bajando hasta quedar en posición de sentadilla", 1, "Piernas", 3)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Peso muerto con una pierna","Ponte de pie apoyado sobre una sola pierna mientras sujetas dos mancuernas. Flexiona un poco una pierna y levántala detrás de ti apoyándote en las caderas. Inclina el torso hacia el suelo a la vez que la pierna trasera queda detrás de ti", 1, "Piernas", 3)')

#MUSCULATURA - Torso
# nivel 1
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Flexión de rodillas","Ponte de rodillas y apoya las manos en el suelo en línea con los hombros. Mantén los codos pegados al tronco y flexiónalos para bajar el cuerpo hasta que el pecho casi toque el suelo, luego sube", 1, "Torso", 1)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Plancha brazos estirados","En posición de plancha, con los brazos estirados, gira el tronco de tal manera que el cuerpo quede alineado en una plancha lateral, con un brazo apoyado en el suelo y el otro estirado hacia el techo. Vuelve a la posición inicial de plancha y gira hacia el otro lado", 1, "Torso", 1)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Superman","Tensa tus músculos abdominales para mantener tu torso estable, luego levanta del suelo unas cuantas pulgadas los brazos, la parte superior del pecho y las piernas simultáneamente. Mantén esta posición un momento antes de volver a bajar suavemente tus brazos y piernas", 1, "Torso", 1)')

# nivel 2
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Flexión normal","Acuestate mirando hacia el suelo, apoyándote únicamente con la punta de los pies y las palmas de las manos. Flexiona los brazos manteniendo en todo momento los codos cerca del cuerpo hasta rozar el suelo con el pecho sin llegar a apoyarse en él. Vuelve a la posición inicial estirando los brazos", 1, "Torso", 2)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Superman nadando","Tumbate boca abajo en una superficie cómoda, extiende pies y brazos y elevalos levemente para que no toquen el suelo, a continuación pasa a elevar pies y brazos simultaneamente (como al nadar)", 1, "Torso", 2)')

# nivel 3
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Plancha lateral","En posición de plancha, con los brazos estirados, gira el tronco de tal manera que el cuerpo quede alineado en una plancha lateral", 1, "Torso", 3)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Plancha invertida","Sientate en el suelo con las piernas juntas. Recuéstate hacia atrás formando un ángulo de 45º entre el suelo y el tronco, apoyando las manos en el suelo con los brazos perpendiculares al suelo. Levanta la pelvis hacia arriba despegando el cuerpo del suelo y contrayendo los glúteos hasta formar una línea recta con el cuerpo. Debes mantener los talones apoyados en el suelo.", 1, "Torso", 3)')

#MUSCULATURA - Abdominales
# nivel 1
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Plancha sobre antebrazos","Colóquese boca abajo. Extienda las piernas detrás de usted. Aguante su peso con los dedos de los pies y los antebrazos. Sus antebrazos deben estar en paralelo entre ellos. Apriete sus musculos abdominales y oblicuos", 1, "Abdominales", 1)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Concava piernas flexionadas","---", 1, "Abdominales", 1)')

# nivel 2
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Mountain climber","Tumbate boca abajo en el suelo apoyando las manos con los dedos dirigidos hacia el frente a la anchura de los hombros. Luego comienza el movimiento consistente en llevar de manera alterna las rodillas hacia el codo opuesto", 1, "Abdominales", 2)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Concava piernas estiradas","---", 1, "Abdominales", 2)')

# nivel 3
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Plancha sobre antebrazos","Colóquese boca abajo. Extienda las piernas detrás de usted. Aguante su peso con los dedos de los pies y los antebrazos. Sus antebrazos deben estar en paralelo entre ellos. Apriete sus musculos abdominales y oblicuos", 1, "Abdominales", 3)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Concava piernas estiradas","---", 1, "Abdominales", 3)')

#CARDIO - Torso
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Burpees","Coloca las manos en el suelo y mantén la cabeza erguida. Desplaza las piernas hacia atrás con los pies juntos y haz una flexión de pecho, para luego volver a la posición inicial y saltar", 0, "Torso", 0)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Mountain climber","Tumbate boca abajo en el suelo apoyando las manos con los dedos dirigidos hacia el frente a la anchura de los hombros. Luego comienza el movimiento consistente en llevar de manera alterna las rodillas hacia el codo opuesto", 0, "Torso", 0)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Caminar hacia pies","---", 0, "Torso", 0)')

#CARDIO - Piernas
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Sentadillas sin salto","Coloca las manos en el suelo y mantén la cabeza erguida. Desplaza las piernas hacia atrás con los pies juntos y haz una flexión de pecho, para luego volver a la posición inicial", 0, "Piernas", 0)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Sentadillas con salto","Coloca las manos en el suelo y mantén la cabeza erguida. Desplaza las piernas hacia atrás con los pies juntos y haz una flexión de pecho, para luego volver a la posición inicial y saltar", 0, "Piernas", 0)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Lunges sin salto","Comienza en posición de zancada, con un pie al frente y el otro atrás, las manos en las caderas, el torso derecho y las rodillas flexionadas formando un ángulo de 90. Sin levantarte, cambia tus piernas de posición", 0, "Piernas", 0)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Lunges con salto","Comienza en posición de zancada, con un pie al frente y el otro atrás, las manos en las caderas, el torso derecho y las rodillas flexionadas formando un ángulo de 90. Abalánzate con fuerza desde el suelo, saltando y cambiando la posición de las piernas a mitad de salto", 0, "Piernas", 0)')


#CARDIO - Abdominales
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Mountain climber","Tumbate boca abajo en el suelo apoyando las manos con los dedos dirigidos hacia el frente a la anchura de los hombros. Luego comienza el movimiento consistente en llevar de manera alterna las rodillas hacia el codo opuesto", 0, "Abdominales", 0)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Caminar hacia pies","---", 0, "Abdominales", 0)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Rodillazo al frente","Colócate de pie con un pie situado ligeramente detrás de ti. Mantén el peso sobre el pie delantero y levanta la rodilla trasera frente a ti mientras llevas el codo contrario hacia esa rodilla. Toca la rodilla con el codo, haz una pausa y repite", 0, "Abdominales", 0)')

#CARDIO - Otros
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Jumping Jacks","De pie con las piernas juntas y los brazos pegados a los muslos, da un salto manteniendo la espalda recta y las piernas separadas a la anchura de los hombros. Al juntar las piernas, tus brazos han de tocar los muslos", 0, "Otros", 0)')
cur.execute('INSERT INTO Exercise (name,detail,type,ex_zone,level) VALUES ("Skipping lateral","Repetidamente eleva las rodillas por encima de la cintura manteniendo la cadera en una posición elevada", 0, "Otros", 0)')

conn.commit()

conn.close()
