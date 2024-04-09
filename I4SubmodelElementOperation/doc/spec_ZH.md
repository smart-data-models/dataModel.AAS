<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：I4SubmodelElementOperation（I4 子模型元素操作  
========================================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4SubmodelElementOperation/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**基于 IDTA-01001-3-0，描述一个通用的 RAMI4.0 子模型元素，代表一个引用资产管理外壳的操作（命令）**。  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: 类别是一个值，可提供有关元素类别的更多元信息  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `descriptions[array]`: 为不同语言的元素添加详细信息  - `executionState[string]`: 操作调用结果状态  - `hasDataSpecification[array]`: 可通过使用数据规范模板进行扩展的元素。数据规范模板定义了一个元素可能或应具有的一组命名的附加属性。RAMI4.0 规范  - `id[*]`: 实体的唯一标识符  - `idShort[string]`: 短 id 是 RAMI40 环境中子模型元素的（短）名称  - `inoutputVariable[array]`: 包含操作输入和输出参数的数组  - `inputVariable[array]`: 包含操作输入参数的数组  - `kind[string]`: 为了区分 "类型 "和 "实例"，使用了 "种类 "一词  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `modelType[object]`: 为了区分 "类型 "和 "实例"，使用了 "种类 "一词  	- `name[string]`: 项目的属性。通常为该类型设置 -Operation    
- `name[string]`: 该项目的名称  - `operationResult[object]`: 包含操作调用返回结果的操作调用结果对象  	- `entity[object]`: 与操作结果相关联的属性集    
	- `entityType[string]`: 实体类型说明/参考    
	- `isException[boolean]`: 如果是异常则为 True    
	- `messages[array]`: 包含申请者信息的附加信息    
	- `success[boolean]`: 如果操作成功，则为 true。否则为假    
