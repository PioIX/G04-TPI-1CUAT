#  Trabajo integrador interdisciplinario Grupo N°04
División: 5B Informática 

### Integrantes:<br/> 
- Iara Mareco<br/>
- Martina Parodi<br/>
- Candela Taito<br/>
- Julieta Vazquez<br/>

# Verdadero o falso sobre el ODS de Igualdad de género y el empoderamiento de la mujer (ODS 5)<br/>

## Introducción: <br/>

Nuestro trabajo cuenta con el objetivo de divulgar información sobre el ODS 5.<br/>
Para ello vamos a crear un juego de verdadero o falso con 12 afirmaciones y cada pantalla tendrá una imagen de una mujer o varias mujeres. Primeramente, en la pantalla de inicio, va a contener un párrafo con las nociones generales de la Agenda 2030; de esta forma el jugador va a poder conocer un poco la agenda antes de profundizar en el ODS seleccionado. Luego, al comenzar el juego, cuando se aprete la opción correcta va a aparecer un cartel verde que diga "correcto!", y en cambio, cuando se responda mal va a mostrar un cartel rojo que diga "incorrecto" y en este último caso va a aparecer un breve texto desarrollando el por qué. Además, va a contar con un contador de puntaje obtenido hasta el momento; si se acierta se suma un punto y en caso contrario no se suma. Y, para que no aparezcan siempre las mismas afirmaciones en sus respectivas pantallas, vamos a almacenar en la base de datos 24 preguntas y posteriormente mostrarlas alternando su orden (es decir, que se muestren en orden aleatorio). Al terminar el juego se mostrará una pantalla que indique el puntaje y el tiempo transcurrido en responder todas las preguntas.

Boceto de la idea:

