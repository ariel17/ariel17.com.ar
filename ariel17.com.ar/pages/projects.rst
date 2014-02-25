.. title: Projectos
.. slug: projects
.. date: 2014/02/24 04:08:09
.. tags: 
.. link:
.. description: Una lista de mis proyectos.
.. type: text

#. `Este sitio`_
#. `Poppurri`_

Este sitio
----------
URL
  http://www.ariel17.com.ar/
Repositorio
  https://github.com/ariel17/ariel17.com.ar
Descripción
  Mi página personal donde exponer mis proyectos e intereses profesionales.
Tecnologías utilizadas:
  * Nikola_: Generador de contenido estático hecho en Python_. El tema usado
             se hizo con `Twitter Bootstrap`_, un framework para diseño de
             sitios web que responde a las características del navegador donde
             se está viendo.
  * Nginx_: Un web server liviano y de fácil configuración.
Está activo
  Sí.
Estado
  En desarrollo.

Poppurri
--------
URL
  http://www.poppurri.com.ar/
Repositorio
  https://github.com/ariel17/poppurri
Descripción
  Un sitio de venta de productos manufacturados. La propuesta inicial fue un
  sitio para exponer fotos de la manufactura de familiares directos pero se
  expandió y se encuentra abierto a la comunidad.
Tecnologías utilizadas
  * Django_: Framework Python_ para programación web.
  * Memcache_: Caché centralizada de objetos en memoria.
  * PostgreSQL_: Base de datos relacional.
  * `Twitter Bootstrap`_: Framework para diseño de sitios web. Es sensible a
                          los diferentes tipos de navegador, adaptando la forma
                          de mostrar el contenido.
  * Nginx_: Web server liviano y de fácil configuración, haciendo de proxy
            entre el dominio y la aplicación Django_.
  * Gunicorn_: Un web server WSGI para Unix hecho en Python_. Utiliza el modelo
               pre-fork (1 proceso maestro -- N procesos hijos) para
               administrar cómo se crean los workers.
Está activo
  Sí.
Estado
  En desarrollo.

.. _Nikola: http://getnikola.com/
.. _Django: http://www.djangoproject.com/
.. _Python: http://www.python.org/
.. _PostgreSQL: http://www.postgresql.org/
.. _Memcache: http://memcached.org/
.. _`Twitter Bootstrap`: http://getbootstrap.com/
.. _Nginx: http://nginx.org/ 
.. _Gunicorn: http://gunicorn.org/
