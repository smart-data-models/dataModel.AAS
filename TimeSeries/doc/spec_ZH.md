<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体时间序列  
======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.AAS/blob/master/TimeSeries/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**时间序列可以表示原始数据，也可以简明扼要地表示主要特征、文字描述或事件。  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 标识公共街道上特定房产的编号    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一标识  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `timeSeries[object]`: 时间序列模型的主要对象  	- `metadata[object]`: 描述和提供时间序列信息的一组数据    
	- `segments[array]`: 时间序列片段列表    
- `type[string]`: NGSI 类型。必须是时间序列  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `timeSeries`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
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
## 有效载荷示例  
#### 时间序列 NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的时间序列示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### 时间序列 NGSI-v2 归一化示例  
下面是一个规范化 JSON-LD 格式的时间序列示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### 时间序列 NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的时间序列示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
#### 时间序列 NGSI-LD 归一化示例  
下面是一个以 JSON-LD 格式规范化的时间序列示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
