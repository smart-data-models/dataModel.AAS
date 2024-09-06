<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 엔티티: I4Asset  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4Asset/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **IDTA-01001-3-0에 기반하여, 지정된 AAS에 연결된 자산 -인스턴스-를 RAMI4.0의 일반 자산 관리 셸 - AAS - 구성 요소로 정의합니다**.  
버전: 0.0.2  
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
- `administration[object]`: 인스턴스 관리 정보  	- `revision[string]`: AAS 개정 번호는 사양 릴리스에 따른 번호입니다.    
	- `version[string]`: AAS 버전 번호는 사양 릴리스에 따른 번호입니다.    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `assetIdentificationModelRef[object]`: 자산은 일반적으로 일련 번호, RFID 코드 등과 같은 여러 가지 식별 속성으로 표현될 수 있습니다. 이러한 로컬 식별 속성은 자산 식별 하위 모델에 정의됩니다.  	- `keys[array]`: 에셋 인스턴스에 대한 키    
- `billOfMaterialRef[object]`: 복합 자산은 다른 엔티티와 자산으로 구성됩니다. 자산의 일부인 이러한 엔티티와 자산은 자재 명세서에 명시되어 있습니다.  	- `keys[array]`: 시맨틱 ID의 키    
- `category[string]`: 카테고리는 AAS의 클래스에 대한 추가 메타 정보를 제공하는 값입니다.  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `descriptions[array]`: 다른 언어로 자세한 지식을 추가하려면  - `hasDataSpecification[array]`: 데이터 사양은 자산이 가질 수 있는 추가 속성을 정의합니다. RAMI4.0 사양  - `id[*]`: 엔티티의 고유 식별자  - `idShort[string]`: RAMI 인스턴스의 짧은 ID(이름)  - `identification[object]`: AAS -자산- 인스턴스 개체 식별  	- `id[uri]`: 하나의 RAMI 인스턴스를 다른 인스턴스와 명확하게 구분하는 신원 정보    
	- `idType[string]`: 식별자 유형(예: IRI 또는 IRD)    
