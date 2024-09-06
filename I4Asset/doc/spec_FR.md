<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : I4Asset  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.AAS/blob/master/I4Asset/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Selon IDTA-01001-3-0, définit l'instance d'actif liée à un AAS donné, un composant générique du Shell d'administration des actifs (AAS) de RAMI4.0**.  
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
- `administration[object]`: Informations sur l'administration de l'instance  	- `revision[string]`: Le numéro de révision de l'AAS est le numéro correspondant à la version de la spécification.    
	- `version[string]`: Le numéro de version de l'AAS est le numéro correspondant à la version de la spécification.    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `assetIdentificationModelRef[object]`: Un bien peut généralement être représenté par plusieurs propriétés d'identification différentes, comme par exemple son numéro de série, son code RFID, etc. Ces propriétés d'identification locales sont définies dans le sous-modèle d'identification des biens.  	- `keys[array]`: clés pour l'instance de l'actif    
- `billOfMaterialRef[object]`: Un bien complexe est composé d'autres entités et biens. Ces entités et biens faisant partie du bien sont spécifiés dans la nomenclature.  	- `keys[array]`: Clés pour l'identifiant sémantique    
- `category[string]`: La catégorie est une valeur qui donne des méta-informations supplémentaires sur la classe du SAA.  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `descriptions[array]`: Pour ajouter des connaissances détaillées dans différentes langues  - `hasDataSpecification[array]`: La spécification des données définit les attributs supplémentaires qu'un bien peut avoir. Spécification RAMI4.0  - `id[*]`: Identifiant unique de l'entité  - `idShort[string]`: Identifiant court (nom) de l'instance RAMI  - `identification[object]`: Identification de l'objet AAS -Asset- Instance  	- `id[uri]`: Informations sur l'identité qui distinguent sans ambiguïté une instance de RAMI d'une autre    
	- `idType[string]`: Type d'identifiant, par exemple IRI ou IRD    
- `kind[string]`: Type de schéma. Ceci est limité à l'instance  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `modelType[object]`: Type de modèle d'instance selon IDTA  	- `name[string]`: Type de l'élément référencé    
- `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `type[string]`: Il doit s'agir d'un type d'entité RAMI4.0 I4Asset NGSI  <!-- /30-PropertiesList -->  
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
## Exemples de charges utiles  
#### I4Asset NGSI-v2 valeurs-clés Exemple  
Voici un exemple d'un I4Asset au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### I4Asset NGSI-v2 normalisé Exemple  
Voici un exemple d'un I4Asset au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### I4Asset NGSI-LD key-values Exemple  
Voici un exemple d'un I4Asset au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### I4Asset NGSI-LD normalisé Exemple  
Voici un exemple d'un I4Asset au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
