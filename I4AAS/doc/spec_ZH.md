<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：I4AAS  
========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4AAS/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
总体说明：**基于 IDTA-01001-3-0，描述了 RAMI4.0 的组件--通用资产管理外壳（AAS）树。  
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
- `administration[object]`: AAS 管理信息  	- `revision[string]`: AAS 修订编号是与规范发布一致的编号    
	- `version[string]`: AAS 版本号是与规范版本一致的编号    
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `asset[object]`: 此处填写资产描述  	- `keys[array]`: 资产钥匙    
- `category[string]`: 类别是一个值，可提供有关元素类别的更多元信息  - `conceptDictionaries[array]`: 资产本身也可以定义自己的字典，其中包含子模型元素的语义定义。这些语义定义称为概念描述（ConceptDescription 或概念字典）。此数组将包含在此模型中使用的 RAMI4.0 特定概念的参考 ID  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `descriptions[array]`: 用不同语言详细介绍美国科学院的情况  - `hasDataSpecification[array]`: 数据规范定义了资产可能具有的附加属性。RAMI4.0 规范  - `id[*]`: 实体的唯一标识符  - `idShort[string]`: short id 是资产管理外壳的（简短）名称  - `identification[object]`: 确定资产的 AAS。RAMI4.0 环境  	- `id[uri]`: 可明确区分一个 AAS 和另一个 AAS 的身份信息。RAMI4.0 环境    
	- `idType[string]`: 标识符类型，例如 IRI 或 IRDI    