- `outputVariable[array]`: 包含操作输出参数的数组  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `refI4AASId[string]`: 引用该子模型元素所属的根资产管理壳  - `refI4AssetId[string]`: 引用该子模型元素所属的根资产  - `refI4SubmodelId[string]`: 引用该子模型元素所属的根子模型  - `requestId[string]`: 针对 INPUT 发送的客户端请求 ID 和/或针对 OUTPUT 获取的值/状态。用于跟踪操作  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `semanticId[object]`: 它指的是一个外部信息源，该信息源解释了子模型元素的构成  	- `keys[array]`: 语义 ID 的键    
- `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `timeout[number]`: 代表 OPC-UA 服务器报告的该命令的超时值  - `type[string]`: 它必须是 RAMI4.0 I4SubmodelElementOperation NGSI 实体类型，以表示 RAMI4.0 AAS 数字孪生子模型操作组件  <!-- /30-PropertiesList -->  
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
I4SubmodelElementOperation:    
  description: 'Based on IDTA-01001-3-0, describes a generic RAMI4.0 SubmodelElement representing an OPERATION (Command) of a referenced Asset Administration Shell'    
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
    executionState:    
      description: The operation invocation result state    
      enum:    
        - canceled    
        - completed    
        - failed    
        - initiated    
        - running    
        - timeout    
      type: string    
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
        type: Property    
    idShort:    
      description: short id is the (short) name of the SubmodelElement within RAMI40 environment    
      type: string    
      x-ngsi:    
        type: Property    
    inoutputVariable:    
      description: Array with parameters that are input and output of the operation    
      items:    
        description: Defines an inoutput variable for this command request    
        properties:    
          category:    
            description: The category is a value that gives further meta information w.r.t. to the class of the element    
            type: string    
            x-ngsi:    
              type: Property    
          constraints:    
            description: Constraints an inoutput Variable may have. RAMI4.0 Asset Administration Shell specification. Version 3.0RC02    
            items:    
              description: 'Every object containing the constraints '    
              properties:    
                type:    
                  description: 'Link, url, constraint ID (AAS Version 3.0RC02) or description of the constrain to be applied'    
                  type: string    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
            type: array    
            x-ngsi:    
              type: Property    
          descriptions:    
            description: For adding detailed knowledge about the Element in different languages    
            items:    
              description: Every object containing the attributes of the descriptions    
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
              description: Every object containing the descriptions of the data specification    
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
          idShort:    
            description: short id is the (short) name of the inoutput Value -variable name- within RAMI40 environment    
            type: string    
            x-ngsi:    
              type: Property    
          kind:    
            description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
            type: string    
            x-ngsi:    
              type: Property    
          modelType:    
            description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
            properties:    
              name:    
                description: Property of the item    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          value:    
            description: The obtained value in string format    
            type: string    
            x-ngsi:    
              type: Property    
          valueType:    
            description: The value type used in string format    
            properties:    
              dataObjectType:    
                description: 'Property of the item. string, integer, float, num etc. are used set for this type'    
                properties:    
                  name:    
                    description: Property of the item. Object type    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    inputVariable:    
      description: Array with input parameters of the operation    
      items:    
        description: Defines an Input variable for this command request    
        properties:    
          category:    
            description: The category is a value that gives further meta information w.r.t. to the class of the element    
            type: string    
            x-ngsi:    
              type: Property    
          constraints:    
            description: Constraints an Input Variable may have. RAMI4.0 Asset Administration Shell specification. Version 3.0RC02    
            items:    
              description: The object containing the constraints    
              properties:    
                type:    
                  description: 'Link, url, constraint ID (AAS Version 3.0RC02) or description of the constrain to be applied'    
                  type: string    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
            type: array    
            x-ngsi:    
              type: Property    
          descriptions:    
            description: For adding detailed knowledge about the Element in different languages    
            items:    
              description: Every object containing the descriptions properties    
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
              description: Every object containing the attributes of the data specification    
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
          idShort:    
            description: short id is the (short) name of the Input Value -variable name- within RAMI40 environment    
            type: string    
            x-ngsi:    
              type: Property    
          kind:    
            description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
            type: string    
            x-ngsi:    
              type: Property    
          modelType:    
            description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
            properties:    
              name:    
                description: Property of the item. Usually -OperationVariable- is set for this type    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          value:    
            description: The given value in string format    
            type: string    
            x-ngsi:    
              type: Property    
          valueType:    
            description: The value type used in string format    
            properties:    
              dataObjectType:    
                description: 'Property of the item. string, integer, float, num etc. are used set for this type'    
                properties:    
                  name:    
                    description: Property of the item. Object type    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
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
          description: Property of the item. Usually -Operation- is set for this type    
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
    operationResult:    
      description: Contains The operation invocation result object with the returned result of an operation invocation    
      properties:    
        entity:    
          description: Set of properties linked to the operation results    
          type: object    
          x-ngsi:    
            type: Property    
        entityType:    
          description: Entity type description/reference    
          type: string    
          x-ngsi:    
            type: Property    
        isException:    
          description: True if it is an exception    
          type: boolean    
          x-ngsi:    
            type: Property    
        messages:    
          description: Additional message containing information for the requester    
          items:    
            description: Item object for the messages    
            properties:    
              code:    
                description: Technology-dependent status or error code    
                type: string    
                x-ngsi:    
                  type: Property    
              messageType:    
                description: The message type enum    
                enum:    
                  - error    
                  - exception    
                  - info    
                  - warning    
                type: string    
                x-ngsi:    
                  type: Property    
              text:    
                description: A message containing more information for the requester about a certain happening in the backend    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          type: array    
          x-ngsi:    
            type: Property    
        success:    
          description: Success true if operation succeed. False if not    
          type: boolean    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    outputVariable:    
      description: Array with Output parameters of the operation    
      items:    
        description: Defines an Output variable for this command request    
        properties:    
          category:    
            description: The category is a value that gives further meta information w.r.t. to the class of the element    
            type: string    
            x-ngsi:    
              type: Property    
          constraints:    
            description: Constraints an Output Variable may have. RAMI4.0 Asset Administration Shell specification. Version 3.0RC02    
            items:    
              description: Every object containing the description of the constraints    
              properties:    
                type:    
                  description: 'Link, url, constraint ID (AAS Version 3.0RC02) or description of the constrain to be applied'    
                  type: string    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
            type: array    
            x-ngsi:    
              type: Property    
          descriptions:    
            description: For adding detailed knowledge about the Element in different languages    
            items:    
              description: Every object containing the attributes of the descriptions    
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
              description: Every object containing the details of the data specification    
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
          idShort:    
            description: short id is the (short) name of the Output Value -variable name- within RAMI40 environment    
            type: string    
            x-ngsi:    
              type: Property    
          kind:    
            description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
            type: string    
            x-ngsi:    
              type: Property    
          modelType:    
            description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
            properties:    
              name:    
                description: Property of the item. Usually -OperationVariable- is set for this type    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          value:    
            description: The obtained value in string format    
            type: string    
            x-ngsi:    
              type: Property    
          valueType:    
            description: The value type used in string format    
            properties:    
              dataObjectType:    
                description: 'Property of the item. string, integer, float, num etc. are used set for this type'    
                properties:    
                  name:    
                    description: Property of the item. Object type    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
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
    requestId:    
      description: Client request ID sent -for INPUT- and/or the retrieved value/status -for OUTPUT-. Used to TRACK the operations    
      type: string    
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
    timeout:    
      description: Represents the timeout value for this command reported by the OPC-UA server    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: It has to be RAMI4.0 I4SubmodelElementOperation NGSI Entity type to represent a RAMI4.0 AAS Digital Twin Submodel Operation component    
      enum:    
        - I4SubmodelElementOperation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2023/04/IDTA-01001-3-0_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AAS/blob/master/I4SubmodelElementOperation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.AAS/I4SubmodelElementOperation/schema.json    
  x-model-tags: Corosect    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### I4SubmodelElementOperation NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 I4SubmodelElementOperation 的示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4SubmodelElementOperation:OperationalCapability:MRobotExecuteTask:AASMRobotVI",  
  "type": "I4SubmodelElementOperation",  
  "category": "PARAMETER",  
  "descriptions": [  
    {  
      "language": "en",  
      "text": "Submodel operational capability [contains various data related to the operation capability of sensor]"  
    }  
  ],  
  "executionState": "initiated",  
  "hasDataSpecification": [],  
  "idShort": "MRobotExecuteTask",  
  "inoutputVariable": [],  
  "inputVariable": [  
    {  
      "value": "review",  
      "constraints": [],  
      "hasDataSpecification": [],  
      "idShort": "TaskID",  
      "category": "CONSTANT",  
      "valueType": {  
        "dataObjectType": {  
          "name": "arg.DataType"  
        }  
      },  
      "kind": "Instance",  
      "descriptions": [  
        {  
          "language": "en",  
          "text": "To give the task id to be executed"  
        }  
      ],  
      "modelType": {  
        "name": "OperationVariable"  
      }  
    }  
  ],  
  "kind": "Instance",  
  "modelType": {  
    "name": "Operation"  
  },  
  "operationResult": {  
    "success": true,  
    "isException": false,  
    "entity": {},  
    "entityType": "string",  
    "messages": [  
      {  
        "messageType": "info",  
        "text": "no message text",  
        "code": "no code"  
      }  
    ]  
  },  
  "outputVariable": [  
    {  
      "value": "review",  
      "constraints": [],  
      "hasDataSpecification": [],  
      "idShort": "CommandStatus",  
      "category": "CONSTANT",  
      "valueType": {  
        "dataObjectType": {  
          "name": "arg.DataType"  
        }  
      },  
      "kind": "Instance",  
      "descriptions": [  
        {  
          "language": "en",  
          "text": "To let the the service consumer know that the command has been received and will be processed"  
        }  
      ],  
      "modelType": {  
        "name": "OperationVariable"  
      }  
    }  
  ],  
  "refI4AASId": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
  "refI4AssetId": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
  "refI4SubmodelId": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AASMRobotVI",  
  "requestId": "review",  
  "semanticId": {  
    "keys": [  
      {  
        "type": "Submodel",  
        "local": false,  
        "value": "",  
        "index": 0,  
        "idType": ""  
      }  
    ]  
  },  
  "timeout": 0  
}  
```  
</details>  
#### I4SubmodelElementOperation NGSI-v2 标准化示例  
下面是一个以 JSON-LD 格式规范化的 I4SubmodelElementOperation 的示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-v2:RAMI40:I4SubmodelElementOperation:OperationalCapability:drop:AGV1",  
    "type": "I4SubmodelElementOperation",  
    "category": {  
        "type": "Text",  
        "value": "CONSTANT",  
        "metadata": {}  
    },  
    "descriptions": {  
        "type": "StructuredValue",  
        "value": [  
            {  
                "language": "en",  
                "text": "Request the AGV to drop a load"  
            }  
        ],  
        "metadata": {}  
    },  
    "hasDataSpecification": {  
        "type": "StructuredValue",  
        "value": "None",  
        "metadata": {}  
    },  
    "idShort": {  
        "type": "Text",  
        "value": "drop",  
        "metadata": {}  
    },  
    "inoutputVariable": {  
        "type": "StructuredValue",  
        "value": [],  
        "metadata": {}  
    },  
    "inputVariable": {  
        "type": "StructuredValue",  
        "value": [  
            {  
                "value": "EURO",  
                "idShort": "loadType"  
            },  
            {  
                "value": "1",  
                "idShort": "loadId"  
            },  
            {  
                "value": "0",  
                "idShort": "height"  
            },  
            {  
                "value": "0",  
                "idShort": "depth"  
            },  
            {  
                "value": "0",  
                "idShort": "side"  
            }  
        ],  
        "metadata": {}  
    },  
    "kind": {  
        "type": "Text",  
        "value": "Instance",  
        "metadata": {}  
    },  
    "modelType": {  
        "type": "StructuredValue",  
        "value": {  
            "name": "Operation"  
        },  
        "metadata": {}  
    },  
    "operationResult": {  
        "type": "StructuredValue",  
        "value": {},  
        "metadata": {}  
    },  
    "outputVariable": {  
        "type": "StructuredValue",  
        "value": [  
            {  
                "value": "",  
                "idShort": "CommandStatus"  
            }  
        ],  
        "metadata": {}  
    },  
    "refI4AASId": {  
        "type": "Text",  
        "value": "urn:ngsi-v2:RAMI40:I4AAS:AGV:AGV1",  
        "metadata": {}  
    },  
    "refI4AssetId": {  
        "type": "Text",  
        "value": "urn:ngsi-v2:RAMI40:I4Asset:AGV:AGV1",  
        "metadata": {}  
    },  
    "refI4SubmodelId": {  
        "type": "Text",  
        "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AGV1",  
        "metadata": {}  
    },  
    "requestId": {  
        "type": "Text",  
        "value": "3b85ce8a-e8dd-4918-b327-c049e7b3d127",  
        "metadata": {}  
    },  
    "semanticId": {  
        "type": "StructuredValue",  
        "value": {  
            "keys": []  
        },  
        "metadata": {}  
    },  
    "timeout": {  
        "type": "Number",  
        "value": 0,  
        "metadata": {}  
    },  
    "valueId": {  
        "type": "Text",  
        "value": "unused",  
        "metadata": {}  
    }  
}  
```  
</details>  
#### I4SubmodelElementOperation NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的 I4SubmodelElementOperation 的示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4SubmodelElementOperation:OperationalCapability:MRobotExecuteTask:AASMRobotVI",  
  "type": "I4SubmodelElementOperation",  
  "category": "PARAMETER",  
  "descriptions": [  
    {  
      "language": "en",  
      "text": "Submodel operational capability [contains various data related to the operation capability of sensor]"  
    }  
  ],  
  "executionState": "initiated",  
  "hasDataSpecification": [],  
  "idShort": "MRobotExecuteTask",  
  "inoutputVariable": [],  
  "inputVariable": [  
    {  
      "value": "review",  
      "hasDataSpecification": [],  
      "idShort": "TaskID",  
      "category": "CONSTANT",  
      "valueType": {  
        "dataObjectType": {  
          "name": "arg.DataType"  
        }  
      },  
      "kind": "Instance",  
      "descriptions": [  
        {  
          "language": "en",  
          "text": "To give the task id to be executed"  
        }  
      ],  
      "modelType": {  
        "name": "OperationVariable"  
      }  
    }  
  ],  
  "kind": "Instance",  
  "modelType": {  
    "name": "Operation"  
  },  
  "operationResult": {  
    "success": true,  
    "isException": false,  
    "entity": {},  
    "entityType": "string",  
    "messages": [  
      {  
        "messageType": "info",  
        "text": "no message text",  
        "code": "no code"  
      }  
    ]  
  },  
  "outputVariable": [  
    {  
      "value": "review",  
      "hasDataSpecification": [],  
      "idShort": "CommandStatus",  
      "category": "CONSTANT",  
      "valueType": {  
        "dataObjectType": {  
          "name": "arg.DataType"  
        }  
      },  
      "kind": "Instance",  
      "descriptions": [  
        {  
          "language": "en",  
          "text": "To let the the service consumer know that the command has been received and will be processed"  
        }  
      ],  
      "modelType": {  
        "name": "OperationVariable"  
      }  
    }  
  ],  
  "refI4AASId": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
  "refI4AssetId": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
  "refI4SubmodelId": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AASMRobotVI",  
  "requestId": "review",  
  "semanticId": {  
    "keys": [  
      {  
        "type": "Submodel",  
        "local": false,  
        "value": "",  
        "index": 0,  
        "idType": ""  
      }  
    ]  
  },  
  "timeout": 0,  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.AAS/context.jsonld"  
  ]  
}  
```  
</details>  
#### I4SubmodelElementOperation NGSI-LD 标准化示例  
下面是一个 I4SubmodelElementOperation 的示例，格式为规范化的 JSON-LD。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4SubmodelElementOperation:OperationalCapability:drop:AGV1",  
  "type": "I4SubmodelElementOperation",  
  "category": {  
    "type": "Property",  
    "value": "CONSTANT"  
  },  
  "descriptions": {  
    "type": "Property",  
    "value": [  
      {  
        "language": "en",  
        "text": "Request the AGV to drop a load"  
      }  
    ]  
  },  
  "hasDataSpecification": {  
    "type": "Property",  
    "value": "None"  
  },  
  "idShort": {  
    "type": "Property",  
    "value": "drop"  
  },  
  "inoutputVariable": {  
    "type": "Property",  
    "value": []  
  },  
  "inputVariable": {  
    "type": "Property",  
    "value": [  
      {  
        "value": "EURO",  
        "idShort": "loadType"  
      },  
      {  
        "value": "1",  
        "idShort": "loadId"  
      },  
      {  
        "value": "0",  
        "idShort": "height"  
      },  
      {  
        "value": "0",  
        "idShort": "depth"  
      },  
      {  
        "value": "0",  
        "idShort": "side"  
      }  
    ]  
  },  
  "kind": {  
    "type": "Property",  
    "value": "Instance"  
  },  
  "modelType": {  
    "type": "Property",  
    "value": {  
      "name": "Operation"  
    }  
  },  
  "operationResult": {  
    "type": "Property",  
    "value": {}  
  },  
  "outputVariable": {  
    "type": "Property",  
    "value": [  
      {  
        "value": "",  
        "idShort": "CommandStatus"  
      }  
    ]  
  },  
  "refI4AASId": {  
    "type": "Property",  
    "value": "urn:ngsi-v2:RAMI40:I4AAS:AGV:AGV1"  
  },  
  "refI4AssetId": {  
    "type": "Property",  
    "value": "urn:ngsi-v2:RAMI40:I4Asset:AGV:AGV1"  
  },  
  "refI4SubmodelId": {  
    "type": "Property",  
    "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AGV1"  
  },  
  "requestId": {  
    "type": "Property",  
    "value": "3b85ce8a-e8dd-4918-b327-c049e7b3d127"  
  },  
  "semanticId": {  
    "type": "Property",  
    "value": {  
      "keys": []  
    }  
  },  
  "timeout": {  
    "type": "Property",  
    "value": 0  
  },  
  "valueId": {  
    "type": "Property",  
    "value": "unused"  
  }  
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
