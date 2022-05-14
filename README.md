# Sistemas de Recuperación de Información

---

Implementación de los modelos clásicos de Sistemas de Recuperación de Información para 
propósitos escolares.

Claudia Olavarrieta Martínez C511

Marcos Adrián Valdivié Rodríguez C512

---

## Módulo **_basics_** y Jerarquía de clases

El módulo **_basics_** consta de las definiciones de clases usadas comunmente por todos los modelos
utilizados en la aplicación.

- __BasicModel:__ Constituye la clase básica para todos los modelos, esta clase recibe en su constructor
 objetos de tipo __BasicStorage__, __Vectorizer__, __BasicConsultor__, __BasicProcessor__ y 
 __BasicQueryProcessor__ que utilizan para almacenar y analizar los documentos y las consultas. Además
 posee los métodos AddDocument que se encarga de analizar un documento y guardarlo en el Storage, y el 
 método abstracto Consult, que dada una consulta debe retornar el conjunto de documentos relevantes a ella.
 
- __BasicConsultor:__ Constituye la clase básica para definir una consulta para un modelo en específico,
contiene un método abstracto llamado Consult que dado un conjunto de documentos y una consulta debe
retornar los documentos relevantes a dicha consulta.

- __BasicProcessor:__ Constituye la clase básica para definir la forma en que un documento será 
analizado para obtener su representación vectorial. Recibe como argumento un objeto de la clase 
__Vectorizer__ y contiene un método abstracto llamado ProcessDocument que dado un documento debe 
retornar la representación vectorial del mismo.

- __BasicQueryProcessor:__ Constituye la clase básica para definir la forma en que una consulta será 
analizada para obtener su representación vectorial. Recibe como argumento un objeto de la clase 
__Vectorizer__ y contiene un método abstracto llamado ProcessQuery que dado una consulta debe 
retornar la representación vectorial de la misma.

- __BasicStorage:__ Constituye la clase básica para representar la forma en que los documentos serán
manipulados y guardados. Contiene los métodos abstractos __SaveDocument__, __GetAllDocuments__, 
__GetDocuments__ y __GetDocumentRepresentations__.

- __Consult y Document:__ Constituyen las clases básicas para representar respectivamente una consulta
y un documento. Contiene campos relevantes a estas entidades como el conjunto de documentos relevantes
en el caso de las consultas y el titulo o autor en el caso de los documentos. 

- __Utils:__ Contiene métodos necesarios para las operaciones entre vectores: dot (que realiza el 
producto escalar entre dos vectores), angle (que retorna el coseno del ángulo entre dos vectores) y
normalize (que normaliza un vector dividiendo cada elemento del mismo por su mayor valor).

- __Vectorizer:__ Contiene los métodos y atributos necesarios para procesar un vector para cada uno de 
los modelos implementados. Utiliza el objeto EnglishStemmer de nltk para realizar un stemming de los
 documentos y las consultas y los objetos CountVectorizer y TfidfTransformer de sklearn para obtener
 los vectores representativos.
 
## Módulo **_fileProcessing_**  

Este módulo contiene los métodos necesarios para abrir, leer y parsear los sets de datos
suministrados. Actualmente solo se encuentra implementado el parser para el set de datos
__cran__.

## Módulo **_metrics_**

Este módulo contiene tres ficheros, encargados de, dado un conjunto de documentos y consultas
analizar y medir la efectividad de los modelos implementados utilizando las medidas de 
_Presición_, _Recobrado_ y la medida de _Medium Average Presicion_ para los modelos que
poseen función de ranking.

## Módulos **_boolean_**, **_vectorial_** y **_probabilistic_**

Estos módulos contienen las implementaciones específicas de las clases básicas
del módulo __basics__ para cada uno de los modelos estudiados. 

## Archivo **_InMemoryStorage_**

Este archivo contiene una implementación de la clase __BasicStorage__ que maneja el conjunto
de documentos como objetos existentes en la memoria del programa.

---

## Algunos detalles de implementación

La función de consulta para el modelo booleano resultó extremadamente ineficiente para
el conjunto de consultas y documentos proporcionados en el dataset __cran__, ya que al
no existir una coincidencia total entre las consultas y los documentos, estas retornaban
siempre una lista vacía de documentos relevantes. Por lo tanto, se decidió extender
esta función de consulta para aceptar un cierto grado de proximidad, retornando aquellos
documentos para los que la cantidad de términos que pertenecen a la consulta pero no al 
documento sea menor que un umbral dado.

Se implementó la clase __Vectorizer__ del módulo __basics__ para que cumpla los siguientes
requisitos:
- Sea capaz se realizar un stemming de los términos usados en los documentos. Para esto se 
utilizó la clase EnglishStemmer del módulo nltk.
- Sea capaz de encontrar términos que sean posibles stopwords, para esto se hizo uso del
parámetro max_df de la clase CountVectorizer del módulo sklearn.feature_extraction.text,
se definió este parámetro con un valor del 0.85 para indicar que se ignore cualquier término
que aparezca en más del 85% del total de documentos.
- Sea capaz de obtener la representación vectorial para los distintos modelos. Para los
modelos booleano y probabilístico se utilizó el parámetro binary de la clase CountVectorizer,
el cual indica que la vectorización de los documentos se debe realizar teniendo en cuenta
solamente la pertenencia o no a cada documento. En el caso del modelo vectorial, se utilizó
la clase TfidfTransformer del mismo módulo para, dado un conjunto de documentos inicial,
y la representación de la cantidad de veces que aparece cada término en un documento dado,
retornar el vector tf-idf de dicho documento. 

Para los modelos binarios y probabilístico se utilizó en todo momento objetos de la clase
csr_matrix (matrix esparcida) del módulo scipy, para de esta forma ganar en cuanto a 
complejidad espacial y temporal de los algoritmos.

  
##Ejecución

Para ejecutar el proyecto debe ejecutar el siguiente comando en la carpeta app:

```bash
python manage.py runserver
```

 