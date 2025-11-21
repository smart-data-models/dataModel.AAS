<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：I4子模型元素能力  
============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4SubmodelElementCapability/LICENSE.md)  
[文档自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**基于IDTA-01001-3-0，描述了一个通用的RAMI4.0子模型元素，该元素代表了引用资产管理外壳的能力。**  
版本: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  
属性列表  
<sup><sub>[*] 如果属性中没有类型，则是因为它可能存在多种类型或不同的格式/模式</sub></sup>  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在地的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 该区域，以及该地区位于国家。  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 一个区是某些国家中一种行政分区，在一些国家中由地方政府管理。    
	- `postOfficeBoxNumber[string]`: 邮局地址的邮局箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 特定道路上的特定属性的识别号码    
- `alternateName[string]`: 这个物品的替代名称  - `areaServed[string]`: 服务或提供的商品所覆盖的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: 类别是关于元素类别的进一步元数据相关的信息。  - `dataProvider[string]`: 一个识别 harmonize 数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间。通常由存储平台分配。  - `dateModified[date-time]`: 实体最后修改的时间。通常由存储平台分配。  - `description[string]`: 这个商品的描述  - `descriptions[array]`: 为不同语言中元素更详细的知识阐释  - `hasDataSpecification[array]`: 数据说明模板可以扩展使用，定义元素可能或必须具有的额外属性一组。RAMI4.0 规格说明  - `id[*]`: 唯一标识符  - `idShort[string]`: 短ID是RAMI40环境下的SubmodelElement的（简短）名称。  - `kind[string]`: 为了区分“类型”和“实例”，使用了术语“种类”。  - `location[*]`: 指向该项的 GeoJSON 引用。它可以是点（Point）、线串（LineString）、多边形（Polygon）、多点（MultiPoint）、多线串（MultiLineString）或多多边形（MultiPolygon）。  - `modelType[object]`: 为了区分“类型”和“实例”，使用了“类”这个术语。  	- `name[string]`: 物品的属性。通常，此类物品会设置“-功能-”    
- `name[string]`: 这个物品的名称  - `owner[array]`: 包含JSON编码的字符序列的列表，该字符序列引用了所有者的唯一ID  - `refI4AASId[string]`: 引用此子模型元素所属的根资产管理壳  - `refI4AssetId[string]`: 引用该子模型元素所属的根资产  - `refI4SubmodelId[string]`: 引用此SubmodelElement所属的根Submodel  - `seeAlso[*]`: 指向关于该项目的其他资源的URI列表  - `semanticId[object]`: 它指的是一个外部信息来源，该来源解释了子模型元素的构成。  	- `keys[array]`: 语义ID的键    
- `source[string]`: 一个字符序列，以 URL 的形式给出实体数据的原始来源。建议使用来源提供者的完全限定域名，或指向来源对象的 URL。  - `type[string]`: 需要使用RAMI4.0 I4SubmodelElementCapability NGSI实体类型来表示RAMI4.0 AAS数字孪生子模型能力组件。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排序（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
I4SubmodelElementCapability:    
  description: 'Based on IDTA-01001-3-0, describes a generic RAMI4.0 SubmodelElement representing an Capability of a referenced Asset Administration Shell'    
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
    category:    
      description: The category is a value that gives further meta information w.r.t. to the class of the element    
      type: string    
      x-ngsi:    
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
    descriptions:    
      description: For adding detailed knowledge about the Element in different languages    
      items:    
        description: Every object containing a description    
        properties:    
          language:    
            description: Substring identifying the language. Acronym according to ISO 639-1    
            type: string    
            x-ngsi:    
              type: Property    
          text:    
            description: The Description text is filled here    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    hasDataSpecification:    
      description: Element that can be extended by using data specification templates. A data specification template defines a named set of additional attributes an element may or shall have. RAMI4.0 specification    
      items:    
        description: Object containing the elements of the data specification    
        properties:    
          type:    
            description: 'Link, url or description of the specified data. DataSpecification template conformant to IEC61360'    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
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
    idShort:    
      description: short id is the (short) name of the SubmodelElement within RAMI40 environment    
      type: string    
      x-ngsi:    
        type: Property    
    kind:    
      description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
      type: string    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
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
    modelType:    
      description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
      properties:    
        name:    
          description: Property of the item. Usually -Capability- is set for this type    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
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
    refI4AASId:    
      description: References the root Asset Administration Shell which this SubmodelElement belongs to    
      type: string    
      x-ngsi:    
        type: Relationship    
    refI4AssetId:    
      description: References the root Asset which this SubmodelElement belongs to    
      type: string    
      x-ngsi:    
        type: Relationship    
    refI4SubmodelId:    
      description: References the root Submodel which this SubmodelElement belongs to    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    semanticId:    
      description: 'It refers to an external information source, which explains the formulation of the submodel element'    
      properties:    
        keys:    
          description: Keys for the semantic id    
          items:    
            description: Every object containing the keys for the semantic id    
            properties:    
              idType:    
                description: References the ID of the type    
                type: string    
                x-ngsi:    
                  type: Property    
              index:    
                description: Integer value of the item    
                type: number    
                x-ngsi:    
                  type: Property    
              local:    
                description: Describes a local or not item    
                type: boolean    
                x-ngsi:    
                  type: Property    
              value:    
                description: Describes/includes the corresponding value    
                type: string    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: It has to be RAMI4.0 I4SubmodelElementCapability NGSI Entity type to represent a RAMI4.0 AAS Digital Twin Submodel Capability component    
      enum:    
        - I4SubmodelElementCapability    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2023/04/IDTA-01001-3-0_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AAS/blob/master/I4SubmodelElementCapability/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.AAS/I4SubmodelElementCapability/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
示例payloads  
I4SubmodelElementCapability NGSI-v2 key-values Example  
这是一个I4SubmodelElementCapability在JSON-LD格式中，作为键值对呈现的例子。当使用`options=keyValues`时，它兼容NGSI-v2，并返回一个实体个体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RAMI40:I4SubmodelElementCapability:OperationManagementAgent:PlanOperation",  
  "type": "I4SubmodelElementCapability",  
  "descriptions": [  
      {  
          "language": "en",  
          "text": "Submodel capability [contains various data related to the capability of an intelligent agent]"  
      }  
  ],    
  "hasDataSpecification": [],  
  "idShort": "OperationManagementAgent:PlanOperation",  
  "category": "PARAMETER",  
  "kind": "Instance",  
  "modelType": {  
      "name": "Capability"  
  },  
  "semanticId": {  
      "keys": [  
          {  
              "local": false,  
              "value": "",  
              "index": 0,  
              "idType": ""  
          }  
      ]  
  },    
  "refI4AASId": "urn:ngsi-ld:RAMI40:I4AAS:OperationManagementAgent",  
  "refI4SubmodelId": "urn:ngsi-ld:RAMI40:I4Submodel:OperationManagementAgent:Capabilities"  
}  
```  
</details>  
I4SubmodelElementCapability NGSI-v2 归一化示例  
这是一个I4SubmodelElementCapability在JSON-LD格式中，已标准化。它与NGSI-v2兼容，当不使用选项时，返回单个实体的数据上下文。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RAMI40:I4SubmodelElementCapability:OperationManagementAgent:PlanOperation",  
  "type": "I4SubmodelElementCapability",  
  "descriptions": {  
      "type": "Property",  
      "value": [  
       {  
          "language": "en",  
          "text": "Submodel capability [contains various data related to the capability of an intelligent agent]"  
       }  
    ]  
  },    
  "hasDataSpecification": {  
    "type": "Property",  
    "value": "None"  
  },  
  "idShort": {  
    "type": "Property",  
    "value": "I4SubmodelElementCapability:OperationManagementAgent:PlanOperation"  
  },    
  "category": {  
    "type": "Property",  
    "value": "PARAMETER"  
  },  
  "kind": {  
    "type": "Property",  
    "value": "Instance"  
  },  
  "modelType": {  
    "type": "Property",  
    "value": {  
      "name": "Capability"  
    }  
  },  
  "semanticId": {  
    "type": "Property",  
    "value": {  
      "keys": []  
    }  
  },  
  "refI4AASId": {  
    "type": "Property",  
    "value": "urn:ngsi-ld:RAMI40:I4AAS:OperationManagementAgent"  
  },  
  "refI4SubmodelId":   
  {  
    "type": "Property",  
    "value": "urn:ngsi-ld:RAMI40:I4Submodel:OperationManagementAgent:Capabilities"  
  }  
}  
```  
</details>  
I4SubmodelElementCapability NGSI-LD key-values Example  
这是一个I4SubmodelElementCapability在JSON-LD格式中，作为键值对呈现的例子。当使用`options=keyValues`时，它兼容NGSI-LD，并返回一个实体个体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RAMI40:I4SubmodelElementCapability:OperationManagementAgent:PlanOperation",  
  "type": "I4SubmodelElementCapability",  
  "descriptions": [  
      {  
          "language": "en",  
          "text": "Submodel capability [contains various data related to the capability of an intelligent agent]"  
      }  
  ],    
  "hasDataSpecification": [],  
  "idShort": "I4SubmodelElementCapability:OperationManagementAgent:PlanOperation",  
  "category": "PARAMETER",  
  "kind": "Instance",  
  "modelType": {  
      "name": "Capability"  
  },  
  "semanticId": {  
      "keys": [  
          {  
              "local": false,  
              "value": "",  
              "index": 0,  
              "idType": ""  
          }  
      ]  
  },    
  "refI4AASId": "urn:ngsi-ld:RAMI40:I4AAS:OperationManagementAgent",  
  "refI4SubmodelId": "urn:ngsi-ld:RAMI40:I4Submodel:OperationManagementAgent:Capabilities",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]    
}  
```  
</details>  
I4SubmodelElementCapability NGSI-LD 归一化示例  
这是一个I4SubmodelElementCapability在JSON-LD格式中，已标准化。它与NGSI-LD兼容，当不使用选项时，返回单个实体的数据上下文。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RAMI40:I4SubmodelElementCapability:OperationManagementAgent:PlanOperation",  
  "type": "I4SubmodelElementCapability",  
  "descriptions": {  
      "type": "Property",  
      "value": [  
       {  
          "language": "en",  
          "text": "Submodel capability [contains various data related to the capability of an intelligent agent]"  
       }  
    ]  
  },    
  "hasDataSpecification": {  
    "type": "Property",  
    "value": "None"  
  },  
  "idShort": {  
    "type": "Property",  
    "value": "I4SubmodelElementCapability:OperationManagementAgent:PlanOperation"  
  },    
  "category": {  
    "type": "Property",  
    "value": "PARAMETER"  
  },  
  "kind": {  
    "type": "Property",  
    "value": "Instance"  
  },  
  "modelType": {  
    "type": "Property",  
    "value": {  
      "name": "Capability"  
    }  
  },  
  "semanticId": {  
    "type": "Property",  
    "value": {  
      "keys": []  
    }  
  },  
  "refI4AASId": {  
    "type": "Property",  
    "value": "urn:ngsi-ld:RAMI40:I4AAS:OperationManagementAgent"  
  },  
  "refI4SubmodelId":   
  {  
    "type": "Property",  
    "value": "urn:ngsi-ld:RAMI40:I4Submodel:OperationManagementAgent:Capabilities"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]    
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
查看[FAQ 10](https://smartdatamodels.org/index.php/faqs/) 获取处理数值单位的解答。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
