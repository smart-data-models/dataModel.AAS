<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: I4Submodel  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4Submodel/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- No se requieren propiedades  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
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
## Ejemplo de carga útil  
#### I4Submodel NGSI-v2 key-values Ejemplo  
He aquí un ejemplo de un I4Submodel en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### I4Submodel NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de un I4Submodel en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### I4Submodel NGSI-LD key-values Ejemplo  
He aquí un ejemplo de un I4Submodel en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### I4Submodel NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un I4Submodel en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
