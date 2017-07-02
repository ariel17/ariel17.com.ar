.. title: (x,y)
.. slug: xy
.. date: 2017-07-01 21:34:51 UTC-03:00
.. tags: go, android, idea
.. category: 
.. link: 
.. description: 
.. type: text

Quiero hacer un proyecto personal en Go, tambien quiero hacer uno en Android, y
para aprovechar ambas intenciones voy a usarlas en un mismo objetivo: **un
sistema de rastreo de personas**.

Definicion del *problema*
-------------------------

Un sistema capaz de proveer a un usuario la informacion geografica de ciertos
individuos (previamente indicados por este) y ubicarlos en un mapa. En
condiciones ideales, el margen de error respecto a la posicion real de la
persona no debe superar los 60 segundos. Se debe guardar el historial de
posiciones de los individuos registrados durante el periodo de 1 dia, aun si el
usuario no esta utilizando el sistema.

Analisis
--------

1. Se utilizara el GPS de los dispositivos Android que los individuos porten
   para obtener la informacion geografica. Para obtener acceder a dicha
   informacion es necesario una aplicacion que pueda capturarla y enviarla a un
   punto de reporte.

1. Siendo que la idea es tener informacion de los individuos aun cuando el
   usuario no este usando el sistema, sera necesario tener un punto de
   comunicacion en comun para las partes que idealmente este siempre
   disponible. Se usara un VPS para proveer dicha funcionalidad.
  
1. Siguiendo la linea del punto anterior, se implementara una API REST para la
   comunicacion entre el server y la aplicacion Andriod.

1. El usuario debera tener una interfaz en la cual pueda cargar datos de
   identificacion de los individuos a monitorear. La misma sera una aplicacion
   web que almacene los datos y los disponibilice en el sistema.

1. La interfaz web tambien sera el medio por el cual se visualizara la posicion
   de los individuos.

.. image:: https://raw.githubusercontent.com/ariel17/xy/master/docs/sequence.mmd.png
