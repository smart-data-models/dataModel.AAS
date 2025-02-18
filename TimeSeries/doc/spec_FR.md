<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Série temporelle  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.AAS/blob/master/TimeSeries/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Les séries temporelles peuvent représenter des données brutes, mais aussi des caractéristiques principales, des descriptions textuelles ou des événements de manière concise**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une voie publique    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `timeSeries[object]`: Objet principal du modèle TimeSeries  	- `metadata[object]`:  Ensemble de données décrivant et fournissant des informations sur la série temporelle.    
	- `segments[array]`: Liste des segments de séries temporelles    
- `type[string]`: Type d'INSG. Il doit s'agir de TimeSeries  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `timeSeries`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TimeSeries:    
  description: 'Time Series can represent raw data, but can also represent main characteristics, textual descriptions or events in a concise way.'    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Relationship    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    timeSeries:    
      description: Main object for TimeSeries model    
      properties:    
        metadata:    
          description: ' A set of data describing and providing information about the time series'    
          properties:    
            description:    
              description: Short description of the time series    
              type: string    
              x-ngsi:    
                type: Property    
            name:    
              description: Meaningful name for labeling    
              type: string    
              x-ngsi:    
                type: Property    
            record:    
              description: A time series record is unique by its ID within the time series and contains the timestamps and variable values referenced to the ID    
              properties:    
                sampleAccelerationX:    
                  description: Acceleration along the x-axis    
                  type: number    
                  x-ngsi:    
                    type: Property    
                sampleAccelerationY:    
                  description: Acceleration along the y-axis    
                  type: number    
                  x-ngsi:    
                    type: Property    
                sampleAccelerationZ:    
                  description: Acceleration along the z-axis    
                  type: number    
                  x-ngsi:    
                    type: Property    
                time:    
                  description: Time of time series record    
                  type: string    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        segments:    
          description: List of time series segments    
          items:    
            properties:    
              description:    
                description: Description of the time series segment    
                type: string    
                x-ngsi:    
                  type: Property    
              duration:    
                description: 'Period covered by the segment, represented according to ISO 8601'    
                type: string    
                x-ngsi:    
                  type: Property    
              endTime:    
                description: Contains the last recorded timestamp of the time series segment    
                type: string    
                x-ngsi:    
                  type: Property    
              externalSegment:    
                description: Reference to a file of data points in sequential order over a period of time    
                properties:    
                  data:    
                    description: ' Sequence of data points in sequential order over a period of time '    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              internalSegment:    
                description: Grouped sequence of data points in successive order over a specified period of time    
                properties:    
                  records:    
                    description: List of data points in successive order over a specified period of time    
                    items:    
                      description: Items of the record    
                      properties:    
                        record00:    
                          description: A time series record is unique by its ID within the time series and contains the timestamps and variable values referenced to the ID    
                          properties:    
                            sampleAccelerationX:    
                            sampleAccelerationY:    
                            sampleAccelerationZ:    
                            time:    
                          type: object    
                          x-ngsi:    
                            type: Property    
                      type: object    
                      x-ngsi:    
                        type: Property    
                    type: array    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              lastUpdate:    
                description: Time of the last chance    
                type: string    
                x-ngsi:    
                  type: Property    
              linkedSegment:    
                description: Reference to an endpoint of data points in sequential order over a period of time    
                properties:    
                  endpoint:    
                    description: 'Specifies a location of a resource on an API server through which time series can be requested '    
                    type: string    
                    x-ngsi:    
                      type: Property    
                  query:    
                    description: Generic query component to read time series data from an API    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              name:    
                description: Name of the time series segment    
                type: string    
                x-ngsi:    
                  type: Property    
              recordCount:    
                description: Indicates how many records are present in a segment    
                type: number    
                x-ngsi:    
                  type: Property    
              samplingInterval:    
                description: The time period between two time series records    
                type: number    
                x-ngsi:    
                  type: Property    
              samplingRate:    
                description: Defines the number of samples per second for a regular time series in Hz    
                type: number    
                x-ngsi:    
                  type: Property    
              startTime:    
                description: Contains the first recorded timestamp of the time series segment    
                type: string    
                x-ngsi:    
                  type: Property    
              state:    
                description: State of the time series related to its progress    
                type: number    
                x-ngsi:    
                  type: Property    
            type: object    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI type. It has to be TimeSeries    
      enum:    
        - TimeSeries    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - timeSeries    
  type: object    
  x-derived-from: https://industrialdigitaltwin.org/wp-content/uploads/2023/03/IDTA-02008-1-1_Submodel_TimeSeriesData.pdf    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2025 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AAS/blob/master/TimeSeries/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.TimeSeries/TimeSeries/schema.json    
  x-model-tags: TimeSeries    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### TimeSeries NGSI-v2 key-values Exemple  
