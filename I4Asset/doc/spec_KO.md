<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역 내 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `administration[object]`: 인스턴스 관리 정보  
	- `version[string]`: AAS 버전 번호는 사양 릴리스에 따른 번호입니다.    
- `alternateName[string]`: 이 항목의 대체 이름  
- `billOfMaterialRef[object]`: 복합 자산은 다른 엔티티와 자산으로 구성됩니다. 자산의 일부인 이러한 엔티티와 자산은 자재 명세서에 명시되어 있습니다.  
- `category[string]`: 카테고리는 AAS의 클래스에 대한 추가 메타 정보를 제공하는 값입니다.  
	- `idType[string]`: 식별자 유형(예: IRI 또는 IRD)    
- `kind[string]`: 스키마의 종류. 이것은 인스턴스  
- `name[string]`: 이 항목의 이름  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-NotesYaml -->
<!-- /40-NotesYaml -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

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



<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
