<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : I4SubmodelElementRelationship  
======================================<!-- /10-Header -->  
<!-- 15-License -->  
Licence ouverte  
Document généré automatiquement : https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Basé sur IDTA-01001-3-0, décrit un sous-élément RAMI4.0 SubmodelElement générique représentant une relation d'un Shell d'Administration d'Actifs référencé.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  
Liste des propriétés  
<sup><sub>[*] Si aucun type n'est défini dans un attribut, cela peut être dû à plusieurs types ou à des formats/patterns différents</sub></sup>  
- `address[object]`: L'adresse de livraison  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne.  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Le lieu où l'adresse de la rue est, et qui se trouve dans la région.  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région où se situe la localité, et qui est dans le pays.  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est une forme de division administrative qui, dans certains pays, est gérée par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de boîte postale pour les adresses PO. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Le numéro d'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Identifiant d'une propriété spécifique sur une rue publique    
- `alternateName[string]`: Une autre dénomination pour cet article  - `areaServed[string]`: La zone géographique où un service ou un article proposé est fourni.  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: La catégorie est une valeur qui donne des informations supplémentaires concernant la classe de l'élément.  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisée  - `dateCreated[date-time]`: Timestamp de création de l'entité. Cela sera généralement alloué par la plateforme de stockage.  - `dateModified[date-time]`: Timestamp de la dernière modification de l'entité. Cela sera généralement alloué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `descriptions[array]`: Pour ajouter des connaissances détaillées sur l'élément dans différentes langues.  - `first[string]`: Le fait fait référence au premier élément de référence du élément de relation.  - `hasDataSpecification[array]`: Template de spécification de données pouvant être étendus en utilisant des modèles de spécification de données. Un modèle de spécification de données définit un ensemble de caractéristiques supplémentaires qu'un élément peut ou doit avoir. RAMI4.0 spécification  - `id[*]`: Identifiant unique de l'entité  - `idShort[string]`: L'ID court est le (court) nom du SubmodelElement à l'intérieur de l'environnement RAMI40.  - `kind[string]`: Pour la distinction entre 'type' et 'instance', le terme 'kind' est utilisé.  - `location[*]`: Référence Géospatiale à l'élément. Elle peut être un Point, une LigneString, un Polygone, un Point MultiPoint, un LigneString MultiPoint, ou un Polygone MultiPoint.  - `modelType[object]`: Pour la distinction entre 'type' et 'instance', le terme 'kind' est utilisé.  	- `name[string]`: Propriété de l'élément. Généralement -Operation- est définie pour ce type.    
- `name[string]`: Le nom de cet article  - `owner[array]`: Une liste contenant une séquence encodée en JSON d'une chaîne de caractères unique faisant référence aux identifiants uniques des propriétaires.  - `refI4AASId[string]`: Le document fait référence à la sous-structure d'administration racine de l'Asset Administration Shell auquel appartient ce SousmodelElement.  - `refI4AssetId[string]`: Le fait fait référence à la racine de l'élément SubmodelElement auquel il appartient.  - `second[string]`: Le deuxième élément de référence du élément de relation.  - `seeAlso[*]`: liste d'URI pointant vers des ressources supplémentaires concernant l'élément  - `semanticId[object]`: Il se réfère à une source d'information externe, qui explique la formulation de l'élément de sous-modèle.  	- `keys[array]`: Clés pour l'ID sémantique    
- `source[string]`: Une séquence de caractères donnant l'origine du flux de données de l'entité comme une URL. Il est recommandé d'être le nom de domaine entièrement qualifié du fournisseur de source, ou l'URL vers l'objet source.  - `type[string]`: Il doit être RAMI4.0 I4SubmodelElementRelationship NGSI Entité de type pour représenter un élément RAMI4.0 AAS Digital Twin Submodel Relationship  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requis  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Description du modèle de données des propriétés  
Triés par ordre alphabétique (cliquez pour plus de détails)  
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
Exemples de payloads  
#### I4SubmodelElementRelationship NGSI-v2 key-values Example '  
Voici un exemple d'un I4SubmodelElementRelationship dans le format JSON-LD comme clé-valeur. Il est compatible avec NGSI-v2 lorsque `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### I4SubmodelElementRelationship NGSI-v2 normalized Example '  
Voici un exemple d'un I4SubmodelElementRelationship dans le format JSON-LD normalisé. Il est compatible avec NGSI-v2 lorsque les options ne sont pas utilisées et renvoie les données de contexte d'une entité individuelle.  
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
#### I4SubmodelElementRelationship NGSI-LD clé-valeurs Exemple '  
Voici un exemple d'un I4SubmodelElementRelationship dans le format JSON-LD comme clé-valeur. Il est compatible avec NGSI-LD lorsque `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### Relation entre les éléments du sous-modèle I4Submodel NGSI-LD Exemple  
Voici un exemple d'un I4SubmodelElementRelationship dans le format JSON-LD normalisé. Il est compatible avec NGSI-LD lorsque les options ne sont pas utilisées et renvoie les données de contexte d'une entité individuelle.  
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
Consultez [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour en savoir plus sur la façon de gérer les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
