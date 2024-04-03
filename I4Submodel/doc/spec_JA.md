<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティI4Submodel  
================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4Submodel/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述**IDTA-01001-3-0 に基づき、RAMI4.0 Asset Administration Shell の汎用サブモデルコンポーネントを記述する。  
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
- `administration[object]`: AASサブモデルの管理情報  	- `revision[string]`: AASリビジョン番号は、仕様書のリリースに沿った番号です。    
	- `version[string]`: AASのバージョン番号は、仕様書のリリースに沿った番号です。    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: カテゴリは、要素のクラスに関するさらなるメタ情報を与える値です。  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `descriptions[array]`: AASに関する詳細な知識をさまざまな言語で追加する。  - `hasDataSpecification[array]`: データ仕様では、サブモデルが持つ可能性のある追加属性を定義します。RAMI4.0 仕様  - `id[*]`: エンティティの一意識別子  - `idShort[string]`: short id は、RAMI40 環境内でのサブモデルの (短い) 名前です。  - `identification[object]`: AAS 内のサブモデルの識別。RAMI4.0 環境  	- `id[uri]`: サブモデルと他のサブモデルを明確に区別するための識別情報 -NGSI Id-.RAMI4.0 環境    
	- `idType[string]`: 識別子のタイプ（例：IRIまたはIRDI    
- `kind[string]`: タイプ」と「インスタンス」を区別するために、「種類」という用語が使われる。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `modelType[object]`: タイプ」と「インスタンス」を区別するために、「種類」という用語が使われる。  	- `name[string]`: アイテムのプロパティ。通常、このタイプには Submodel が設定されます。    
- `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `qualifiers[array]`: 要素のセマンティクスが修飾子とは無関係に同じであれば、修飾子が使われる。異なるのは、要素に対する値の質または意味だけである。  - `refI4AASId[string]`: このサブモデルが属するルート資産管理シェルを参照します。  - `refI4AssetId[string]`: この Submodel が属するルート Asset を参照します。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `semanticId[object]`: サブモデルの定式化を説明する外部情報源を参照する。  	- `keys[array]`: セマンティックIDのキー    
- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `submodelElements[array]`: RAMI コマンドの場合は I4SubmodelElementOperation / RAMI プロパティの場合は I4SubmodelElementProperty となります。  - `type[string]`: RAMI4.0 AAS デジタルツインサブモデルのコンポーネントを表すには、RAMI4.0 I4Submodel NGSI Entity タイプでなければなりません。  <!-- /30-PropertiesList -->  
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
## ペイロードの例  
#### I4Submodel NGSI-v2 キー値の例  
以下はI4SubmodelをJSON-LD形式でkey-valuesとした例である。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
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
#### I4Submodel NGSI-v2 正規化例  
以下は正規化された JSON-LD フォーマットの I4Submodel の例である。これは、オプションを使用しない場合、NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### I4Submodel NGSI-LD キー値の例  
以下は I4Submodel を JSON-LD フォーマットの key-values で表した例である。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。  
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
#### I4Submodel NGSI-LD 正規化例  
以下は正規化された JSON-LD フォーマットの I4Submodel の例である。これは、オプションを使用しない場合、NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
