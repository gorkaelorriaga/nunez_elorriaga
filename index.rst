.. index.rst

Documentación del módulo Convertir.
==================================================

Bienvenido a la documentación del módudo Convertir, tu módulo de conversiones para el día a día.

.. module:: convertir


Clase CheckErrors
==================

.. autoclass:: CheckErrors
   :members:
   :special-members: __init__, check_is_number, check_input_type
   :exclude-members: __init__, check_is_number, check_input_type

   Esta clase se encarga de comprobar los problemas que puedan darse debido a los inputs del usuario.

   .. automethod:: __init__
      :noindex:

   Inicializa la clase.

   Argumentos:
      - value_or_values (numérico o iterable de numéricos): valor o valores a convertir.
      - measure_from (str): unidad original.
      - measure_to (str): unidad destino.

   .. automethod:: check_is_number
      :noindex:

   Comprueba que el input de cantidad `value_or_values` es numérico o puede ser interpretado como tal. En caso de ser un iterable, comprueba que todos los elementos de este lo sean.

   .. automethod:: check_input_type
      :noindex:

   Comprueba el tipo de variable que el input `value_or_values` es en Python.

Clase MedidaLongitud
======================

.. autoclass:: MedidaLongitud
   :members:
   :special-members: __init__, cambio_longitudes
   :show-inheritance:
   :exclude-members: __init__, cambio_longitudes

   Esta clase se encarga de realizar las conversiones entre unidades de longitud.

   .. automethod:: __init__
      :noindex:

   Inicializa la clase.

   Argumentos:
      - value_or_values (numérico o iterable de numéricos): valor o valores a convertir.
      - measure_from (str): unidad original.
      - measure_to (str): unidad destino.

   .. automethod:: cambio_longitudes
      :noindex:

   Realiza la conversión de medidas.

Clase MedidaArea
=================

.. autoclass:: MedidaArea
   :members:
   :special-members: __init__, cambio_areas
   :show-inheritance:
   :exclude-members: __init__, cambio_areas

   Esta clase se encarga de realizar las conversiones entre unidades de área.

   Argumentos:
      - value_or_values (numérico o iterable de numéricos): valor o valores a convertir.
      - measure_from (str): unidad original.
      - measure_to (str): unidad destino.

   .. automethod:: __init__
      :noindex:

   Inicializa la clase.

   .. automethod:: cambio_areas
      :noindex:

   Realiza la conversión de medidas.

Clase MedidaVolumen
====================

.. autoclass:: MedidaVolumen
   :members:
   :special-members: __init__, cambio_volumenes
   :show-inheritance:
   :exclude-members: __init__, cambio_volumenes

   Esta clase se encarga de realizar las conversiones entre unidades de volumen.


   .. automethod:: __init__
      :noindex:

   Inicializa la clase.

   Argumentos:
      - value_or_values (numérico o iterable de numéricos): valor o valores a convertir.
      - measure_from (str): unidad original.
      - measure_to (str): unidad destino.

   .. automethod:: cambio_volumenes
      :noindex:

   Realiza la conversión de medidas.

Clase MedidasLiquidos
======================

.. autoclass:: MedidasLiquidos
   :members:
   :special-members: __init__, cambio_liquidos
   :show-inheritance:
   :exclude-members: __init__, cambio_liquidos

   Esta clase se encarga de realizar las conversiones entre unidades de líquidos.

   .. automethod:: __init__
      :noindex:

   Inicializa la clase.

   Argumentos:
      - value_or_values (numérico o iterable de numéricos): valor o valores a convertir.
      - measure_from (str): unidad original.
      - measure_to (str): unidad destino.

   .. automethod:: cambio_liquidos
      :noindex:

   Realiza la conversión de medidas.


Clase MedidaTiempo
======================

.. autoclass:: MedidaTiempo
   :members:
   :special-members: __init__, cambio_tiempo, year_month,month_week, week_day, day_hour, hour_minute, minute_second
   :show-inheritance:
   :exclude-members: __init__, cambio_tiempo, year_month,month_week, week_day, day_hour, hour_minute, minute_second

   Esta clase se encarga de realizar las conversiones entre unidades de líquidos.

   .. automethod:: __init__
      :noindex:

   Inicializa la clase.

   Argumentos:
      - value_or_values (numérico o iterable de numéricos): valor o valores a convertir.
      - measure_from (str): unidad original.
      - measure_to (str): unidad destino.

   .. automethod:: year_month
      :noindex:

   Convierte años a meses.

   .. automethod:: month_week
      :noindex:

   Convierte meses a semanas.

   .. automethod:: week_day
      :noindex:

   Convierte semanas a días.

   .. automethod:: day_hour
      :noindex:
   
   Convierte días a horas.

   .. automethod:: hour_minute
      :noindex:

   Convierte horas a minutos.

   .. automethod:: minute_second
      :noindex:

   Convierte minutos a segundos.

   .. automethod:: cambio_tiempo
      :noindex:

   Realiza la conversión de medidas.


Clase Conversor
================

.. autoclass:: Conversor
   :members:
   :special-members: __init__, check_measures
   :show-inheritance:
   :exclude-members: __init__, check_measures

   Esta clase se encarga de realizar las conversiones de cara al usuario.

   .. automethod:: __init__
      :noindex:

   Inicializa la clase.

   Argumentos:
      - value_or_values (numérico o iterable de numéricos): valor o valores a convertir.
      - measure_from (str): unidad original.
      - measure_to (str): unidad destino.

   .. automethod:: check_measures
      :noindex:

   Controla qué conversión aplicar según las medidas provistas como parámetros.