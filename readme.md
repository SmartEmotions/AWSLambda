# AWS Serverless Con DJango

Este ejemplo no explica sobre el desarrollo de aplicaciones o API con Python Django. Si desea aprender en detalle sobre Django, [Graphene](https://docs.graphene-python.org/projects/django/en/latest/) y otros temas relacionados con el uso para principiantes en este tipo de tecnologías, diríjase a la documentación de cada una para aprender sobre su configuración básica, sin embargo, puede ver el código fuente completo del ejemplo en [**GitHub**](https://github.com/SmartEmotions/AWSLambda-Python), en el archivo requirementes.txt se encuentras las librerías utilizadas.

#### [Ver Artículo Completo en Coneccio](https://coneccio.com/t/serverless-en-aws-lamda-con-python/39)

#### [Ver demo](https://osjfw3bchj.execute-api.us-east-1.amazonaws.com/dev/ingredients?query=query%7B%0A%20%20allCategories%7B%0A%20%20%20%20name%2C%0A%20%20%20%20ingredients%7B%0A%20%20%20%20%20%20name%2C%0A%20%20%20%20%20%20notes%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D)

El ejemplo realiza el modelamiento de una API para Ingredientes y categorías, los modelos se verían como en la imagen, una relación de uno a varios entre categoría e ingrediente en esa dirección.![](/assets/ER AWS Serverless Example.png)Con los modelos se obtendrá en [GraphQL ](https://graphql.org/learn/)los servicios implementados, en el ejemplo están las consultas para obtener las listas tal como se indica en la imagen de ingredientes y categorías, diríjase a [Graphene](https://docs.graphene-python.org/projects/django/en/latest/) si desea aprender más sobre cómo usar esta tecnología.

###### Consulta de Categorías e Ingredientes

```
query{
  allCategories{
    name,
    ingredients{
      name,
      notes
    }
  }
}
```

###### Respuesta de Categorías e Ingredientes

```Json
{
  "data": {
    "allCategories": [
      {
        "name": "Fruit",
        "ingredients": [
          {
            "name": "Apple",
            "notes": "Health food"
          },
          {
            "name": "Banana",
            "notes": "Delicious with potasio"
          }
        ]
      },
      {
        "name": "Vegetal",
        "ingredients": [
          {
            "name": "Letuce",
            "notes": "Great at launch"
          }
        ]
      },
      {
        "name": "Protein",
        "ingredients": []
      }
    ]
  }
}
```

## Zappa

Es una librería de Python para el desarrollo rápido de aplicaciones en Serverless de AWS Lambda. Con el proyecto base para iniciar, lo primero es configurar los accesos de Amazon Web Services.

```
aws configure
```

Configuré las llaves obtenidas de AWS en IAM, recuerde, las llaves deben tener los permisos anteriormente mencionados en este artículo, este paso se recomienda hacer uso de entornos virtuales para Python de ese modo las llaves se guardarán en un segmento aislado del sistema operativo, los parámetros solicitados son el AWS\_KEY\_ID\_ y el \_AWS\_SECRET\_ID.

```
zappa init
```

Ahora puede iniciar la configuración del proyecto para ser lanzado en AWS Lambda, el resultado de este comando es un objeto JSON en la base del proyecto `zappa_settings.json`: **AWS Region**, es la zona geográfica dispuesta por AWS, es posible personalizar otra zona, diríjase a AWS Región para conocer más sobre las opciones a elegir; **DJango Settings**, es la configuración que se tomará para la función lambda, por defecto se adhiere la configuración del proyecto base, es posible personalizar dependiente del entorno de desarrollo \(muy recomendable\) de ese modo cada entorno puede tener su base de datos, etc. **S3 Bucket**, es el nombre del bucket donde se almacenarán los archivos estáticos, además se usa S3 para empaquetar todo el proyecto y luego desplegarlo en AWS Lambda, este proceso lo hace Zappa y es transparente en el despliegue.

```JSON
{
    "dev": {
        "aws_region": "us-east-1",
        "django_settings": "AWSLambda.settings",
        "profile_name": "default",
        "project_name": "awslambda",
        "runtime": "python3.6",
        "s3_bucket": "zappa-r7ob6ry3q"
    }
}
```

El primer despliegue realiza la configuración iniciale en AWS Lambda,  por lo tanto se ejecuta en la terminal.

`zappa deploy`

Cuando se realicen actualizaciónes solo agregue.

`zappa update`