Voici un exemple de TimeSeries au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "TimeSeriesData",  
    "type": "TimeSeries",  
    "timeSeries": {  
        "segments": [  
            {  
                "name": "",  
                "description": "",  
                "recordCount": 13134,  
                "startTime": "2020-09-19T14:40:38.318",  
                "endTime": "2020-09-19T14:40:38.318",  
                "duration": "P3DT4H59M",  
                "samplingInterval": 1,  
                "samplingRate": 3200,  
                "state": 0,  
                "lastUpdate": "2020-09-19T14:40:38.318",  
                "externalSegment": {  
                    "data": ""  
                },  
                "linkedSegment": {  
                    "endpoint": "",  
                    "query": ""  
                },  
                "internalSegment": {  
                    "records": [  
                        {  
                            "record00": {  
                                "time": "2020-09-19T14:40:38.318",  
                                "sampleAccelerationX": 0.0,  
                                "sampleAccelerationY": 0.0,  
                                "sampleAccelerationZ": 0.0  
                            }  
                        }  
                    ]  
                }  
            }  
        ],  
        "metadata": {  
            "name": "",  
            "description": "",  
            "record": {  
                "time": "2020-09-19T14:40:38.318",  
                "sampleAccelerationX": 0.0,  
                "sampleAccelerationY": 0.0,  
                "sampleAccelerationZ": 0.0  
            }  
        }  
    }  
}  
```  
</details>  
#### TimeSeries NGSI-v2 normalisé Exemple  
Voici un exemple de TimeSeries au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec l'INSG-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "TimeSeriesData",  
    "type": "TimeSeries",  
    "timeSeries": {  
        "type": "StructuredValue",  
        "value": {  
            "segments": [  
                {  
                    "name": "",  
                    "description": "",  
                    "recordCount": 13134,  
                    "startTime": "2020-09-19T14:40:38.318",  
                    "endTime": "2020-09-19T14:40:38.318",  
                    "duration": "P3DT4H59M",  
                    "samplingInterval": 1,  
                    "samplingRate": 3200,  
                    "state": 0,  
                    "lastUpdate": "2020-09-19T14:40:38.318",  
                    "externalSegment": {  
                        "type": "StructuredValue",  
                        "value": {  
                            "data": ""  
                        }  
                    },  
                    "linkedSegment": {  
                        "type": "StructuredValue",  
                        "value": {  
                            "endpoint": "",  
                            "query": ""  
                        }  
                    },  
                    "internalSegment": {  
                        "type": "StructuredValue",  
                        "value": {  
                            "records": [  
                                {  
                                    "type": "StructuredValue",  
                                    "value": {  
                                        "record00": {  
                                            "type": "StructuredValue",  
                                            "value": {  
                                                "time": "2020-09-19T14:40:38.318",  
                                                "sampleAccelerationX": 0,  
                                                "sampleAccelerationY": 0,  
                                                "sampleAccelerationZ": 0  
                                            }  
                                        }  
                                    }  
                                }  
                            ]  
                        }  
                    }  
                }  
            ],  
            "metadata": {  
                "type": "StructuredValue",  
                "value": {  
                    "name": "",  
                    "description": "",  
                    "record": {  
                        "time": "2020-09-19T14:40:38.318",  
                        "sampleAccelerationX": 0,  
                        "sampleAccelerationY": 0,  
                        "sampleAccelerationZ": 0  
                    }  
                }  
            }  
        }  
    }  
}  
```  
</details>  
#### TimeSeries Valeurs clés NGSI-LD Exemple  
Voici un exemple d'une série temporelle au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:TimeSeriesData:TimeSeriesData",  
    "type": "TimeSeries",  
    "timeSeries": {  
        "segments":   
        [  
            {  
                "name": "",  
                "description": "",  
                "recordCount": 13134,  
                "startTime": "2020-09-19T14:40:38.318",  
                "endTime": "2020-09-19T14:40:38.318",  
                "duration": "P3DT4H59M",  
                "samplingInterval": 1,  
                "samplingRate": 3200,  
                "state": 0,  
                "lastUpdate": "2020-09-19T14:40:38.318",  
                "externalSegment": {  
                    "data": ""  
                },  
                "linkedSegment": {  
                    "endpoint": "",  
                    "query": ""  
                },  
                "internalSegment": {  
                    "records": [  
                        {  
                            "record00": {  
                                "time": "2020-09-19T14:40:38.318",  
                                "sampleAccelerationX": 0.0,  
                                "sampleAccelerationY": 0.0,  
                                "sampleAccelerationZ": 0.0  
                            }  
                        }  
                    ]  
                }  
            }  
        ],  
        "metadata": {  
            "name": "",  
            "description": "",  
            "record": {  
                "time": "2020-09-19T14:40:38.318",  
                "sampleAccelerationX": 0.0,  
                "sampleAccelerationY": 0.0,  
                "sampleAccelerationZ": 0.0  
            }  
        }  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OPCUA/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### TimeSeries NGSI-LD normalisé Exemple  
Voici un exemple de TimeSeries au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:TimeSeriesData:TimeSeriesData",  
    "type": "TimeSeries",  
    "timeSeries": {  
        "type": "Property",  
        "value": {  
            "segments": [  
                {  
                    "name": "",  
                    "description": "",  
                    "recordCount": 13134,  
                    "startTime": "2020-09-19T14:40:38.318",  
                    "endTime": "2020-09-19T14:40:38.318",  
                    "duration": "P3DT4H59M",  
                    "samplingInterval": 1,  
                    "samplingRate": 3200,  
                    "state": 0,  
                    "lastUpdate": "2020-09-19T14:40:38.318",  
                    "externalSegment": {  
                        "type": "Property",  
                        "value": {  
                            "data": ""  
                        }  
                    },  
                    "linkedSegment": {  
                        "type": "Property",  
                        "value": {  
                            "endpoint": "",  
                            "query": ""  
                        }  
                    },  
                    "internalSegment": {  
                        "type": "Property",  
                        "value": {  
                            "records": [  
                                {  
                                    "type": "Property",  
                                    "value": {  
                                        "record00": {  
                                            "type": "Property",  
                                            "value": {  
                                                "time": "2020-09-19T14:40:38.318",  
                                                "sampleAccelerationX": 0,  
                                                "sampleAccelerationY": 0,  
                                                "sampleAccelerationZ": 0  
                                            }  
                                        }  
                                    }  
                                }  
                            ]  
                        }  
                    }  
                }  
            ],  
            "metadata": {  
                "type": "Property",  
                "value": {  
                    "name": "",  
                    "description": "",  
                    "record": {  
                        "type": "Property",  
                        "value": {  
                            "time": "2020-09-19T14:40:38.318",  
                            "sampleAccelerationX": 0,  
                            "sampleAccelerationY": 0,  
                            "sampleAccelerationZ": 0  
                        }  
                    }  
                }  
            }  
        }  
    },  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.OPCUA/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.OPCUA/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
