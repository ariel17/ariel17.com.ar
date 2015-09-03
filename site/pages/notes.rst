.. title: Apuntes
.. slug: notes
.. date: 2014/04/18 01:19:13
.. tags: aprender
.. link: 
.. description: 
.. type: text

.. class:: thumbnail
.. figure:: /galleries/projects/notes_full.png
   :target: http://www.ariel17.com.ar/notes/
   :width: 800 px
   :scale: 50%
   :alt: Apuntes en Sphinx
   :align: right

:Página web: http://www.ariel17.com.ar/notes/

El proyecto puede considerarse un experimento para reemplazar la acción de
tomar apuntes en papel para cualquier materia de estudio. Concretamente no
difiere la forma de tomarlos (es una cuestión personal) sino del medio
utilizado y la posibilidad de perpetuación, disponibilidad y facilidad de
distribución en caso de desear compartir el contenido.

Tecnologías utilizadas
----------------------

* reStructuredText_ (rst): es la sintaxis utilizada para generar el contenido de
  los resúmenes. La sintaxis es muy simple y se pueden aprender las
  particularidades a medida que se avanza. Tiene soporte para expresiones
  matemáticas en LaTex_.

* Sphinx-doc_: es una herramienta que facilita la conversión de contenido rst a
  un formato de salida especificado. En particular, para este proyecto se
  puede generar formato HTML y ePub_.

* git_: es un administrador de versiones de código fuente distribuido. Como el
  contenido se escribe en texto plano y tiene una sintaxis que debe ser
  respetada, se lo puede tratar como un proyecto de desarrollo y utilizar
  herramientas propias de este ámbito para su administración; en particular ésta
  es muy útil para preparar contenido de forma incremental separando lo que está
  listo para ser subido.

* Nginx_: un web server liviano para servir las páginas generadas.

* Ubuntu_: un sistema operativo Linux basado en Debian_, que se hace de
  servidor para el proyecto.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _LaTeX: http://www.latex-project.org/
.. _Sphinx-doc: http://sphinx-doc.org/
.. _ePub: http://es.wikipedia.org/wiki/EPUB
.. _git: http://git-scm.com/
.. _Nginx: http://nginx.org/
.. _Ubuntu: http://www.ubuntu.com/
.. _Debian: https://www.debian.org/