- `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `modelType[object]`: 为了区分 "类型 "和 "实例"，使用了 "种类 "一词  	- `name[string]`: 项目引用属性的描述    
- `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `refI4AssetId[uri]`: 引用链接到该 AAS 的根资产  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `submodels[array]`: AAS 包含一组复杂的信息，子模式为这些复杂的数据提供了一个单独的类别  - `type[string]`: 它必须是 RAMI4.0 I4AAS NGSI 实体类型，以表示 RAMI4.0 AAS 数字双胞胎  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
I4AAS:    
  description: 'Based on IDTA-01001-3-0, describes a generic Asset Administration Shell - AAS - tree, component of the RAMI4.0'    
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
    administration:    
      description: AAS administration information    
      properties:    
        revision:    
          description: AAS Revision number is the number in line with release of specification    
          type: string    
          x-ngsi:    
            type: Property    
        version:    
          description: AAS Version number is the number in line with release of specification    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - version    
        - revision    
      type: object    
      x-ngsi:    
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
    asset:    
      description: The Asset descripton is filled here    
      properties:    
        keys:    
          description: Keys for the Asset    
          items:    
            - properties:    
                idType:    
                  description: 'Property. Type of the Identifier, eg.IRI or IRDI'    
                  type: string    
                index:    
                  description: Property. Index encodes the position in the original sequence    
                  type: integer    
                local:    
                  description: Property. It defines whether the asset is created locally or globally    
                  type: boolean    
                type:    
                  description: Property. Type (description) of the asset    
                  enum:    
                    - Asset    
                  type: string    
                value:    
                  description: Property. Here comes the id pointing to the definition of asset    
                  type: string    
              required:    
                - type    
                - local    
                - value    
                - index    
                - idType    
              type: object    
          type: array    
          x-ngsi:    
            type: Property    
      required:    
        - keys    
      type: object    
      x-ngsi:    
        type: Property    
    category:    
      description: The category is a value that gives further meta information w.r.t. to the class of the element    
      type: string    
      x-ngsi:    
        type: Property    
    conceptDictionaries:    
      description: The Asset itself can also define its own dictionary that contains semantic definitions of its submodel elements. These semantic definitions are called concept descriptions (ConceptDescription or concept dictionary). This array will contain ref ids to RAMI4.0 specific concepts used within this model    
      items:    
        properties:    
          type:    
            description: 'Link, url, reference or description of the specified I4.0 concept'    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
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
      description: For adding detailed knowldedge about the AAS in different languages    
      items:    
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
        required:    
          - language    
          - text    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    hasDataSpecification:    
      description: Data specification defines the additional attributes an asset may have. RAMI4.0 specification    
      items:    
        properties:    
          type:    
            description: 'Link, url or descriptionof the specified data'    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
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
        type: Property    
    idShort:    
      description: short id is the (short) name of the ASSET ADMINISTRATION SHELL    
      type: string    
      x-ngsi:    
        type: Property    
    identification:    
      description: Identification of the AAS for the asset. RAMI4.0 environment    
      properties:    
        id:    
          description: 'Identity information that unambiguously distinguishes one AAS from another one. RAMI4.0 environmet '    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        idType:    
          description: 'Type of the Identifier, eg.IRI or IRDI'    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - idType    
        - id    
      type: object    
      x-ngsi:    
        type: Property    
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
    modelType:    
      description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
      properties:    
        name:    
          description: Description of the referenced property of the item    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - name    
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
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    refI4AssetId:    
      description: References the root Asset linked to this AAS    
      format: uri    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    submodels:    
      description: 'AAS contains complex set of informations, submodels provide a separate category for this complex data'    
      items:    
        description: It clearly identify the attribute of data    
        properties:    
          keys:    
            description: keys for the submodel    
            items:    
              properties:    
                idType:    
                  description: Identity information that unambiguously distinguishes one submodel from another one. Can be IRI or IRDI    
                  type: string    
                  x-ngsi:    
                    type: Property    
                index:    
                  description: Index encodes the position in the original sequence    
                  type: number    
                  x-ngsi:    
                    type: Property    
                local:    
                  description: It defines whether the submodel is created locally or globally    
                  type: boolean    
                  x-ngsi:    
                    type: Property    
                type:    
                  description: Type (description) of the submodel    
                  enum:    
                    - Submodel    
                  type: string    
                  x-ngsi:    
                    type: Property    
                value:    
                  description: The id of the submodel pointing to the definition of the Submodel    
                  type: string    
                  x-ngsi:    
                    type: Property    
              required:    
                - type    
                - local    
                - value    
                - index    
                - idType    
              type: object    
            type: array    
            x-ngsi:    
              type: Property    
        required:    
          - keys    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: It has to be RAMI4.0 I4AAS NGSI Entity type to represent a RAMI4.0 AAS Digital Twin    
      enum:    
        - I4AAS    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2023/04/IDTA-01001-3-0_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AAS/blob/master/I4AAS/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.AAS/I4AAS/schema.json    
  x-model-tags: Corosect    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### I4AAS NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 I4AAS 示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
  "type": "I4AAS",  
  "administration": {  
    "version": "1.0",  
    "revision": "1.0"  
  },  
  "asset": {  
    "keys": [  
      {  
        "type": "Asset",  
        "local": true,  
        "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
        "index": 0,  
        "idType": "IRI"  
      }  
    ]  
  },  
  "category": "CONSTANT",  
  "conceptDictionaries": [],  
  "descriptions": [  
    {  
      "language": "en",  
      "text": "AAS of AASMRobotVI"  
    }  
  ],  
  "hasDataSpecification": [],  
  "idShort": "AASMRobotVI",  
  "identification": {  
    "idType": "IRI",  
    "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI"  
  },  
  "modelType": {  
    "name": "AssetAdministrationShell"  
  },  
  "refI4AssetId": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
  "submodels": [  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:AssetConditionMonitoring:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:Nameplate:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalData:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    }  
  ]  
}  
```  
</details>  
#### I4AAS NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 I4AAS 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
  "type": "I4AAS",  
  "administration": {  
    "type": "StructuredValue",  
    "value": {  
      "version": "1.0",  
      "revision": "1.0"  
    }  
  },  
  "asset": {  
    "type": "StructuredValue",  
    "value": {  
      "keys": [  
        {  
          "type": "Asset",  
          "local": true,  
          "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    }  
  },  
  "category": {  
    "type": "Text",  
    "value": "CONSTANT"  
  },  
  "conceptDictionaries": {  
    "type": "array",  
    "value": []  
  },  
  "descriptions": {  
    "type": "array",  
    "value": [  
      {  
        "language": "en",  
        "text": "AAS of AASMRobotVI"  
      }  
    ]  
  },  
  "hasDataSpecification": {  
    "type": "array",  
    "value": []  
  },  
  "idShort": {  
    "type": "Text",  
    "value": "AASMRobotVI"  
  },  
  "identification": {  
    "type": "StructuredValue",  
    "value": {  
      "idType": "IRI",  
      "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI"  
    }  
  },  
  "modelType": {  
    "type": "StructuredValue",  
    "value": {  
      "name": "AssetAdministrationShell"  
    }  
  },  
  "refI4AssetId": {  
    "type": "Text",  
    "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI"  
  },  
  "submodels": {  
    "type": "array",  
    "value": [  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:AssetConditionMonitoring:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:Nameplate:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalData:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      }  
    ]  
  }  
}  
```  
</details>  
#### I4AAS NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的 I4AAS 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
  "type": "I4AAS",  
  "administration": {  
    "version": "1.0",  
    "revision": "1.0"  
  },  
  "asset": {  
    "keys": [  
      {  
        "type": "Asset",  
        "local": true,  
        "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
        "index": 0,  
        "idType": "IRI"  
      }  
    ]  
  },  
  "category": "CONSTANT",  
  "conceptDictionaries": [],  
  "descriptions": [  
    {  
      "language": "en",  
      "text": "AAS of AASMRobotVI"  
    }  
  ],  
  "hasDataSpecification": [],  
  "idShort": "AASMRobotVI",  
  "identification": {  
    "idType": "IRI",  
    "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI"  
  },  
  "modelType": {  
    "name": "AssetAdministrationShell"  
  },  
  "refI4AssetId": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
  "submodels": [  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:AssetConditionMonitoring:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:Nameplate:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalData:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    }  
  ],  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.AAS/context.jsonld"  
  ]  
}  
```  
</details>  
#### I4AAS NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式的 I4AAS 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
  "type": "I4AAS",  
  "administration": {  
    "type": "Property",  
    "value": {  
      "version": "1.0",  
      "revision": "1.0"  
    }  
  },  
  "asset": {  
    "type": "Property",  
    "value": {  
      "keys": [  
        {  
          "type": "Asset",  
          "local": true,  
          "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    }  
  },  
  "category": {  
    "type": "Property",  
    "value": "CONSTANT"  
  },  
  "conceptDictionaries": {  
    "type": "Property",  
    "value": []  
  },  
  "descriptions": {  
    "type": "Property",  
    "value": [  
      {  
        "language": "en",  
        "text": "AAS of AASMRobotVI"  
      }  
    ]  
  },  
  "hasDataSpecification": {  
    "type": "Property",  
    "value": []  
  },  
  "idShort": {  
    "type": "Property",  
    "value": "AASMRobotVI"  
  },  
  "identification": {  
    "type": "Property",  
    "value": {  
      "idType": "IRI",  
      "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI"  
    }  
  },  
  "modelType": {  
    "type": "Property",  
    "value": {  
      "name": "AssetAdministrationShell"  
    }  
  },  
  "refI4AssetId": {  
    "type": "Property",  
    "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI"  
  },  
  "submodels": {  
    "type": "Property",  
    "value": [  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:AssetConditionMonitoring:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:Nameplate:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalData:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      }  
    ]  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.AAS/context.jsonld"  
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