![Boceto](https://user-images.githubusercontent.com/100932704/175573120-eaf5c856-8a73-48f9-a44b-be86ff9d837e.jpg)

Nombre y diagrama de las bases de datos:

![Diagrama bases de datos ODS proyecto](https://user-images.githubusercontent.com/100931968/177585734-482e6ad5-19df-4534-9c3c-2a852a0ab8f8.png)

Tabla de las afirmaciones:

![Afirmaciones ODS](https://user-images.githubusercontent.com/100931968/178121525-77e71136-f0d0-49bf-ae82-a3e181a5f0d9.jpg)

Tabla de las respuestas:

![Respuestas ODS](https://user-images.githubusercontent.com/100931968/178121535-d6026674-ff87-4518-b1f3-55ba183f409e.jpg)

NOTA: En total van a ser 24 afirmaciones, pero por ahora en la tabla usamos 9.

Funcionalidad <br/>
- Único jugador <br/>
- Una ronda con 12 afirmaciones <br/>
- Puntaje acumulable <br/>
- Tiempo transcurrido <br/>

Nociones generales <br/>
El Objetivo 5 busca ponerle un fin a cualquier manera de discriminación o violencia contra todas las mujeres y las niñas.
La Agenda 2030 reconoce que las mujeres y las niñas son sujetos de discriminación y violencia en todos los lugares del mundo. La igualdad entre los géneros no es solo un derecho humano fundamental, sino la base para conseguir un mundo próspero y sostenible. Este ODS es fundamental para las mujeres jóvenes y niñas, ya que al igual que cualquier persona, les corresponde la facilidad del acceso a la educación; al trabajo, atención médica y a las decisiones políticas y económicas. Para  lograr este objetivo, es necesario modificar las leyes discriminatorias y adoptar otras que promuevan activamente la igualdad.

Afirmaciones que se le van a plantear al jugador y si son correctas o no. <br/>
- Mayormente, las mujeres y/o niñas víctimas de violencia de género tienen entre  15 y 60 años. correcta
- 40% de los trabajadores en el sector sanitario y social son mujeres. incorrecta
70% de los trabajadores en el sector sanitario y social son mujeres.
- La meta principal del ODS 5 es evitar la violencia y discriminación de género en cualquier ámbito. incorrecta
La meta principal del ODS 5 es lograr la igualdad de todos los géneros y empoderar a todas las mujeres y las niñas.
- El organismo responsable de las metas priorizadas de la ODS 5 es el Ministerio de las Mujeres, Géneros y Diversidad. correcta
- El Programa igualar propone dar charlas en distintos espacios públicos para dar a entender sobre el propósito de la ODS 5 y concientizar sobre la igualdad de género planteada por este objetivo. incorrecta
El Programa igualar tiene como fin reducir las separaciones y grietas estructurales de género que existen en el mundo del trabajo, el empleo y la producción desde una mirada interseccional y de derechos humanos. 
- Uno de los conflictos que enfrentan las mujeres y las niñas diaramente que reconoce y plantea la ODS 5 es la dificultad  para acceder a la tierra, la tecnología, los mercados, la infraestructura y los servicios. correcta
- La campaña nacional "cuidar en igualdad" reúne a 14 organismos del poder ejecutivo nacional para debatir y planificar políticas que aporten a una redistribución entre géneros y que aporten a reconocer el cuidado como una necesidad, como un trabajo y como un derecho. incorrecta
La campaña nacional "cuidar en igualdad" involucra al Estado y lo obliga a crear políticas públicas para que los trabajos de cuidado, históricamente considerados del ámbito privado y femeninos, sean públicos y de todos los géneros.
- La Meta 5.1 la cual busca "darle un fin a todas las formas de discriminación contra todas las mujeres, niñas, niños y niñes LGBTI+ garantizando la igualdad de oportunidades en todo el mundo" es una meta adaptada recientemente. correcta
- El programa producir fue hecho para la prestación económica, asistencia psicológica y asesoramiento legal a las mujeres. incorrecta
El programa producir busca crear o fortalecer proyectos productivos de todo el país, llevados adelante por organizaciones comunitarias en las que participan mujeres y LGBTI+ que estén experimentando o hayan experimentado violencia de género.
- La meta 5.4 la cual busca "reconocer y valorar los cuidados y el trabajo doméstico no remunerados mediante servicios públicos, infraestructuras y políticas de protección social y promoviendo la responsabilidad compartida en el hogar y la familia, según proceda el país" todavía no fue adaptada. correcta
- Uno de los motivos por los que se quiere implementar el programa igualar
es por la escasez de ingresos debido a la gran cantidad de tiempo dedicada a las tareas domésticas. incorrecta
Uno de los motivos por los que se quiere implementar el programa igualar es por los problemas de permanencia en el mundo laboral.

Tareas <br/>
1. Investigación y redacción de preguntas y sus respuestas<br/>
2. Diseño de imagen y de la UI<br/> 
3. Diseño de la base de datos<br/>
4. Funciones de interacción con la base (API, Flask) <br/>
5. Front-end del juego (HTML, CSS, JS) <br/>
6. Testeo <br/>
7. Puesta en producción <br/>

Reponsabilidades <br/>
1. Mareco: 2.5 <br/>
2. Parodi: 3.6.7 <br/>
3. Taito: 1.6.3 <br/>
4. Vazquez: 2.4 <br/>

Primer entregable (30/6)
- Estructura de la base de datos<br/>
- Preguntas y respuestas<br/>
- Reglas y puntajes<br/>
- Maqueta html<br/>

Segundo entregable (7/7)
- API en flask de preguntas y respuestas<br/>
- UI de preguntas y respuetas en conjunto con back-end<br/>
- Pruebas de juego<br/>

Tercer entregable (14/7) <br/>
- Juego completo en línea


# Índice:
- [App de Flask](https://github.com/PioIX/replit_grupo04)<br/>
- [Presupuesto](https://github.com/PioIX/G04-TPI-1CUAT/blob/87e63d234e1c988918586f3fc07d7791ab994fe8/Presupuesto.md)<br/>



