<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: I4SubmodelElementCapability  
====================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia Abierta](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4SubmodelElementCapability/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Basado en IDTA-01001-3-0, describe un SubmodelElement RAMI4.0 genérico que representa una Capability de un Asset Administration Shell referenciado**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque podría tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, es gestionada por el gobierno local.    
	- `postOfficeBoxNumber[string]`: El número de apartado postal para las direcciones de apartado de correos. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: La dirección postal  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Número que identifica una propiedad específica en una calle pública    
- `alternateName[string]`: Un nombre alternativo para este ítem  - `areaServed[string]`: El área geográfica donde se proporciona un servicio o un artículo ofrecido  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: La categoría es un valor que proporciona metainformación adicional con respecto a la clase del elemento.  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Timestamp de creación de la entidad. Normalmente, este será asignado por la plataforma de almacenamiento.  - `dateModified[date-time]`: Timestamp de la última modificación de la entidad. Esto normalmente se asignará por la plataforma de almacenamiento.  - `description[string]`: Error: Translation failed after 60 attempt(s). Last reason: 404 NOT_FOUND. {'error': {'code': 404, 'message': 'models/gemini-2.5-flash-native-audio-preview-09-2025 is not found for API version v1beta, or is not supported for generateContent. Call ListModels to see the list of available models and their supported methods.', 'status': 'NOT_FOUND'}}  - `descriptions[array]`: Para añadir conocimiento detallado sobre el Elemento en diferentes idiomas  - `hasDataSpecification[array]`: Element que puede ser extendido utilizando plantillas de especificación de datos. Una plantilla de especificación de datos define un conjunto de atributos adicionales nombrados que un elemento puede o debe tener. RAMI4.0 especificación  - `id[*]`: Error: Translation failed after 60 attempt(s). Last reason: 404 NOT_FOUND. {'error': {'code': 404, 'message': 'models/gemini-2.5-flash-native-audio-preview-09-2025 is not found for API version v1beta, or is not supported for generateContent. Call ListModels to see the list of available models and their supported methods.', 'status': 'NOT_FOUND'}}  - `idShort[string]`: El identificador corto es el nombre (corto) del SubmodelElement dentro del entorno RAMI40.  - `kind[string]`: Para la distinción entre 'tipo' e 'instancia', se utiliza el término 'clase'.  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `modelType[object]`: Para la distinción entre 'tipo' e 'instancia', se utiliza el término 'clase'.  	- `name[string]`: Propiedad del elemento. Normalmente, para este tipo se establece -Capability-.    
- `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres con codificación JSON que hacen referencia a los identificadores únicos del/de los propietario(s)  - `refI4AASId[string]`: Hace referencia al Asset Administration Shell raíz al que pertenece este SubmodelElement  - `refI4AssetId[string]`: Hace referencia al Activo raíz al que pertenece este SubmodeloElemento  - `refI4SubmodelId[string]`: Hace referencia al Submodelo raíz al que pertenece este SubmodeloElemento  - `seeAlso[*]`: lista de URI que apuntan a recursos adicionales sobre el artículo  - `semanticId[object]`: Se refiere a una fuente de información externa, que explica la formulación del elemento del submodelo.  	- `keys[array]`: Claves para el ID semántico    
- `source[string]`: Una secuencia de caracteres que proporciona la fuente original de los datos de la entidad como una URL. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL al objeto fuente.  - `type[string]`: Debe ser un tipo de entidad NGSI RAMI4.0 I4SubmodelElementCapability para representar un componente de capacidad de Submodelo de Gemelo Digital AAS RAMI4.0  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenado alfabéticamente (haga clic para detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
I4SubmodelElementCapability:    
  description: 'Based on IDTA-01001-3-0, describes a generic RAMI4.0 SubmodelElement representing an Capability of a referenced Asset Administration Shell'    
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
          description: Property of the item. Usually -Capability- is set for this type    
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
    refI4SubmodelId:    
      description: References the root Submodel which this SubmodelElement belongs to    
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
      description: It has to be RAMI4.0 I4SubmodelElementCapability NGSI Entity type to represent a RAMI4.0 AAS Digital Twin Submodel Capability component    
      enum:    
        - I4SubmodelElementCapability    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2023/04/IDTA-01001-3-0_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AAS/blob/master/I4SubmodelElementCapability/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.AAS/I4SubmodelElementCapability/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplos de cargas útiles  
#### I4SubmodelElementCapability NGSI-v2 clave-valores Ejemplo  
Aquí hay un ejemplo de un I4SubmodelElementCapability en formato JSON-LD como pares clave-valor. Esto es compatible con NGSI-v2 cuando se usa `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RAMI40:I4SubmodelElementCapability:OperationManagementAgent:PlanOperation",  
  "type": "I4SubmodelElementCapability",  
  "descriptions": [  
      {  
          "language": "en",  
          "text": "Submodel capability [contains various data related to the capability of an intelligent agent]"  
      }  
  ],    
  "hasDataSpecification": [],  
  "idShort": "OperationManagementAgent:PlanOperation",  
  "category": "PARAMETER",  
  "kind": "Instance",  
  "modelType": {  
      "name": "Capability"  
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
  "refI4SubmodelId": "urn:ngsi-ld:RAMI40:I4Submodel:OperationManagementAgent:Capabilities"  
}  
```  
</details>  
I4SubmodelElementCapability NGSI-v2 Ejemplo normalizado  
Aquí hay un ejemplo de un I4SubmodelElementCapability en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RAMI40:I4SubmodelElementCapability:OperationManagementAgent:PlanOperation",  
  "type": "I4SubmodelElementCapability",  
  "descriptions": {  
      "type": "Property",  
      "value": [  
       {  
          "language": "en",  
          "text": "Submodel capability [contains various data related to the capability of an intelligent agent]"  
       }  
    ]  
  },    
  "hasDataSpecification": {  
    "type": "Property",  
    "value": "None"  
  },  
  "idShort": {  
    "type": "Property",  
    "value": "I4SubmodelElementCapability:OperationManagementAgent:PlanOperation"  
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
      "name": "Capability"  
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
  "refI4SubmodelId":   
  {  
    "type": "Property",  
    "value": "urn:ngsi-ld:RAMI40:I4Submodel:OperationManagementAgent:Capabilities"  
  }  
}  
```  
</details>  
Ejemplo de pares clave-valor NGSI-LD para I4SubmodelElementCapability  
Aquí hay un ejemplo de una I4SubmodelElementCapability en formato JSON-LD como pares clave-valor. Esto es compatible con NGSI-LD cuando se usa `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RAMI40:I4SubmodelElementCapability:OperationManagementAgent:PlanOperation",  
  "type": "I4SubmodelElementCapability",  
  "descriptions": [  
      {  
          "language": "en",  
          "text": "Submodel capability [contains various data related to the capability of an intelligent agent]"  
      }  
  ],    
  "hasDataSpecification": [],  
  "idShort": "I4SubmodelElementCapability:OperationManagementAgent:PlanOperation",  
  "category": "PARAMETER",  
  "kind": "Instance",  
  "modelType": {  
      "name": "Capability"  
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
  "refI4SubmodelId": "urn:ngsi-ld:RAMI40:I4Submodel:OperationManagementAgent:Capabilities",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]    
}  
```  
</details>  
#### I4SubmodelElementCapability NGSI-LD Ejemplo normalizado  
Aquí hay un ejemplo de una I4SubmodelElementCapability en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:RAMI40:I4SubmodelElementCapability:OperationManagementAgent:PlanOperation",  
  "type": "I4SubmodelElementCapability",  
  "descriptions": {  
      "type": "Property",  
      "value": [  
       {  
          "language": "en",  
          "text": "Submodel capability [contains various data related to the capability of an intelligent agent]"  
       }  
    ]  
  },    
  "hasDataSpecification": {  
    "type": "Property",  
    "value": "None"  
  },  
  "idShort": {  
    "type": "Property",  
    "value": "I4SubmodelElementCapability:OperationManagementAgent:PlanOperation"  
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
      "name": "Capability"  
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
  "refI4SubmodelId":   
  {  
    "type": "Property",  
    "value": "urn:ngsi-ld:RAMI40:I4Submodel:OperationManagementAgent:Capabilities"  
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
Consulte [Pregunta frecuente 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo manejar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
