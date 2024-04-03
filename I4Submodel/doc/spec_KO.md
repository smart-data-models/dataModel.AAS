<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: I4Submodel  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4Submodel/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **IDTA-01001-3-0에 기반하여, RAMI4.0 자산 관리 셸의 일반 하위 모델 구성 요소를 설명합니다**.  
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
- `administration[object]`: AAS 하위 모델 관리 정보  	- `revision[string]`: AAS 개정 번호는 사양 릴리스에 따른 번호입니다.    
	- `version[string]`: AAS 버전 번호는 사양 릴리스에 따른 번호입니다.    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: 카테고리는 요소의 클래스에 대한 추가 메타 정보를 제공하는 값입니다.  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `descriptions[array]`: 다른 언어로 된 AAS에 대한 자세한 지식을 추가하려면 다음과 같이 하세요.  - `hasDataSpecification[array]`: 데이터 사양은 하위 모델이 가질 수 있는 추가 속성을 정의합니다. RAMI4.0 사양  - `id[*]`: 엔티티의 고유 식별자  - `idShort[string]`: 짧은 ID는 RAMI40 환경 내 하위 모델의 (짧은) 이름입니다.  - `identification[object]`: AAS 내에서 하위 모델 식별. RAMI4.0 환경  	- `id[uri]`: 한 하위 모델을 다른 하위 모델과 명확하게 구분하는 신원 정보 -NGSI Id-. RAMI4.0 환경    
	- `idType[string]`: 식별자 유형(예: IRI 또는 IRDI)    
