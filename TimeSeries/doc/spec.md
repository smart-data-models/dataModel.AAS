<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: TimeSeries  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.AAS/blob/master/TimeSeries/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Time Series can represent raw data, but can also represent main characteristics, textual descriptions or events in a concise way.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Number identifying a specific property on a public street    
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `timeSeries[object]`: Main object for TimeSeries model  	- `metadata[object]`:  A set of data describing and providing information about the time series    
	- `segments[array]`: List of time series segments    
- `type[string]`: NGSI type. It has to be TimeSeries  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `timeSeries`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
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
## Example payloads    
#### TimeSeries NGSI-v2 key-values Example    
Here is an example of a TimeSeries in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### TimeSeries NGSI-v2 normalized Example    
Here is an example of a TimeSeries in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### TimeSeries NGSI-LD key-values Example    
Here is an example of a TimeSeries in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### TimeSeries NGSI-LD normalized Example    
Here is an example of a TimeSeries in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
