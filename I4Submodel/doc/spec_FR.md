<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : I4Submodel  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.AAS/blob/master/I4Submodel/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Selon IDTA-01001-3-0, décrit un composant générique de sous-modèle du Shell d'administration des actifs RAMI4.0**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une voie publique    
- `administration[object]`: Informations sur l'administration du sous-modèle AAS  	- `revision[string]`: Le numéro de révision de l'AAS est le numéro correspondant à la version de la spécification.    
	- `version[string]`: Le numéro de version de l'AAS est le numéro correspondant à la version de la spécification.    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: La catégorie est une valeur qui donne des méta-informations supplémentaires sur la classe de l'élément.  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `descriptions[array]`: Pour ajouter des connaissances détaillées sur l'AAS dans différentes langues  - `hasDataSpecification[array]`: La spécification des données définit les attributs supplémentaires qu'un sous-modèle peut avoir. Spécification RAMI4.0  - `id[*]`: Identifiant unique de l'entité  - `idShort[string]`: short id est le nom (court) du sous-modèle dans l'environnement RAMI40  - `identification[object]`: Identification du sous-modèle dans son AAS. Environnement RAMI4.0  	- `id[uri]`: Information d'identité qui distingue sans ambiguïté un sous-modèle d'un autre -NGSI Id-. Environnement RAMI4.0    
	- `idType[string]`: Type d'identifiant, par exemple IRI ou IRDI    
- `kind[string]`: Pour distinguer le "type" de l'"instance", on utilise le terme "genre".  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `modelType[object]`: Pour la distinction entre "type" et "instance", le terme "genre" est utilisé.  	- `name[string]`: Propriété de l'élément. En général, le sous-modèle est défini pour ce type d'élément.    
- `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `qualifiers[array]`: Les qualificatifs sont utilisés si la sémantique de l'élément est la même indépendamment de ses qualificatifs. Seule la qualité ou la signification de la valeur de l'élément diffère.  - `refI4AASId[string]`: Fait référence au Shell d'administration des actifs racine auquel ce sous-modèle appartient.  - `refI4AssetId[string]`: Fait référence à l'actif racine auquel appartient ce sous-modèle  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `semanticId[object]`: Il renvoie à une source d'information externe qui explique la formulation du sous-modèle.  	- `keys[array]`: Clés pour l'identifiant sémantique    
- `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `submodelElements[array]`: Élément de données comprenant la liste des éléments - opérations ou commandes ET propriétés - I4SubmodelElementOperation pour les commandes RAMI / I4SubmodelElementProperty pour les propriétés RAMI.  - `type[string]`: Il doit s'agir d'un type d'entité RAMI4.0 I4Submodel NGSI pour représenter un composant du sous-modèle de jumeau numérique RAMI4.0 AAS.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### Sous-modèle I4 Valeurs clés de l'INSG-v2 Exemple  
Voici un exemple de sous-modèle I4 au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### I4Submodel NGSI-v2 normalisé Exemple  
Voici un exemple de sous-modèle I4Submodel au format JSON-LD tel qu'il a été normalisé. Il est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### Sous-modèle I4 Valeurs clés NGSI-LD Exemple  
Voici un exemple de sous-modèle I4 au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### I4Submodel NGSI-LD normalisé Exemple  
Voici un exemple de sous-modèle I4Submodel au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