- `kind[string]`: '유형'과 '인스턴스'의 구분을 위해 '종류'라는 용어가 사용됩니다.  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인스트링, 다각형, 멀티포인트, 멀티라인스트링 또는 멀티폴리곤일 수 있습니다.  - `modelType[object]`: '유형'과 '인스턴스'의 구분을 위해 '종류'라는 용어가 사용됩니다.  	- `name[string]`: 항목의 속성입니다. 일반적으로 이 유형에는 하위 모델이 설정됩니다.    
- `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `qualifiers[array]`: 한정자는 한정자와 관계없이 요소의 의미가 동일한 경우에 사용됩니다. 요소의 품질이나 값의 의미만 다를 뿐입니다.  - `refI4AASId[string]`: 이 서브모델이 속한 루트 에셋 관리 셸을 참조합니다.  - `refI4AssetId[string]`: 이 서브모델이 속한 루트 애셋을 참조합니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `semanticId[object]`: 하위 모델의 공식을 설명하는 외부 정보 소스를 참조합니다.  	- `keys[array]`: 시맨틱 ID의 키    
- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `submodelElements[array]`: 요소 목록이 포함된 데이터 요소 - 연산 또는 명령 및 속성 - RAMI 명령의 경우 I4SubmodelElementOperation / RAMI 속성의 경우 I4SubmodelElementProperty.  - `type[string]`: RAMI4.0 AAS 디지털 트윈 서브모델 컴포넌트를 나타내려면 RAMI4.0 I4Submodel NGSI 엔티티 유형이어야 합니다.  <!-- /30-PropertiesList -->  
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
I4Submodel:    
  description: 'Based on IDTA-01001-3-0, describes a generic submodel component of the RAMI4.0 Asset Administration Shell'    
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
      description: AAS Submodel administration information    
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
      description: For adding detailed knowledge about the AAS in different languages    
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
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    hasDataSpecification:    
      description: Data specification defines the additional attributes a Submodel may have. RAMI4.0 specification    
      items:    
        properties:    
          type:    
            description: 'Link, url or description of the specified data'    
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
      description: short id is the (short) name of the Submodel within RAMI40 environment    
      type: string    
      x-ngsi:    
        type: Property    
    identification:    
      description: Identification of the Submodel within its AAS. RAMI4.0 environment    
      properties:    
        id:    
          description: 'Identity information that unambiguously distinguishes one Submodel from another one -NGSI Id-. RAMI4.0 environment '    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        idType:    
          description: 'Type of the Identifier, eg.IRI or IRDI'    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
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
      description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used.'    
      properties:    
        name:    
          description: Property of the item. Usually Submodel is set for this type.    
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
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    qualifiers:    
      description: Qualifiers are used if the semantics of the element is the same independent of its qualifiers. It is only the quality or the meaning of the value for the element that differs    
      items:    
        properties:    
          type:    
            description: 'Link, url or description of the qualifier'    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    refI4AASId:    
      description: References the root Asset Administration Shell which this Submodel belongs to    
      type: string    
      x-ngsi:    
        type: Relationship    
    refI4AssetId:    
      description: References the root Asset which this Submodel belongs to    
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
      description: 'It refer to an external information source, which explains the formulation of the submodel'    
      properties:    
        keys:    
          description: Keys for the Semantic ID    
          items:    
            description: Every Semantic ID element    
            type: string    
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
    submodelElements:    
      description: Data element which includes the list of Elements -Operations or Commands AND Properties- I4SubmodelElementOperation for RAMI commands / I4SubmodelElementProperty for RAMI Properties    
      items:    
        description: Link to the RAMI40 element -I4SubmodelElementOperation or I4SubmodelElementProperty- that maps the Command/Property of the RAMI Submodel    
        properties:    
          category:    
            description: The category is a value that gives further meta information w.r.t. to the class of the element    
            type: string    
            x-ngsi:    
              type: Property    
          idShort:    
            description: short id is the (short) name of the Submodel within RAMI40 environment    
            type: string    
            x-ngsi:    
              type: Property    
          modelType:    
            properties:    
              name:    
                description: Property of the item. Name of the model type    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
          refI4SubmodelElement:    
            description: Link to the NGSI entity -I4SubmodelElementOperation or I4SubmodelElementProperty- that maps the Command/Property of the Submodel    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: It has to be RAMI4.0 I4Submodel NGSI Entity type to represent a RAMI4.0 AAS Digital Twin Submodel component    
      enum:    
        - I4Submodel    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2023/04/IDTA-01001-3-0_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AAS/blob/master/I4Submodel/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.AAS/I4Submodel/schema.json    
  x-model-tags: Corosect    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### I4Submodel NGSI-v2 키 값 예제  
다음은 키 값으로 JSON-LD 형식의 I4Submodel의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI",  
  "type": "I4Submodel",  
  "administration": {  
    "version": "1.0",  
    "revision": ""  
  },  
  "category": "CONSTANT",  
  "descriptions": [  
    {  
      "language": "en",  
      "text": "Contains technical data related to ICrate"  
    }  
  ],  
  "hasDataSpecification": [],  
  "idShort": "TechnicalData",  
  "identification": {  
    "idType": "IRI",  
    "id": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI"  
  },  
  "kind": "Instance",  
  "modelType": {  
    "name": "Submodel"  
  },  
  "qualifiers": [],  
  "refI4AASId": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
  "refI4AssetId": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
  "semanticId": {  
    "keys": []  
  },  
  "submodelElements": [  
    {  
      "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:MRobotTaskConfigured:AASMRobotVI",  
      "idShort": "MRobotTaskConfigured",  
      "category": "PARAMETER",  
      "modelType": {  
        "name": "Property"  
      }  
    },  
    {  
      "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:MRobotMovementStatusConfigured:AASMRobotVI",  
      "idShort": "MRobotMovementStatusConfigured",  
      "category": "PARAMETER",  
      "modelType": {  
        "name": "Property"  
      }  
    },  
    {  
      "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:StatusConfigured:AASMRobotVI",  
      "idShort": "StatusConfigured",  
      "category": "PARAMETER",  
      "modelType": {  
        "name": "Property"  
      }  
    },  
    {  
      "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:TaskStatusConfigured:AASMRobotVI",  
      "idShort": "TaskStatusConfigured",  
      "category": "PARAMETER",  
      "modelType": {  
        "name": "Property"  
      }  
    },  
    {  
      "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:VIConfiguredInspectionType:AASMRobotVI",  
      "idShort": "VIConfiguredInspectionType",  
      "category": "PARAMETER",  
      "modelType": {  
        "name": "Property"  
      }  
    },  
    {  
      "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:VIConfiguredFarmType:AASMRobotVI",  
      "idShort": "VIConfiguredFarmType",  
      "category": "PARAMETER",  
      "modelType": {  
        "name": "Property"  
      }  
    },  
    {  
      "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:VIConfiguredDOL:AASMRobotVI",  
      "idShort": "VIConfiguredDOL",  
      "category": "PARAMETER",  
      "modelType": {  
        "name": "Property"  
      }  
    }  
  ]  
}  
```  
</details>  
#### I4Submodel NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 I4Submodel의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI",  
  "type": "I4Submodel",  
  "administration": {  
    "type": "StructuredValue",  
    "value": {  
      "version": "1.0",  
      "revision": ""  
    }  
  },  
  "category": {  
    "type": "Text",  
    "value": "CONSTANT"  
  },  
  "descriptions": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "language": "en",  
        "text": "Contains technical data related to ICrate"  
      }  
    ]  
  },  
  "hasDataSpecification": {  
    "type": "StructuredValue",  
    "value": []  
  },  
  "idShort": {  
    "type": "Text",  
    "value": "TechnicalData"  
  },  
  "identification": {  
    "type": "StructuredValue",  
    "value": {  
      "idType": "IRI",  
      "id": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI"  
    }  
  },  
  "kind": {  
    "type": "Text",  
    "value": "Instance"  
  },  
  "modelType": {  
    "type": "StructuredValue",  
    "value": {  
      "name": "Submodel"  
    }  
  },  
  "qualifiers": {  
    "type": "StructuredValue",  
    "value": []  
  },  
  "refI4AASId": {  
    "type": "Text",  
    "value": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI"  
  },  
  "refI4AssetId": {  
    "type": "Text",  
    "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI"  
  },  
  "semanticId": {  
    "type": "StructuredValue",  
    "value": {  
      "keys": []  
    }  
  },  
  "submodelElements": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:MRobotTaskConfigured:AASMRobotVI",  
        "idShort": "MRobotTaskConfigured",  
        "category": "PARAMETER",  
        "modelType": {  
          "name": "Property"  
        }  
      },  
      {  
        "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:MRobotMovementStatusConfigured:AASMRobotVI",  
        "idShort": "MRobotMovementStatusConfigured",  
        "category": "PARAMETER",  
        "modelType": {  
          "name": "Property"  
        }  
      },  
      {  
        "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:StatusConfigured:AASMRobotVI",  
        "idShort": "StatusConfigured",  
        "category": "PARAMETER",  
        "modelType": {  
          "name": "Property"  
        }  
      },  
      {  
        "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:TaskStatusConfigured:AASMRobotVI",  
        "idShort": "TaskStatusConfigured",  
        "category": "PARAMETER",  
        "modelType": {  
          "name": "Property"  
        }  
      },  
      {  
        "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:VIConfiguredInspectionType:AASMRobotVI",  
        "idShort": "VIConfiguredInspectionType",  
        "category": "PARAMETER",  
        "modelType": {  
          "name": "Property"  
        }  
      },  
      {  
        "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:VIConfiguredFarmType:AASMRobotVI",  
        "idShort": "VIConfiguredFarmType",  
        "category": "PARAMETER",  
        "modelType": {  
          "name": "Property"  
        }  
      },  
      {  
        "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:VIConfiguredDOL:AASMRobotVI",  
        "idShort": "VIConfiguredDOL",  
        "category": "PARAMETER",  
        "modelType": {  
          "name": "Property"  
        }  
      }  
    ]  
  }  
}  
```  
</details>  
#### I4Submodel NGSI-LD 키 값 예제  
다음은 키 값으로 JSON-LD 형식의 I4Submodel의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI",  
  "type": "I4Submodel",  
  "administration": {  
    "version": "1.0",  
    "revision": ""  
  },  
  "category": "CONSTANT",  
  "descriptions": [  
    {  
      "language": "en",  
      "text": "Contains technical data related to ICrate"  
    }  
  ],  
  "hasDataSpecification": [],  
  "idShort": "TechnicalData",  
  "identification": {  
    "idType": "IRI",  
    "id": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI"  
  },  
  "kind": "Instance",  
  "modelType": {  
    "name": "Submodel"  
  },  
  "qualifiers": [],  
  "refI4AASId": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
  "refI4AssetId": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
  "semanticId": {  
    "keys": []  
  },  
  "submodelElements": [  
    {  
      "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:MRobotTaskConfigured:AASMRobotVI",  
      "idShort": "MRobotTaskConfigured",  
      "category": "PARAMETER",  
      "modelType": {  
        "name": "Property"  
      }  
    },  
    {  
      "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:MRobotMovementStatusConfigured:AASMRobotVI",  
      "idShort": "MRobotMovementStatusConfigured",  
      "category": "PARAMETER",  
      "modelType": {  
        "name": "Property"  
      }  
    },  
    {  
      "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:StatusConfigured:AASMRobotVI",  
      "idShort": "StatusConfigured",  
      "category": "PARAMETER",  
      "modelType": {  
        "name": "Property"  
      }  
    },  
    {  
      "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:TaskStatusConfigured:AASMRobotVI",  
      "idShort": "TaskStatusConfigured",  
      "category": "PARAMETER",  
      "modelType": {  
        "name": "Property"  
      }  
    },  
    {  
      "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:VIConfiguredInspectionType:AASMRobotVI",  
      "idShort": "VIConfiguredInspectionType",  
      "category": "PARAMETER",  
      "modelType": {  
        "name": "Property"  
      }  
    },  
    {  
      "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:VIConfiguredFarmType:AASMRobotVI",  
      "idShort": "VIConfiguredFarmType",  
      "category": "PARAMETER",  
      "modelType": {  
        "name": "Property"  
      }  
    },  
    {  
      "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:VIConfiguredDOL:AASMRobotVI",  
      "idShort": "VIConfiguredDOL",  
      "category": "PARAMETER",  
      "modelType": {  
        "name": "Property"  
      }  
    }  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.AAS/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### I4Submodel NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 I4Submodel의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI",  
  "type": "I4Submodel",  
  "administration": {  
    "type": "Property",  
    "value": {  
      "version": "1.0",  
      "revision": ""  
    }  
  },  
  "category": {  
    "type": "Property",  
    "value": "CONSTANT"  
  },  
  "descriptions": {  
    "type": "Property",  
    "value": [  
      {  
        "language": "en",  
        "text": "Contains technical data related to ICrate"  
      }  
    ]  
  },  
  "hasDataSpecification": {  
    "type": "Property",  
    "value": []  
  },  
  "idShort": {  
    "type": "Property",  
    "value": "TechnicalData"  
  },  
  "identification": {  
    "type": "Property",  
    "value": {  
      "idType": "IRI",  
      "id": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI"  
    }  
  },  
  "kind": {  
    "type": "Property",  
    "value": "Instance"  
  },  
  "modelType": {  
    "type": "Property",  
    "value": {  
      "name": "Submodel"  
    }  
  },  
  "qualifiers": {  
    "type": "Property",  
    "value": []  
  },  
  "refI4AASId": {  
    "type": "Property",  
    "value": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI"  
  },  
  "refI4AssetId": {  
    "type": "Property",  
    "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI"  
  },  
  "semanticId": {  
    "type": "Property",  
    "value": {  
      "keys": []  
    }  
  },  
  "submodelElements": {  
    "type": "Property",  
    "value": [  
      {  
        "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:MRobotTaskConfigured:AASMRobotVI",  
        "idShort": "MRobotTaskConfigured",  
        "category": "PARAMETER",  
        "modelType": {  
          "name": "Property"  
        }  
      },  
      {  
        "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:MRobotMovementStatusConfigured:AASMRobotVI",  
        "idShort": "MRobotMovementStatusConfigured",  
        "category": "PARAMETER",  
        "modelType": {  
          "name": "Property"  
        }  
      },  
      {  
        "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:StatusConfigured:AASMRobotVI",  
        "idShort": "StatusConfigured",  
        "category": "PARAMETER",  
        "modelType": {  
          "name": "Property"  
        }  
      },  
      {  
        "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:TaskStatusConfigured:AASMRobotVI",  
        "idShort": "TaskStatusConfigured",  
        "category": "PARAMETER",  
        "modelType": {  
          "name": "Property"  
        }  
      },  
      {  
        "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:VIConfiguredInspectionType:AASMRobotVI",  
        "idShort": "VIConfiguredInspectionType",  
        "category": "PARAMETER",  
        "modelType": {  
          "name": "Property"  
        }  
      },  
      {  
        "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:VIConfiguredFarmType:AASMRobotVI",  
        "idShort": "VIConfiguredFarmType",  
        "category": "PARAMETER",  
        "modelType": {  
          "name": "Property"  
        }  
      },  
      {  
        "refI4SubmodelElement": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:TechnicalData:VIConfiguredDOL:AASMRobotVI",  
        "idShort": "VIConfiguredDOL",  
        "category": "PARAMETER",  
        "modelType": {  
          "name": "Property"  
        }  
      }  
    ]  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.AAS/master/context.jsonld"  
  ]  
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
