<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Serie temporali  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.AAS/blob/master/TimeSeries/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Le serie temporali possono rappresentare dati grezzi, ma anche caratteristiche principali, descrizioni testuali o eventi in modo conciso.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzati  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `timeSeries[object]`: Oggetto principale per il modello TimeSeries  	- `metadata[object]`:  Un insieme di dati che descrivono e forniscono informazioni sulle serie temporali.    
	- `segments[array]`: Elenco dei segmenti delle serie temporali    
- `type[string]`: Tipo NGSI. Deve essere TimeSeries  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `timeSeries`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempi di payload  
#### TimeSeries NGSI-v2 valori-chiave Esempio  
Ecco un esempio di TimeSeries in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Serie temporale NGSI-v2 normalizzata Esempio  
Ecco un esempio di TimeSeries in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
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
#### Serie temporale NGSI-LD valori chiave Esempio  
Ecco un esempio di TimeSeries in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Serie temporale NGSI-LD normalizzata Esempio  
Ecco un esempio di TimeSeries in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
