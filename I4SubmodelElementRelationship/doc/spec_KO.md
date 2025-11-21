<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: I4SubmodelElementRelationship  
==================================<!-- /10-Header -->  
<!-- 15-License -->  
데이터 모델 AAS 라이선스 (https://github.com/smart-data-models/dataModel.AAS/blob/master/I4SubmodelElementRelationship/LICENSE.md)  
자동 생성 문서 ([https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60])  
<!-- /15-License -->  
<!-- 20-Description -->  
IDTA-01001-3-0에 기반하여, IDTA-01001-3-0의 Generic RAMI4.0 SubmodelElement은 참조 자산 관리 셸의 관계를 나타내는 것  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  
특성 목록  
<sup><sub>[*] 유형이 속성에서 나타나지 않는 이유는 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 나라. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 거리 주소에 위치한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 지역은 해당 지역과, 그리고 해당 지역이 국가에 속하는 곳  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지역은 일부 국가에서 지역 정부가 관리하는 유형의 행정 구역이다.    
	- `postOfficeBoxNumber[string]`: PO 박스 번호는 우편 박스 주소입니다. 예를 들어 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편번호. 예를 들어 24004 입니다.  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 특정 도로의 특정 속성 식별하는 번호    
- `alternateName[string]`: 이 물건에 대한 대체 명칭  - `areaServed[string]`: 서비스 또는 제공되는 지역  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: 범주에 대한 추가 메타 정보와 관련하여 요소의 클래스에 대한 정보 제공하는 분류입니다.  - `dataProvider[string]`:  harmonize 데이터 엔티티를 제공하는 데이터 시퀀스  - `dateCreated[date-time]`: 엔터티 생성 시간. 일반적으로 저장 플랫폼에서 할당됩니다.  - `dateModified[date-time]`: 엔터티의 마지막 수정 시점입니다. 일반적으로 저장 플랫폼에서 할당됩니다.  - `description[string]`: 이 물품에 대한 설명  - `descriptions[array]`: 다양한 언어로 요소에 대한 상세한 지식을 추가하는 것에 대해  - `first[string]`: 관계 요소의 첫 번째 참조 요소에 대한 참조 요소의 첫 번째 참조를 언급한다.  - `hasDataSpecification[array]`: 데이터 지정 양식의 확장 요소. 데이터 지정 양식은 요소가 가질 수 있는 추가 속성 집합을 정의합니다. RAMI4.0 특성 설명  - `id[*]`: Entity의 고유 식별자  - `idShort[string]`: RAMI40 환경 내 SubmodelElement의 짧은 ID는 (short) 이름입니다.  - `kind[string]`: ‘종류’와 ‘개별 인스턴스’를 구별하기 위해 ‘종’이라는 용어를 사용합니다.  - `location[*]`: 아이템에 대한 지오펜조 참조입니다. 점, 선분, 폴리곤, 다중점, 다중선분 또는 다중폴리곤 중 하나일 수 있습니다.  - `modelType[object]`: ‘종류’와 ‘개별 인스턴스’를 구별하기 위해 ‘종’이라는 용어를 사용합니다.  	- `name[string]`: 항목의 속성입니다. 일반적으로 이 유형에는 -운영-이 설정됩니다.    
- `name[string]`: 이 상품의 이름  - `owner[array]`: JSON 코드가 암호화된 문자열을 포함하는 목록으로, 소유자(또는 소유자들의) 고유 ID를 참조하는 목록  - `refI4AASId[string]`: 이 하위 요소가 속한 자산 관리 셸의 근원 참조  - `refI4AssetId[string]`: 이 하위 요소가 속한 뿌리 자산에 대한 참조입니다.  - `second[string]`: 관계 요소의 두 번째 참조 요소에 대한 참조 요소의 참조.  - `seeAlso[*]`: 유리(Uri)를 통해 추가 자원 정보에 대한 내용  - `semanticId[object]`: 이는 하위 모델 요소의 형식을 설명하는 외부 정보 소스입니다.  	- `keys[array]`: 의미적 ID 키    
- `source[string]`: 원본 데이터의 출처를 나타내는 문자열의 시퀀스입니다. 원본 제공업체의 완전한 도메인 이름으로 권장되며, 소스 객체에 대한 URL입니다.  - `type[string]`: RAMI4.0 I4SubmodelElementRelationship NGSI Entity type to represent a RAMI4.0 AAS Digital Twin Submodel Relationship component  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수적인 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Property 모델 설명  
알림 목록을 오름차순으로 정렬 (세부 정보 보기 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
I4SubmodelElementRelationship:    
  description: 'Based on IDTA-01001-3-0, describes a generic RAMI4.0 SubmodelElement representing an Relationship of a referenced Asset Administration Shell'    
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
    first:    
      description: References the first Reference Element of the Relationship Element.    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    second:    
      description: References the second Reference Element of the Relationship Element.    
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
      description: It has to be RAMI4.0 I4SubmodelElementRelationship NGSI Entity type to represent a RAMI4.0 AAS Digital Twin Submodel Relationship component    
      enum:    
        - I4SubmodelElementRelationship    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2023/04/IDTA-01001-3-0_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AAS/blob/master/I4SubmodelElementRelationship/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.AAS/I4SubmodelElementRelationship/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
예시 포설드  
NGSI-v2 key-values Example  I4SubmodelElementRelationship  
I4SubmodelElementRelationship in JSON-LD format as key-value pairs is an example. It’s compatible with NGSI-v2 when using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RAMI40:I4SubmodelElementRelationship:OperationManagementAgent:PlanOperation",  
  "type": "I4SubmodelElementRelationship",  
  "descriptions": [  
      {  
          "language": "en",  
          "text": "Submodel Relationship [contains various data related to the Relationship of an intelligent agent capability to its operations]"  
      }  
  ],    
  "hasDataSpecification": [],  
  "idShort": "I4SubmodelElementRelationship:OperationManagementAgent:PlanOperation",  
  "category": "PARAMETER",  
  "kind": "Instance",  
  "modelType": {  
      "name": "Relationship"  
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
  "first": "urn:ngsi-ld:RAMI40:I4SubmodelElementCapability:OperationManagementAgent:PlanOperation",  
  "second": "urn:ngsi-ld:RAMI40:I4SubmodelElementOperation:OperationManagementAgent:PlanOperationSchedule"  
}  
```  
</details>  
NGSI-v2 normalized Example  
I4SubmodelElementRelationship의 JSON-LD 형식으로 정상화된 예시입니다. NGSI-v2를 사용하지 않을 경우에도 해당 개체에 대한 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RAMI40:I4SubmodelElementRelationship:OperationManagementAgent:PlanOperation",  
  "type": "I4SubmodelElementRelationship",  
  "descriptions": {  
      "type": "Property",  
      "value": [  
       {  
          "language": "en",  
          "text": "Submodel Relationship [contains various data related to the Relationship of an intelligent agent capability to its operations]"  
       }  
    ]  
  },    
  "hasDataSpecification": {  
    "type": "Property",  
    "value": "None"  
  },  
  "idShort": {  
    "type": "Property",  
    "value": "I4SubmodelElementRelationship:OperationManagementAgent:PlanOperation"  
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
      "name": "Relationship"  
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
  "first": {  
    "type": "Property",  
    "value": "urn:ngsi-ld:RAMI40:I4SubmodelElementCapability:OperationManagementAgent:PlanOperation"  
  },  
  "second": {  
    "type": "Property",  
    "value": "urn:ngsi-ld:RAMI40:I4SubmodelElementOperation:OperationManagementAgent:PlanOperationSchedule"  
  }      
}  
```  
</details>  
NGSI-LD 키-값 예시: I4SubmodelElementRelationship  
I4SubmodelElementRelationship의 JSON-LD 형식으로, 키-값 쌍으로 표현되는 예시입니다. NGSI-LD를 사용할 때 `options=keyValues`와 함께 사용하면 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RAMI40:I4SubmodelElementRelationship:OperationManagementAgent:PlanOperation",  
  "type": "I4SubmodelElementRelationship",  
  "descriptions": [  
      {  
          "language": "en",  
          "text": "Submodel Relationship [contains various data related to the Relationship of an intelligent agent capability to its operations]"  
      }  
  ],    
  "hasDataSpecification": [],  
  "idShort": "I4SubmodelElementRelationship:OperationManagementAgent:PlanOperation",  
  "category": "PARAMETER",  
  "kind": "Instance",  
  "modelType": {  
      "name": "Relationship"  
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
  "first": "urn:ngsi-ld:RAMI40:I4SubmodelElementCapability:OperationManagementAgent:PlanOperation",  
  "second": "urn:ngsi-ld:RAMI40:I4SubmodelElementOperation:OperationManagementAgent:PlanOperationSchedule",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]    
}  
```  
</details>  
NGSI-LD normalized Example  
I4SubmodelElementRelationship in JSON-LD 형식으로 정상화된 예시입니다. NGSI-LD를 사용하지 않을 때도 호환되며, 개별 개체에 대한 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RAMI40:I4SubmodelElementRelationship:OperationManagementAgent:PlanOperation",  
  "type": "I4SubmodelElementRelationship",  
  "descriptions": {  
      "type": "Property",  
      "value": [  
       {  
          "language": "en",  
          "text": "Submodel Relationship [contains various data related to the Relationship of an intelligent agent capability to its operations]"  
       }  
    ]  
  },    
  "hasDataSpecification": {  
    "type": "Property",  
    "value": "None"  
  },  
  "idShort": {  
    "type": "Property",  
    "value": "I4SubmodelElementRelationship:OperationManagementAgent:PlanOperation"  
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
      "name": "Relationship"  
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
  "first": {  
    "type": "Property",  
    "value": "urn:ngsi-ld:RAMI40:I4SubmodelElementCapability:OperationManagementAgent:PlanOperation"  
  },  
  "second": {  
    "type": "Property",  
    "value": "urn:ngsi-ld:RAMI40:I4SubmodelElementOperation:OperationManagementAgent:PlanOperationSchedule"  
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
FAQ 10 ([https://smartdatamodels.org/index.php/faqs/10](https://smartdatamodels.org/index.php/faqs/10))에 대해 규모 단위 문제에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
