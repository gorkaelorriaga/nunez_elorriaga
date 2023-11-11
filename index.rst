.. index.rst

Documentación del Módulo convertir.
============================================

.. automodule:: convertir
   :members:
   :undoc-members:
   :show-inheritance:

Clase CheckErrors
================

.. autoclass:: CheckErrors
   :members:
   :special-members: __init__, check_is_number, check_input_type, check_measures
   :show-inheritance:

   Esta clase se encarga de comprobar los problemas que puedan darse debido a los inputs del usuario.

   .. automethod:: __init__
      :noindex:

      Inicializa la clase.

   .. automethod:: check_is_number
      :noindex:

      Comprueba que el input de cantidad `value_or_values` es numérico o puede ser interpretado como tal. En caso de ser un iterable, comprueba que todos los elementos de este lo sean.

   .. automethod:: check_input_type
      :noindex:

      Comprueba el tipo de variable que el input `value_or_values` es en Python.

   .. automethod:: check_measures
      :noindex:

      Comprueba la categoría de unidad (moneda/longitud/área/volúmen/líquido) que se ha introducido a los inputs de unidad `measure_from` y `measure_to`.

Clase MedidaLongitud
====================

.. autoclass:: MedidaLongitud
   :members:
   :special-members: __init__, cambio_medidas
   :show-inheritance:

   Esta clase se encarga de realizar las conversiones entre unidades de longitud.

   .. automethod:: __init__
      :noindex:

      Inicializa la clase.

   .. automethod:: cambio_medidas
      :noindex:

      Realiza la conversión de medidas.

Clase MedidaArea
================

.. autoclass:: MedidaArea
   :members:
   :special-members: __init__, cambio_medidas
   :show-inheritance:

   Esta clase se encarga de realizar las conversiones entre unidades de área.

   .. automethod:: __init__
      :noindex:

      Inicializa la clase.

   .. automethod:: cambio_medidas
      :noindex:

      Realiza la conversión de medidas.

Clase MedidaVolumen
==================

.. autoclass:: MedidaVolumen
   :members:
   :special-members: __init__, cambio_medidas
   :show-inheritance:

   Esta clase se encarga de realizar las conversiones entre unidades de volumen.

   .. automethod:: __init__
      :noindex:

      Inicializa la clase.

   .. automethod:: cambio_medidas
      :noindex:

      Realiza la conversión de medidas.

Clase MedidasLiquidos
=====================

.. autoclass:: MedidasLiquidos
   :members:
   :special-members: __init__, cambio_medidas
   :show-inheritance:

   Esta clase se encarga de realizar las conversiones entre unidades de líquidos.

   .. automethod:: __init__
      :noindex:

      Inicializa la clase.

   .. automethod:: cambio_medidas
      :noindex:

      Realiza la conversión de medidas.