- `kind[string]`: 스키마의 종류. 이것은 인스턴스  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인스트링, 다각형, 멀티포인트, 멀티라인스트링 또는 멀티폴리곤일 수 있습니다.  - `modelType[object]`: IDTA에 따른 인스턴스 모델 유형  	- `name[string]`: 참조된 항목의 유형    
- `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: RAMI4.0 I4Asset NGSI 엔티티 유형이어야 합니다.  <!-- /30-PropertiesList -->  
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
I4Asset:    
  description: 'Based on IDTA-01001-3-0, defines the Asset -instance- linked to a given AAS a generic Asset Administration Shell - AAS -  component of the RAMI4.0'    
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
      description: Instance administration information    
      properties:    
        revision:    
          description: AAS Revision number is the number in line with release of specification    
          type: string    
          x-ngsi:    
            type: Property    
        version:    
          description: AAS version number is the number in line with release of specification    
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
    assetIdentificationModelRef:    
      description: 'An asset typically may be represented by several different identification properties like for example the serial number, its RFID code etc. Such local identification properties are defined in the asset identification submodel'    
      properties:    
        keys:    
          description: keys for the asset instance    
          items:    
            - description: 'Property. object containing the properties type, local, value, index and idtype'    
              properties:    
                idType:    
                  description: Property. idType of the item    
                  type: string    
                index:    
                  description: Property. Integer related to the item    
                  type: integer    
                local:    
                  description: Property. True if this is local item. False if not    
                  type: boolean    
                type:    
                  description: Property. Type of the object inside the keys of the assetIdentificationModelRef    
                  type: string    
                value:    
                  description: Property. Value of the item of the object    
                  type: string    
              type: object    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    billOfMaterialRef:    
      description: A complex asset is composed out of other entities and assets. These entities and assets being part of the asset are specified in the bill of material    
      properties:    
        keys:    
          description: Keys for the Semantic ID    
          items:    
            - description: 'Property. object containing the properties type, local, value, index and idtype'    
              properties:    
                idType:    
                  description: Property. idType of the item    
                  type: string    
                index:    
                  description: Property. Order of the item in the object    
                  type: integer    
                local:    
                  description: Property. Whether the item is local. False if not    
                  type: boolean    
                type:    
                  description: Property. Type of the object inside the keys of the billOfMaterialRef    
                  type: string    
                value:    
                  description: Property. Value of the item of the object    
                  type: string    
              type: object    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    category:    
      description: The category is a value that gives further meta information w.r.t. to the class of the AAS    
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
      description: For adding detailed knowledge in different languages    
      items:    
        description: object containing the properties language and text    
        properties:    
          language:    
            description: Substring identifying the language. Acronym according to ISO 639-1    
            type: string    
            x-ngsi:    
              type: Property    
          text:    
            description: Add the description text here    
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
      description: Data specification defines the additional attributes an asset may have. RAMI4.0 specification    
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
      description: Short id (name) of the RAMI Instance    
      type: string    
      x-ngsi:    
        type: Property    
    identification:    
      description: Identification of the AAS -Asset- Instance object    
      properties:    
        id:    
          description: Identity information that unambiguously distinguishes one RAMI Instance from another one    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        idType:    
          description: 'Type of the Identifier, eg.IRI or IRD'    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    kind:    
      description: Kind of the Schema. This is restricted to Instance    
      enum:    
        - Instance    
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
      description: Instance model type according to IDTA    
      properties:    
        name:    
          description: Type of the referenced item    
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
    type:    
      description: It has to be RAMI4.0 I4Asset NGSI Entity type    
      enum:    
        - I4Asset    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2023/04/IDTA-01001-3-0_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AAS/blob/master/I4Asset/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.AAS/I4Asset/schema.json    
  x-model-tags: Corosect    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### I4Asset NGSI-v2 키 값 예시  
다음은 JSON-LD 형식의 I4Asset을 키값으로 사용하는 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
    "type": "I4Asset",  
    "administration": {  
        "version": "1.0",  
        "revision": "\n      "  
    },  
    "assetIdentificationModelRef": {  
        "keys": [  
            {  
                "type": "Submodel",  
                "local": true,  
                "value": "urn:ngsi-v2:RAMI40:I4Submodel:NamePlate:AASMRobotVI",  
                "index": 0,  
                "idType": "IRI"  
            }  
        ]  
    },  
    "billOfMaterialRef": {  
        "keys": [  
            {  
                "type": "Submodel",  
                "local": true,  
                "value": "urn:ngsi-v2:RAMI40:I4Submodel:BillOfMaterial:AASMRobotVI",  
                "index": 0,  
                "idType": "IRI"  
            }  
        ]  
    },  
    "category": "CONSTANT",  
    "descriptions": [  
        {  
            "language": "en",  
            "text": "MRobotVI asset"  
        }  
    ],  
    "hasDataSpecification": [],  
    "idShort": "MRobotVI",  
    "identification": {  
        "idType": "IRI",  
        "id": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI"  
    },  
    "kind": "Instance",  
    "modelType": {  
        "name": "Asset"  
    }  
}  
```  
</details>  
#### I4Asset NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 I4Asset의 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
  "type": "I4Asset",  
  "administration": {  
      "type": "StructuredValue",  
      "value": {  
          "version": "1.0",  
          "revision": "\n      "  
      },  
      "metadata": {}  
  },  
  "assetIdentificationModelRef": {  
      "type": "StructuredValue",  
      "value": {  
          "keys": [  
              {  
                  "type": "Submodel",  
                  "local": true,  
                  "value": "urn:ngsi-v2:RAMI40:I4Submodel:NamePlate:AASMRobotVI",  
                  "index": 0,  
                  "idType": "IRI"  
              }  
          ]  
      },  
      "metadata": {}  
  },  
  "billOfMaterialRef": {  
      "type": "StructuredValue",  
      "value": {  
          "keys": [  
              {  
                  "type": "Submodel",  
                  "local": true,  
                  "value": "urn:ngsi-v2:RAMI40:I4Submodel:BillOfMaterial:AASMRobotVI",  
                  "index": 0,  
                  "idType": "IRI"  
              }  
          ]  
      },  
      "metadata": {}  
  },  
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
              "text": "MRobotVI asset"  
          }  
      ],  
      "metadata": {}  
  },  
  "hasDataSpecification": {  
      "type": "StructuredValue",  
      "value": [],  
      "metadata": {}  
  },  
  "idShort": {  
      "type": "Text",  
      "value": "Asset",  
      "metadata": {}  
  },  
  "identification": {  
      "type": "StructuredValue",  
      "value": {  
          "idType": "IRI",  
          "id": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI"  
      },  
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
          "name": "Asset"  
      },  
      "metadata": {}  
  }  
}  
```  
</details>  
#### I4Asset NGSI-LD 키 값 예시  
다음은 JSON-LD 형식의 I4Asset을 키값으로 사용하는 예시입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
  "type": "I4Asset",  
  "administration": {  
    "version": "1.0",  
    "revision": "\n      "  
  },  
  "assetIdentificationModelRef": {  
    "keys": [  
      {  
        "type": "Submodel",  
        "local": true,  
        "value": "urn:ngsi-v2:RAMI40:I4Submodel:NamePlate:AASMRobotVI",  
        "index": 0,  
        "idType": "IRI"  
      }  
    ]  
  },  
  "billOfMaterialRef": {  
    "keys": [  
      {  
        "type": "Submodel",  
        "local": true,  
        "value": "urn:ngsi-v2:RAMI40:I4Submodel:BillOfMaterial:AASMRobotVI",  
        "index": 0,  
        "idType": "IRI"  
      }  
    ]  
  },  
  "category": "CONSTANT",  
  "descriptions": [  
    {  
      "language": "en",  
      "text": "MRobotVI asset"  
    }  
  ],  
  "hasDataSpecification": [],  
  "idShort": "MRobotVI",  
  "identification": {  
    "idType": "IRI",  
    "id": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI"  
  },  
  "kind": "Instance",  
  "modelType": {  
    "name": "Asset"  
  },  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.AAS/context.jsonld"  
  ]  
}  
```  
</details>  
#### I4Asset NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 I4Asset의 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
  "type": "I4Asset",  
  "administration": {  
    "type": "Property",  
    "value": {  
      "version": "1.0",  
      "revision": "\n      "  
    }  
  },  
  "assetIdentificationModelRef": {  
    "type": "Property",  
    "value": {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": true,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:NamePlate:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    }  
  },  
  "billOfMaterialRef": {  
    "type": "Property",  
    "value": {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": true,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:BillOfMaterial:AASMRobotVI",  
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
  "descriptions": {  
    "type": "Property",  
    "value": [  
      {  
        "language": "en",  
        "text": "MRobotVI asset"  
      }  
    ]  
  },  
  "hasDataSpecification": {  
    "type": "Property",  
    "value": []  
  },  
  "idShort": {  
    "type": "Property",  
    "value": "Asset"  
  },  
  "identification": {  
    "type": "Property",  
    "value": {  
      "idType": "IRI",  
      "id": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI"  
    }  
  },  
  "kind": {  
    "type": "Property",  
    "value": "Instance"  
  },  
  "modelType": {  
    "type": "Property",  
    "value": {  
      "name": "Asset"  
    }  
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
