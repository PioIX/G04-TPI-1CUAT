from ctypes.wintypes import INT
import sqlite3
conn = sqlite3.connect('bases_de_datos.db')

conn.execute('''CREATE TABLE IF NOT EXISTS Afirmaciones
                (id_afirmacion INT PRIMARY KEY,
                es_correcta BOOLEAN,
                id_respuesta INT,
                contenido_afirmacion TEXT NOT NULL);''')
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (1, True, NULL, "En los últimos años, solo una mujer ganó un premio académico para la mejor directora.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (2, False, 2, "40% de los trabajadores en el sector sanitario y social son mujeres." );""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (3, True, NULL, "Mayormente, las mujeres y/o niñas víctimas de violencia de género tienen entre 15 y 60 años.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (4, False, 4, "53 países han tomado medidas para hacer seguimiento de las asignaciones presupuestarias para la igualdad de género.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (5, True, NULL, "El organismo responsable de las metas priorizadas de la ODS 5 es el Ministerio de las Mujeres, Géneros y Diversidad.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (6, False, 6, "La meta principal del ODS 5 es evitar la violencia y discriminación de género en cualquier ámbito.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (7, True, NULL, "Los efectos de la pandemia de la COVID-19 podrían revertir los logros que se han alcanzado en materia de igualdad de género y derechos de las mujeres.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (8, False, 8, "El Programa igualar propone dar charlas en distintos espacios públicos para dar a entender sobre el propósito de la ODS 5 y concientizar sobre la igualdad de género planteada por este objetivo.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (9, True, NULL,"Uno de los conflictos que enfrentan las mujeres y las niñas diariamente que reconoce y plantea la ODS 5 es la dificultad para acceder a la tierra, la tecnología, los mercados, la infraestructura y los servicios.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (10, False, 10, "La campaña nacional Cuidar en Igualdad reúne a 14 organismos del poder ejecutivo nacional para debatir y planificar políticas que aporten a una redistribución entre géneros y que aporten a reconocer el cuidado como una necesidad, como un trabajo y como un derecho.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (11, True, NULL, "La Meta 5.1 la cual busca darle un fin a todas las formas de discriminación contra todas las mujeres, niñas, niños y niñes LGBTI+ garantizando la igualdad de oportunidades en todo el mundo es una meta adaptada recientemente.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (12, False, 12, "El programa producir fue hecho para la prestación económica, asistencia psicológica y asesoramiento legal a las mujeres.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (13, True, NULL, "La meta 5.4 la cual busca reconocer y valorar los cuidados y el trabajo doméstico no remunerados mediante servicios públicos, infraestructuras y políticas de protección social y promoviendo la responsabilidad compartida en el hogar y la familia, según proceda el país todavía no fue adaptada.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (14, False, 14, "Uno de los motivos por los que se quiere implementar el programa igualar es por la escasez de ingresos debido a la gran cantidad de tiempo dedicado a las tareas domésticas.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (15, True, NULL, "A nivel mundial, 132 millones de mujeres/niñas no van/no fueron a la escuela.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (16, False, 16, "El país con más mujeres representantes en el parlamento nacional es Cuba.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (17, True, NULL, "Entre 2000 y 2015 se produjeron avances a nivel mundial con relación a la igualdad entre los géneros.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (18, False, 18, "Las mujeres y hombres comparten las mismas necesidades en el espacio público.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (19, True, NULL, "La desigualdad de género provoca el estancamiento del progreso social.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (20, False, 20, "Hoy en día, tanto hombres como mujeres experimentan niveles similares de acoso sexual en el transporte público.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (21, True, NULL, "En 18 países, los esposos pueden impedir legalmente que sus esposas trabajen.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (22, True, NULL, "Las mujeres corren mayores riesgos durante un desastre natural que los hombres.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (23, False, 23, "Alrededor de 100 millones de mujeres en todo el mundo son analfabetas.");""")
conn.commit()

conn.execute("""INSERT INTO Afirmaciones
                    (id_afirmacion, es_correcta, id_respuesta, contenido_afirmacion)
                VALUES
                    (24, True, NULL, "Se identificaron 4 nudos centrales de la desigualdad de género en América Latina.");""")
conn.commit()

conn.execute('''CREATE TABLE IF NOT EXISTS Respuestas
                (id_afirmacion INT,
                id_respuesta INT PRIMARY KEY,
                contenido_respuesta TEXT NOT NULL);''')
conn.commit()

conn.execute("""INSERT INTO Respuestas
                    (id_afirmacion, id_respuesta, contenido_respuesta)
                VALUES
                    (2, 2, "70% de los trabajadores en el sector sanitario y social son mujeres.");""")
conn.commit()

conn.execute("""INSERT INTO Respuestas
                    (id_afirmacion, id_respuesta, contenido_respuesta)
                VALUES
                    (4, 4, "Más de 100 países han tomado medidas para hacer seguimiento de las asignaciones presupuestarias para la igualdad de género.");""")
conn.commit()

conn.execute("""INSERT INTO Respuestas
                    (id_afirmacion, id_respuesta, contenido_respuesta)
                VALUES
                    (6, 6, "La meta principal del ODS 5 es lograr la igualdad de todos los géneros y empoderar a todas las mujeres y las niñas.");""")
conn.commit()

conn.execute("""INSERT INTO Respuestas
                    (id_afirmacion, id_respuesta, contenido_respuesta)
                VALUES
                    (8, 8, "El Programa igualar tiene como fin reducir las separaciones y grietas estructurales de género que existen en el mundo del trabajo, el empleo y la producción desde una mirada interseccional y de derechos humanos.");""")
conn.commit()

conn.execute("""INSERT INTO Respuestas
                    (id_afirmacion, id_respuesta, contenido_respuesta)
                VALUES
                    (10, 10, "La campaña nacional Cuidar en Igualdad involucra al Estado y lo obliga a crear políticas públicas para que los trabajos de cuidado, históricamente considerados del ámbito privado y femeninos, sean públicos y de todos los géneros.");""")
conn.commit()

conn.execute("""INSERT INTO Respuestas
                    (id_afirmacion, id_respuesta, contenido_respuesta)
                VALUES
                    (12, 12, "El programa Producir busca crear o fortalecer proyectos productivos de todo el país, llevados adelante por organizaciones comunitarias en las que participan mujeres y LGBTI+ que estén experimentando o hayan experimentado violencia de género.");""")
conn.commit()

conn.execute("""INSERT INTO Respuestas
                    (id_afirmacion, id_respuesta, contenido_respuesta)
                VALUES
                    (14, 14, "Uno de los motivos por los que se quiere implementar el programa igualar es por los problemas de permanencia en el mundo laboral.");""")
conn.commit()

conn.execute("""INSERT INTO Respuestas
                    (id_afirmacion, id_respuesta, contenido_respuesta)
                VALUES
                    (16, 16, "El país con más mujeres representantes en el parlamento nacional es Rwanda.");""")
conn.commit()

conn.execute("""INSERT INTO Respuestas
                    (id_afirmacion, id_respuesta, contenido_respuesta)
                VALUES
                    (18, 18, "Las necesidades de movilidad, vivienda, trabajo y seguridad de las mujeres son específicas, cambiantes y dependen de su vida familiar, laboral y social.");""")
conn.commit()            

conn.execute("""INSERT INTO Respuestas
                    (id_afirmacion, id_respuesta, contenido_respuesta)
                VALUES
                    (20, 20, "Los casos de víctimas de acoso en el transporte son el 95% mujeres y 5% hombres. Como consecuencia, la inseguridad lleva a muchas mujeres a reducir sus desplazamientos, lo que limita sus oportunidades de educación, laborales y sociales.");""")
conn.commit()            

conn.execute("""INSERT INTO Respuestas
                    (id_afirmacion, id_respuesta, contenido_respuesta)
                VALUES
                    (23, 23, "Aproximadamente 700 millones de personas analfabetas del mundo son mujeres. A pesar de los progresos realizados durante las últimas dos décadas, las niñas aún tienen menos probabilidades que los niños de ir a la escuela. Estas desigualdades siguen estando profundamente arraigadas, y en muchas sociedades la educación de las niñas no se considera una prioridad. De acuerdo con la Unesco, si la actual tendencia continúa, 15 millones de niñas entre 6 y 10 años nunca pondrán un pie en una escuela, en comparación con los 10 millones de niños que tampoco lo harán.");""")
conn.commit()
