<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 엔티티: I4AAS  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4AAS/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **IDTA-01001-3-0에 기반하여, RAMI4.0의 구성 요소인 일반 자산 관리 셸 - AAS - 트리를 설명합니다**.  
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
- `administration[object]`: AAS 관리 정보  	- `revision[string]`: AAS 개정 번호는 사양 릴리스에 따른 번호입니다.    
	- `version[string]`: AAS 버전 번호는 사양 릴리스에 따른 번호입니다.    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `asset[object]`: 에셋 설명은 여기에 채워집니다.  	- `keys[array]`: 에셋의 키    
- `category[string]`: 카테고리는 요소의 클래스에 대한 추가 메타 정보를 제공하는 값입니다.  - `conceptDictionaries[array]`: 에셋 자체는 하위 모델 요소의 의미론적 정의를 포함하는 자체 사전을 정의할 수도 있습니다. 이러한 의미 정의를 개념 설명(ConceptDescription 또는 개념 사전)이라고 합니다. 이 배열에는 이 모델 내에서 사용되는 RAMI4.0 특정 개념에 대한 참조 ID가 포함됩니다.  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `descriptions[array]`: 다른 언어로 된 AAS에 대한 자세한 지식을 추가하려면 다음을 참조하세요.  - `hasDataSpecification[array]`: 데이터 사양은 자산이 가질 수 있는 추가 속성을 정의합니다. RAMI4.0 사양  - `id[*]`: 엔티티의 고유 식별자  - `idShort[string]`: 짧은 ID는 자산 관리 셸의 (짧은) 이름입니다.  - `identification[object]`: 자산에 대한 AAS 식별. RAMI4.0 환경  	- `id[uri]`: 한 AAS를 다른 AAS와 명확하게 구분하는 신원 정보입니다. RAMI4.0 환경    
	- `idType[string]`: 식별자 유형(예: IRI 또는 IRDI)    
- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인스트링, 다각형, 멀티포인트, 멀티라인스트링 또는 멀티폴리곤일 수 있습니다.  - `modelType[object]`: '유형'과 '인스턴스'의 구분을 위해 '종류'라는 용어가 사용됩니다.  	- `name[string]`: 항목의 참조된 속성에 대한 설명    
- `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `refI4AssetId[uri]`: 이 AAS에 연결된 루트 에셋을 참조합니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `submodels[array]`: AAS에는 복잡한 정보 집합이 포함되어 있으며, 하위 모델은 이 복잡한 데이터에 대해 별도의 범주를 제공합니다.  - `type[string]`: RAMI4.0 AAS 디지털 트윈을 나타내려면 RAMI4.0 I4AAS NGSI 엔티티 유형이어야 합니다.  <!-- /30-PropertiesList -->  
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
## 페이로드 예시  
#### I4AAS NGSI-v2 키 값 예시  
다음은 키 값으로 JSON-LD 형식의 I4AAS의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### I4AAS NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 I4AAS의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### I4AAS NGSI-LD 키 값 예시  
다음은 키 값으로 JSON-LD 형식의 I4AAS의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### I4AAS NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 I4AAS의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
규모 단위를 다루는 방법에 대한 답변은 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
