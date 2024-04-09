<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: I4SubmodelElementOperation  
===============================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4SubmodelElementOperation/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **IDTA-01001-3-0에 기반하여 참조된 자산 관리 셸**의 운영(명령)을 나타내는 일반 RAMI4.0 하위 모델 요소를 설명합니다.  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역 내 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: 카테고리는 요소의 클래스에 대한 추가 메타 정보를 제공하는 값입니다.  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `descriptions[array]`: 다른 언어로 된 요소에 대한 자세한 지식을 추가하려면 다음을 수행하세요.  - `executionState[string]`: 작업 호출 결과 상태  - `hasDataSpecification[array]`: 데이터 사양 템플릿을 사용하여 확장할 수 있는 요소입니다. 데이터 사양 템플릿은 요소가 가질 수 있거나 가져야 하는 추가 속성의 명명된 집합을 정의합니다. RAMI4.0 사양  - `id[*]`: 엔티티의 고유 식별자  - `idShort[string]`: 짧은 ID는 RAMI40 환경 내에서 하위 모델 요소의 (짧은) 이름입니다.  - `inoutputVariable[array]`: 연산의 입력 및 출력인 매개변수가 있는 배열  - `inputVariable[array]`: 작업의 입력 매개변수가 있는 배열  - `kind[string]`: '유형'과 '인스턴스'의 구분을 위해 '종류'라는 용어가 사용됩니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인스트링, 다각형, 멀티포인트, 멀티라인스트링 또는 멀티폴리곤일 수 있습니다.  - `modelType[object]`: '유형'과 '인스턴스'의 구분을 위해 '종류'라는 용어가 사용됩니다.  	- `name[string]`: 항목의 속성입니다. 일반적으로 이 유형에는 -작동-이 설정됩니다.    
- `name[string]`: 이 항목의 이름  - `operationResult[object]`: 연산 호출의 반환된 결과가 있는 연산 호출 결과 객체를 포함합니다.  	- `entity[object]`: 작업 결과에 연결된 속성 집합    
	- `entityType[string]`: 엔티티 유형 설명/참조    
	- `isException[boolean]`: 예외인 경우 사실    
	- `messages[array]`: 요청자에 대한 정보가 포함된 추가 메시지    
	- `success[boolean]`: 작업이 성공하면 성공 참입니다. 실패하면 거짓    
- `outputVariable[array]`: 작업의 출력 매개변수가 있는 배열  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `refI4AASId[string]`: 이 서브모델 엘리먼트가 속한 루트 에셋 관리 셸을 참조합니다.  - `refI4AssetId[string]`: 이 서브모델 엘리먼트가 속한 루트 에셋을 참조합니다.  - `refI4SubmodelId[string]`: 이 서브모델 엘리먼트가 속한 루트 서브모델을 참조합니다.  - `requestId[string]`: 전송된 클라이언트 요청 ID(INPUT의 경우) 및/또는 검색된 값/상태(OUTPUT의 경우). 작업 추적에 사용  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `semanticId[object]`: 하위 모델 요소의 공식을 설명하는 외부 정보 소스를 참조합니다.  	- `keys[array]`: 시맨틱 ID의 키    
- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `timeout[number]`: OPC-UA 서버가 보고한 이 명령의 시간 초과 값을 나타냅니다.  - `type[string]`: RAMI4.0 AAS 디지털 트윈 서브모델 오퍼레이션 컴포넌트를 나타내려면 RAMI4.0 I4SubmodelElementOperation NGSI 엔티티 유형이어야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
## 페이로드 예시  
#### I4SubmodelElementOperation NGSI-v2 키 값 예제  
다음은 키 값으로 JSON-LD 형식의 I4SubmodelElementOperation의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### I4SubmodelElementOperation NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 I4SubmodelElementOperation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### I4SubmodelElementOperation NGSI-LD 키 값 예제  
다음은 키 값으로 JSON-LD 형식의 I4SubmodelElementOperation의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### I4SubmodelElementOperation NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 I4SubmodelElementOperation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
규모 단위를 다루는 방법에 대한 답변은 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
