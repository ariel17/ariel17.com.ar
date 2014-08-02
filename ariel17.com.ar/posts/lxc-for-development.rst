.. title: Ambientes de desarrollo con Contenedores Linux
.. slug: lxc-for-development
.. date: 2014/08/02 10:07:23
.. tags: linux, desarrollo, virtualización
.. link: 
.. description: Crear ambientes de desarrollo usando LXC
.. type: text

Linux Containers
================

Pueden obtener más información en la `página oficial de LXC`_.

Instalación
-----------

Para instalar LXC debemos ejecutar los siguientes comandos:

.. code-block:: bash

   ~$ sudo apt-get install lxc

Creación
--------

La creación de containers puede realizarse mediante los templates o indicar
manualmente qué imagen utilizar.

.. code-block:: bash

   ~$ lxc-create -n ubuntu1 -t ubuntu  # creates a container named ubuntu1 using the ubuntu template
   ~$ lxc-create -n ubuntu2 -t ubuntu-cloud -- -r trusty -T http://cloud-images.ubuntu.com/trusty/current/trusty-server-cloudimg-arm64-root.tar.gz

De esta manera, la creación de los containers se realiza sin más intervención
de parte del usuario. También existe una manera de crearlos de manera
interactiva, visualizando las distribuciones y arquitecturas disponibles:

.. code-block:: bash

   ~$ lxc-create -t download -n ubuntu3

Una consola web para controlar a todos
======================================

Existe un proyecto llamado `LXC Web Panel`_ (un `fork del proyecto original`_
para versiones de lxc>=1.0) que es justamente un sito web para la
administración de los contenedores linux. Ofrece además de las herramientas de
control, reportes estadísiticos para la visualización del consumo de recursos
tanto del host como de los contenedores.

Instalando Web Panel
--------------------

Para instalar el panel web debemos agregar el paquete a nuestro repositorio
local, instalarlo y hacer ciertas configuraciones:

.. code-block:: bash

   ~$ wget -O - http://claudyus.github.io/LXC-Web-Panel/claudyus.gpg.key | sudo apt-key add -
   ~$ echo "deb http://claudyus.github.io/LXC-Web-Panel/ ./" | sudo tee /etc/apt/sources.list.d/lwp.list
   ~$ sudo apt-get update
   ~$ sudo apt-get install lwp
   ~$ sudo cp /etc/lwp/lwp.example.conf /etc/lwp/lwp.conf  # using default configuration
   ~$ sudo service lwp start

Vamos a asumir que se usaron las configuraciones por defecto; si realizaron
cambios no olviden adaptar los ejemplos de aquí a sus casos particulares. Una
vez terminada la instalación, abrimos un browser y nos dirigimos a la dirección
web http://localhost:5000/:

.. class:: thumbnail
.. figure:: /galleries/lxc-for-development/login.png
   :width: 100 %
   :scale: 80 %
   :alt: Login en LXC Web Panel.
   :align: center

Usando :code:`admin` como usuario y contraseña por defecto, accederemos al
panel y nos mostrará una visión de los recursos utilizados tanto por el host
como por los contenedores, así como links a diversas configuraciones:

.. class:: thumbnail
.. figure:: /galleries/lxc-for-development/dashboard.png
   :width: 100 %
   :scale: 80 %
   :alt: Dashboard en LXC Web Panel.
   :align: center


   

.. _`página oficial de LXC`: https://linuxcontainers.org/
.. _`LXC Web Panel`: http://claudyus.github.io/LXC-Web-Panel/
.. _`fork del proyecto original`: http://lxc-webpanel.github.io/
.. _`página oficial del panel`: `LXC Web Panel`_
