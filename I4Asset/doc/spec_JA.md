<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティI4アセット  
============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4Asset/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**IDTA-01001-3-0に基づき、RAMI4.0の一般的なAsset Administration Shell - AAS - コンポーネントであるAASにリンクされたAsset -instanceを定義する。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `administration[object]`: インスタンス管理情報  	- `revision[string]`: AASリビジョン番号は、仕様書のリリースに沿った番号です。    
	- `version[string]`: AASのバージョン番号は、仕様書のリリースに沿った番号です。    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `assetIdentificationModelRef[object]`: 資産は通常、シリアル番号や RFID コードなど、複数の異なる識別プロパティで表されることがあります。このようなローカルな識別プロパティは資産識別サブモデルで定義されます。  	- `keys[array]`: アセットインスタンスのキー    
- `billOfMaterialRef[object]`: 複合資産は、他の事業体や資産から構成される。資産の一部であるこれらの事業体や資産は、部品表で指定される。  	- `keys[array]`: セマンティックIDのキー    
- `category[string]`: カテゴリは、AASのクラスに関するさらなるメタ情報を与える値である。  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `descriptions[array]`: さまざまな言語の詳細な知識を追加する  - `hasDataSpecification[array]`: データ仕様は、アセットが持つ可能性のある追加属性を定義します。RAMI4.0仕様  - `id[*]`: エンティティの一意識別子  - `idShort[string]`: RAMI インスタンスの短い ID (名前)  - `identification[object]`: AAS -資産-インスタンスオブジェクトの識別  	- `id[uri]`: あるRAMIインスタンスと別のRAMIインスタンスを明確に区別する識別情報    
	- `idType[string]`: 識別子のタイプ（例：IRIまたはIRD    
- `kind[string]`: スキーマの種類。これはインスタンスに限定される。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `modelType[object]`: IDTAによるインスタンス・モデル・タイプ  	- `name[string]`: 参照アイテムのタイプ    
- `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: RAMI4.0 I4Asset NGSI Entity タイプでなければなりません。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
            - properties:    
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
                  type: string    
                value:    
                  description: Property. Value of the item    
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
            - properties:    
                idType:    
                  description: Property. idType of the item    
                  type: string    
                index:    
                  description: Property. Order of the item    
                  type: integer    
                local:    
                  description: Property. Whether if the item is local    
                  type: boolean    
                type:    
                  type: string    
                value:    
                  description: Property. Value of the item    
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
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### I4Asset NGSI-v2 キー値の例  
JSON-LD形式のI4Assetのkey-valuesの例です。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
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
    "idshort": "Asset",  
    "kind": "Instance",  
    "modelType": {  
        "name": "Asset"  
    }  
}  
```  
</details>  
#### I4Asset NGSI-v2 正規化例  
以下は、正規化されたJSON-LDフォーマットのI4Assetの例である。これはNGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。  
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
  "idshort": {  
      "type": "Text",  
      "value": "Asset",  
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
#### I4Asset NGSI-LD キー値の例  
JSON-LDフォーマットのI4Assetのkey-valuesの例です。これはNGSI-LDと互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
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
  "idshort": "Asset",  
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
#### I4Asset NGSI-LD 正規化例  
正規化されたJSON-LDフォーマットのI4Assetの例です。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
  "idshort": {  
    "type": "Property",  
    "value": "Asset"  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
