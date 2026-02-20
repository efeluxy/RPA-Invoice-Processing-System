MANUAL DE DESPLIEGUE Y EJECUCIÓN - ROBOT ALTA CLIENTES
======================================================

DESCRIPCIÓN
-----------
Este robot automatiza la lectura de facturas PDF desde Outlook, valida duplicados en Excel, da de alta clientes en un CRM Web simulado y registra la actividad en UiPath Orchestrator.

REQUISITOS DEL SISTEMA
----------------------
1. UiPath Studio (Versión 2023.x o superior).
2. Microsoft Outlook (Aplicación de escritorio instalada y logueada).
3. Navegador Google Chrome o Microsoft Edge.
4. Conexión a Internet (para Orchestrator).

ESTRUCTURA DE CARPETAS NECESARIA
--------------------------------
Asegúrese de que dentro de la carpeta del proyecto existen las siguientes rutas. Si no existen, el robot intentará crearlas, pero se recomienda verificar:

* Data\Temp          -> (Aquí se descargarán los PDFs temporalmente)
* Data\Revision      -> (Aquí debe estar el archivo Revision.xlsx)
* Data\CRM_Mock      -> (Aquí debe estar el archivo CRM.html)
* Output\Reports     -> (Aquí se generará el informe final)
* Output\Screenshots -> (Aquí se guardarán las capturas de errores)

CONFIGURACIÓN PREVIA (IMPORTANTE)
---------------------------------
1. CRM MOCK:
   Abra el archivo "Data\CRM_Mock\CRM.html" con su navegador.
   IMPORTANTE: Mantenga esta pestaña abierta antes de iniciar el robot.

2. OUTLOOK:
   Abra la aplicación de Outlook.
   Asegúrese de tener una carpeta o correos en la bandeja de entrada que contengan el asunto "Factura pendiente" y un PDF adjunto.

3. EXCEL:
   Asegúrese de que el archivo "Data\Revision\Revision.xlsx" está CERRADO. Si lo tiene abierto, el robot dará error al intentar escribir.

4. ORCHESTRATOR:
   El robot está configurado para usar la cola "ColaFacturas". Asegúrese de que el Orchestrator conectado tiene esa cola creada o modifique la actividad si usa una carpeta distinta.

CÓMO EJECUTAR
-------------
1. Abra el archivo "Main.xaml" en UiPath Studio.
2. En la cinta de opciones superior, haga clic en la flecha derecha (desplegable) del botón "Depurar" (Botón de play azul) y seleccione "Ejecutar archivo" (Run File).
3. No utilice el ratón ni el teclado mientras el robot opera sobre el formulario web.

VERIFICACIÓN DE RESULTADOS
--------------------------
Al finalizar la ejecución:
1. Revise "Output\Reports\Informe_Ejecucion.txt" para ver el resumen de contadores.
2. Abra "Data\Revision\Revision.xlsx" para ver los clientes añadidos.
3. Verifique en UiPath Orchestrator las nuevas transacciones en la cola.