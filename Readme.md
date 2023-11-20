<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL ML-OPS** </h1>

<p align=center><img src=https://ubuntucommunity.s3.dualstack.us-east-2.amazonaws.com/original/3X/5/5/559eebb1b680098adc83ef22cbba1078d3b43033.png><p>

# <h1 align=center> **Introducción** </h1>

El desafío que se plantea en este proyecto es el desarrollo de un proceso de Machine Learning Operations (MLOps) integral que abarque diversas etapas fundamentales. Comenzando con la Ingeniería de Datos, se llevará a cabo la Extraction, Transform and Load (ETL) de manera eficiente y efectiva. Posteriormente, se adentrará en el terreno del Machine Learning, donde se realizará un exhaustivo Exploratory Data Analysis (EDA) para comprender en profundidad los datos. Además, se explorarán y entrenarán múltiples modelos para encontrar la mejor solución. El proyecto culminará con la implementación de un sistema de deployment que no solo abarca el modelo, sino también los datos del proceso ETL. 

# <h1 align=center> **Índice** </h1>

- [Transform and Load (ETL)](#transform-and-load-etl)
- [Análisis Exploratorio de Datos (EDA)](#análisis-exploratorio-de-datos-eda)
- [Desarrollo de la aplicación de FAST API](#desarrollo-de-la-aplicación-de-fast-api)
- [Sistema de recomendación](#sistema-de-recomendación)
- [Video](#video)
- [Fuentes de datos](#fuentes-de-datos)
- [Carpeta Entregables](#carpeta-entregables)
- [Autor](#autor)

# <h1 align=left> **Desarrollo del Proyecto**</h1>

## **Transform and Load** (ETL)

En mi rol de Data Engineer, hemos abordado con éxito el proceso de Extraction, Transform, and Load (ETL) como parte fundamental de este proyecto. A continuación, destacaré algunos de los pasos clave en el proceso, que se encuentran detallados en el archivo [ETL.ipynb](Entregables/ETL.ipynb) junto con comentarios paso a paso. Aunque estos pasos están enumerados en un orden específico, es importante tener en cuenta que algunos de ellos se repiten a lo largo del flujo de trabajo:

+ **Extracción de Datos**: En este primer paso, se extrajeron los datos de las fuentes pertinentes, como bases de datos, archivos, o servicios web. Esto garantiza que tengamos acceso a la información necesaria.

+ **Limpieza de Datos**: Se realizó una limpieza exhaustiva de los datos para abordar problemas como valores nulos, duplicados o inconsistencias. Esta etapa es crucial para asegurar la calidad de los datos.

+ **Transformación de Datos**: Se aplicaron transformaciones a los datos, como la conversión de tipos de datos, la normalización y la agregación. Estas transformaciones preparan los datos para su posterior análisis y modelado.

+ **Validación y Verificación de Datos**: En este punto, se llevaron a cabo controles de calidad para asegurarse de que los datos procesados sean precisos y confiables.

+ **Repetición de Pasos Anteriores**: Algunos de los pasos mencionados anteriormente, como la limpieza y la transformación de datos, se repitieron a medida que se descubrieron nuevos problemas o se obtuvieron datos adicionales.

+ **Exportación de Datos Procesados**: Una vez que los datos estuvieron listos, se exportaron en el formato adecuado para su posterior uso en el proceso de Machine Learning.

## **Análisis Exploratorio de Datos** (EDA)

Se realizó un análisis en profundidad de los datos para comprender sus características, distribuciones y relaciones. Esto ayudó a identificar patrones y tendencias que serán útiles en etapas posteriores. El detalle completo de este proceso se encuentra registrado paso a paso en el archivo [EDA.ipynb](Entregables/EDA.ipynb), lo que nos ha permitido responder algunas preguntas clave, como:

### `¿Cuáles son los "Developers" con más usuarios?` 
### `¿Cuáles son los juegos con mayor recomendación?`
### `¿Cuál es la cantidad de tipo de sentimiento por análisis?`
### `¿Cuáles son los juegos con más tiempo de juego?`
### `¿Cuáles son los Géneros más jugados?`

# **Desarrollo de la aplicación de FAST API**

*La implementación de una API con FastAPI para servir los datos de la empresa y su posterior implementación en `Render` para su consumo en la web es una estrategia efectiva para hacer que los datos sean accesibles y utilizables por diversos departamentos y aplicaciones. Aquí están algunas de las consultas que se llevarón acabo para esta API:*

+ **def developer( desarrollador : str )**: Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.

+ **def userdata( User_id : str )**: Debe devolver cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.

+ **def UserForGenre( genero : str )**: Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

+ **def best_developer_year( año : int )**: Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)

+ **def developer_reviews_analysis( desarrolladora : str )**: Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

La aplicación se encuentra disponible en [la siguiente ubicación](https://proyecto-ml-ops-epok.onrender.com/docs). Tener en cuenta que `Render` apaga las aplicaciones, dar tiempo a que construya el contenedor y reinicie la app.


### **Sistema de recomendación**

Una vez que todos los datos son accesibles a través de la API y están disponibles para su uso por los departamentos de Analytics y Machine Learning, y después de haber realizado un análisis exploratorio de datos (EDA) que nos brinda una comprensión profunda de la información a nuestra disposición, es el momento de avanzar en el entrenamiento de nuestro modelo de Machine Learning para construir un sistema de recomendación.

Instanciamos nuestro modelo utilizando la librería `surprise` y hemos creado nuestra propia escala de calificación de juegos, que llamamos `rating`. Luego, procedimos a dividir los datos para poder entrenar el modelo de manera efectiva. Una vez completada esta etapa, hemos empleado el algoritmo de *Singular Value Decomposition (SVD)* para llevar a cabo el entrenamiento de nuestro modelo de recomendación.

Los detalles exhaustivos de todo este proceso se encuentran disponibles en el archivo [ML.ipynb](Entregables/ML.ipynb). Después de completar el entrenamiento del modelo, lo hemos guardado en un archivo con extensión `.pkl` llamado [modelo_de_ML.pkl](modelo_de_ML.pkl). Esta acción nos permitirá utilizar el modelo de manera eficaz en nuestra función dentro de la API.

Este modelo entrenado con SVD está listo para generar recomendaciones precisas y personalizadas basadas en las calificaciones y preferencias de los usuarios, contribuyendo así a mejorar la experiencia de los usuarios y a impulsar las estrategias de retención y fidelización.

+ **def recomendacion_usuario( id de usuario )**: Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.

La aplicación la podras encontrar abajo como la última funció disponible en [la siguiente ubicación](https://proyecto-ml-ops-epok.onrender.com/docs)

## **Video**

[Mirar el Video](https://www.youtube.com/watch?v=OrVL2gzds40)

## Carpeta Entregables

+ [ETL](Entregables/ETL.ipynb)
+ [EDA](Entregables/EDA.ipynb)
+ [Machine learning](Entregables/ML.ipynb)

## Fuentes de datos

### El repositorio no contiene los datos originales provistos para el proyecto, los mismos pueden ser encontrados en las siguientes ubicaciones:

+ [Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj): Carpeta con el archivo de origen en formato .json (steam_games.json).
+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit#gid=0): Diccionario con algunas descripciones de las columnas disponibles en el dataset.
<br/>

## Autor

+ Mariano Emanuel Baigorria
+ [GitHub](https://github.com/Marianoe155)
+ [Linkedin](https://www.linkedin.com/in/mariano-baigorria-b85004282/)

