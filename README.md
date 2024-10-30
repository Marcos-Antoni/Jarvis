# API de Lenguaje Natural

Este proyecto es una API construida con **Flask** que utiliza **AWS** para procesar solicitudes a través de un modelo de lenguaje. La API tiene una única ruta `/what` que recibe parámetros de consulta y devuelve una respuesta generada por el modelo.

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Características](#características)
- [Instalación y Uso](#instalación-y-uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuciones](#contribuciones)
- [Recursos Adicionales](#recursos-adicionales)

## Descripción del Proyecto

Este proyecto fue creado para ver qué tan complicado es tener tu propio LLM en internet con la capacidad de interactuar con él desde una API propia.

## Características

- API RESTful construida con Flask.
- Validación de API key.
- Validación de parámetros de entrada.
- Integración con AWS para el procesamiento de lenguaje natural.
- Respuestas en formato JSON.

## Instalación y Uso

**_Nota importante:_** Este proyecto funciona gracias a las configuraciones que hice en AWS que me permiten el acceso a modelos LLM de sus servicios. Si ya configuraste tu AWS entonces solo te falta agregar estas 3 variables de entorno:

```.env
API_KEY = la clave de acceso a tu API
AWS_ACCESS_KEY_ID = ID de identificación de usuario de AWS
AWS_SECRET_ACCESS_KEY = ID de acceso a las herramientas de AWS
```

Para aquellos que quieran instalar el proyecto, sigan estos pasos:

1. Clonen el repositorio:
   ```bash
   git clone https://github.com/Marcos-Antoni/Jarvis.git
   ```
2. Naveguen al directorio del proyecto:
   ```bash
   cd Jarvis
   ```
3. Instalen las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Configuren las variables de entorno necesarias en un archivo `.env`:
   ```
   API_KEY = la clave de acceso a tu API
   ```
5. Ejecuten el proyecto:

   ```bash
   python src/backend/main.py
   ```

6. Abren [http://localhost:5000/what?key={"key"}&ask={"ask"}](http://localhost:5000/what) en su navegador para probar la API.

## Estructura del Proyecto

El proyecto maneja esta estructura de carpetas:

```bash
Jarvies/
├── main.py
└── src/
    ├── routes.py
    ├── what.py
    ├── variablesGlobales.py
    ├── boto3.py
    └── LLM.py
```

- **main.py**: Es el archivo principal que inicia la aplicación Flask.
- **routes.py**: Define las rutas de la API.
- **what.py**: Contiene la lógica para ver si la API_Key es correcta y ejecutar el LLM.
- **variablesGlobales.py**: Define las variables globales utilizadas en el proyecto.
- **boto3.py**: Configura el cliente de AWS Boto3 para interactuar con el LLM.
- **LLM.py**: Llama al cliente Boto3 para obtener respuestas del modelo.

## Contribuciones

Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz un commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Envía un pull request.

## Recursos Adicionales

- [ChatNarsiso](https://github.com/Marcos-Antoni/ChatNarsiso)
- [Documentación de Flask](https://flask.palletsprojects.com/)
- [Documentación de Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS](https://aws.amazon.com/)
