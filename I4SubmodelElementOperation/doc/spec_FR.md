<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : I4SubmodelElementOperation  
===================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.AAS/blob/master/I4SubmodelElementOperation/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Selon IDTA-01001-3-0, décrit un élément générique du sous-modèle RAMI4.0 représentant une OPERATION (commande) d'un shell d'administration des biens référencé**.  
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: La catégorie est une valeur qui donne des méta-informations supplémentaires sur la classe de l'élément.  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `descriptions[array]`: Pour ajouter des connaissances détaillées sur l'élément dans différentes langues  - `executionState[string]`: L'état du résultat de l'invocation de l'opération  - `hasDataSpecification[array]`: Élément qui peut être étendu à l'aide de modèles de spécification de données. Un modèle de spécification des données définit un ensemble nommé d'attributs supplémentaires qu'un élément peut ou doit avoir. Spécification RAMI4.0  - `id[*]`: Identifiant unique de l'entité  - `idShort[string]`: short id est le nom (court) de l'élément de sous-modèle dans l'environnement RAMI40  - `inoutputVariable[array]`: Tableau contenant les paramètres d'entrée et de sortie de l'opération  - `inputVariable[array]`: Tableau contenant les paramètres d'entrée de l'opération  - `kind[string]`: Pour distinguer le "type" de l'"instance", on utilise le terme "genre".  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `modelType[object]`: Pour distinguer le "type" de l'"instance", on utilise le terme "genre".  	- `name[string]`: Propriété de l'élément. Généralement, l'option -Opération- est définie pour ce type d'élément.    
- `name[string]`: Le nom de cet élément  - `operationResult[object]`: Contient L'objet résultat de l'invocation d'opération avec le résultat retourné d'une invocation d'opération  	- `entity[object]`: Ensemble de propriétés liées aux résultats de l'opération    
	- `entityType[string]`: Type d'entité description/référence    
	- `isException[boolean]`: Vrai s'il s'agit d'une exception    
	- `messages[array]`: Message supplémentaire contenant des informations pour le demandeur    
	- `success[boolean]`: Succès true si l'opération est réussie. Faux si l'opération n'est pas réussie.    
- `outputVariable[array]`: Tableau contenant les paramètres de sortie de l'opération  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `refI4AASId[string]`: Fait référence au Shell d'administration des actifs racine auquel appartient cet élément de sous-modèle.  - `refI4AssetId[string]`: Fait référence à l'actif racine auquel appartient ce SubmodelElement  - `refI4SubmodelId[string]`: Fait référence au sous-modèle racine auquel appartient cet élément de sous-modèle  - `requestId[string]`: ID de la requête du client envoyée -pour INPUT- et/ou la valeur/le statut récupéré(e) -pour OUTPUT-. Utilisé pour suivre les opérations  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `semanticId[object]`: Il renvoie à une source d'information externe qui explique la formulation de l'élément du sous-modèle.  	- `keys[array]`: Clés pour l'identifiant sémantique    
- `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `timeout[number]`: Représente la valeur du délai d'attente pour cette commande communiquée par le serveur OPC-UA.  - `type[string]`: Elle doit être de type RAMI4.0 I4SubmodelElementOperation NGSI Entity pour représenter un composant de sous-modèle de jumelage numérique RAMI4.0 AAS Digital Twin Operation.  <!-- /30-PropertiesList -->  
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
I4SubmodelElementOperation:    
  description: 'Based on IDTA-01001-3-0, describes a generic RAMI4.0 SubmodelElement representing an OPERATION (Command) of a referenced Asset Administration Shell'    
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
    executionState:    
      description: The operation invocation result state    
      enum:    
        - canceled    
        - completed    
        - failed    
        - initiated    
        - running    
        - timeout    
      type: string    
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
        type: Property    
    idShort:    
      description: short id is the (short) name of the SubmodelElement within RAMI40 environment    
      type: string    
      x-ngsi:    
        type: Property    
    inoutputVariable:    
      description: Array with parameters that are input and output of the operation    
      items:    
        description: Defines an inoutput variable for this command request    
        properties:    
          category:    
            description: The category is a value that gives further meta information w.r.t. to the class of the element    
            type: string    
            x-ngsi:    
              type: Property    
          constraints:    
            description: Constraints an inoutput Variable may have. RAMI4.0 Asset Administration Shell specification. Version 3.0RC02    
            items:    
              description: 'Every object containing the constraints '    
              properties:    
                type:    
                  description: 'Link, url, constraint ID (AAS Version 3.0RC02) or description of the constrain to be applied'    
                  type: string    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
            type: array    
            x-ngsi:    
              type: Property    
          descriptions:    
            description: For adding detailed knowledge about the Element in different languages    
            items:    
              description: Every object containing the attributes of the descriptions    
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
              description: Every object containing the descriptions of the data specification    
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
          idShort:    
            description: short id is the (short) name of the inoutput Value -variable name- within RAMI40 environment    
            type: string    
            x-ngsi:    
              type: Property    
          kind:    
            description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
            type: string    
            x-ngsi:    
              type: Property    
          modelType:    
            description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
            properties:    
              name:    
                description: Property of the item    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          value:    
            description: The obtained value in string format    
            type: string    
            x-ngsi:    
              type: Property    
          valueType:    
            description: The value type used in string format    
            properties:    
              dataObjectType:    
                description: 'Property of the item. string, integer, float, num etc. are used set for this type'    
                properties:    
                  name:    
                    description: Property of the item. Object type    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    inputVariable:    
      description: Array with input parameters of the operation    
      items:    
        description: Defines an Input variable for this command request    
        properties:    
          category:    
            description: The category is a value that gives further meta information w.r.t. to the class of the element    
            type: string    
            x-ngsi:    
              type: Property    
          constraints:    
            description: Constraints an Input Variable may have. RAMI4.0 Asset Administration Shell specification. Version 3.0RC02    
            items:    
              description: The object containing the constraints    
              properties:    
                type:    
                  description: 'Link, url, constraint ID (AAS Version 3.0RC02) or description of the constrain to be applied'    
                  type: string    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
            type: array    
            x-ngsi:    
              type: Property    
          descriptions:    
            description: For adding detailed knowledge about the Element in different languages    
            items:    
              description: Every object containing the descriptions properties    
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
              description: Every object containing the attributes of the data specification    
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
          idShort:    
            description: short id is the (short) name of the Input Value -variable name- within RAMI40 environment    
            type: string    
            x-ngsi:    
              type: Property    
          kind:    
            description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
            type: string    
            x-ngsi:    
              type: Property    
          modelType:    
            description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
            properties:    
              name:    
                description: Property of the item. Usually -OperationVariable- is set for this type    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          value:    
            description: The given value in string format    
            type: string    
            x-ngsi:    
              type: Property    
          valueType:    
            description: The value type used in string format    
            properties:    
              dataObjectType:    
                description: 'Property of the item. string, integer, float, num etc. are used set for this type'    
                properties:    
                  name:    
                    description: Property of the item. Object type    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
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
    operationResult:    
      description: Contains The operation invocation result object with the returned result of an operation invocation    
      properties:    
        entity:    
          description: Set of properties linked to the operation results    
          type: object    
          x-ngsi:    
            type: Property    
        entityType:    
          description: Entity type description/reference    
          type: string    
          x-ngsi:    
            type: Property    
        isException:    
          description: True if it is an exception    
          type: boolean    
          x-ngsi:    
            type: Property    
        messages:    
          description: Additional message containing information for the requester    
          items:    
            description: Item object for the messages    
            properties:    
              code:    
                description: Technology-dependent status or error code    
                type: string    
                x-ngsi:    
                  type: Property    
              messageType:    
                description: The message type enum    
                enum:    
                  - error    
                  - exception    
                  - info    
                  - warning    
                type: string    
                x-ngsi:    
                  type: Property    
              text:    
                description: A message containing more information for the requester about a certain happening in the backend    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          type: array    
          x-ngsi:    
            type: Property    
        success:    
          description: Success true if operation succeed. False if not    
          type: boolean    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    outputVariable:    
      description: Array with Output parameters of the operation    
      items:    
        description: Defines an Output variable for this command request    
        properties:    
          category:    
            description: The category is a value that gives further meta information w.r.t. to the class of the element    
            type: string    
            x-ngsi:    
              type: Property    
          constraints:    
            description: Constraints an Output Variable may have. RAMI4.0 Asset Administration Shell specification. Version 3.0RC02    
            items:    
              description: Every object containing the description of the constraints    
              properties:    
                type:    
                  description: 'Link, url, constraint ID (AAS Version 3.0RC02) or description of the constrain to be applied'    
                  type: string    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
            type: array    
            x-ngsi:    
              type: Property    
          descriptions:    
            description: For adding detailed knowledge about the Element in different languages    
            items:    
              description: Every object containing the attributes of the descriptions    
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
              description: Every object containing the details of the data specification    
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
          idShort:    
            description: short id is the (short) name of the Output Value -variable name- within RAMI40 environment    
            type: string    
            x-ngsi:    
              type: Property    
          kind:    
            description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
            type: string    
            x-ngsi:    
              type: Property    
          modelType:    
            description: 'For the distinction of ''type'' and ''instance'', the term ''kind'' is used'    
            properties:    
              name:    
                description: Property of the item. Usually -OperationVariable- is set for this type    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
          value:    
            description: The obtained value in string format    
            type: string    
            x-ngsi:    
              type: Property    
          valueType:    
            description: The value type used in string format    
            properties:    
              dataObjectType:    
                description: 'Property of the item. string, integer, float, num etc. are used set for this type'    
                properties:    
                  name:    
                    description: Property of the item. Object type    
                    type: string    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
            type: object    
            x-ngsi:    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
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
    requestId:    
      description: Client request ID sent -for INPUT- and/or the retrieved value/status -for OUTPUT-. Used to TRACK the operations    
      type: string    
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
    timeout:    
      description: Represents the timeout value for this command reported by the OPC-UA server    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: It has to be RAMI4.0 I4SubmodelElementOperation NGSI Entity type to represent a RAMI4.0 AAS Digital Twin Submodel Operation component    
      enum:    
        - I4SubmodelElementOperation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2023/04/IDTA-01001-3-0_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AAS/blob/master/I4SubmodelElementOperation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.AAS/I4SubmodelElementOperation/schema.json    
  x-model-tags: Corosect    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### I4SubmodelElementOperation Valeurs clés NGSI-v2 Exemple  
Voici un exemple d'une I4SubmodelElementOperation au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4SubmodelElementOperation:OperationalCapability:MRobotExecuteTask:AASMRobotVI",  
  "type": "I4SubmodelElementOperation",  
  "category": "PARAMETER",  
  "descriptions": [  
    {  
      "language": "en",  
      "text": "Submodel operational capability [contains various data related to the operation capability of sensor]"  
    }  
  ],  
  "executionState": "initiated",  
  "hasDataSpecification": [],  
  "idShort": "MRobotExecuteTask",  
  "inoutputVariable": [],  
  "inputVariable": [  
    {  
      "value": "review",  
      "constraints": [],  
      "hasDataSpecification": [],  
      "idShort": "TaskID",  
      "category": "CONSTANT",  
      "valueType": {  
        "dataObjectType": {  
          "name": "arg.DataType"  
        }  
      },  
      "kind": "Instance",  
      "descriptions": [  
        {  
          "language": "en",  
          "text": "To give the task id to be executed"  
        }  
      ],  
      "modelType": {  
        "name": "OperationVariable"  
      }  
    }  
  ],  
  "kind": "Instance",  
  "modelType": {  
    "name": "Operation"  
  },  
  "operationResult": {  
    "success": true,  
    "isException": false,  
    "entity": {},  
    "entityType": "string",  
    "messages": [  
      {  
        "messageType": "info",  
        "text": "no message text",  
        "code": "no code"  
      }  
    ]  
  },  
  "outputVariable": [  
    {  
      "value": "review",  
      "constraints": [],  
      "hasDataSpecification": [],  
      "idShort": "CommandStatus",  
      "category": "CONSTANT",  
      "valueType": {  
        "dataObjectType": {  
          "name": "arg.DataType"  
        }  
      },  
      "kind": "Instance",  
      "descriptions": [  
        {  
          "language": "en",  
          "text": "To let the the service consumer know that the command has been received and will be processed"  
        }  
      ],  
      "modelType": {  
        "name": "OperationVariable"  
      }  
    }  
  ],  
  "refI4AASId": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
  "refI4AssetId": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
  "refI4SubmodelId": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AASMRobotVI",  
  "requestId": "review",  
  "semanticId": {  
    "keys": [  
      {  
        "type": "Submodel",  
        "local": false,  
        "value": "",  
        "index": 0,  
        "idType": ""  
      }  
    ]  
  },  
  "timeout": 0  
}  
```  
</details>  
#### I4SubmodelElementOperation NGSI-v2 normalisée Exemple  
Voici un exemple d'une I4SubmodelElementOperation au format JSON-LD telle que normalisée. Cette opération est compatible avec la NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-v2:RAMI40:I4SubmodelElementOperation:OperationalCapability:drop:AGV1",  
    "type": "I4SubmodelElementOperation",  
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
                "text": "Request the AGV to drop a load"  
            }  
        ],  
        "metadata": {}  
    },  
    "hasDataSpecification": {  
        "type": "StructuredValue",  
        "value": "None",  
        "metadata": {}  
    },  
    "idShort": {  
        "type": "Text",  
        "value": "drop",  
        "metadata": {}  
    },  
    "inoutputVariable": {  
        "type": "StructuredValue",  
        "value": [],  
        "metadata": {}  
    },  
    "inputVariable": {  
        "type": "StructuredValue",  
        "value": [  
            {  
                "value": "EURO",  
                "idShort": "loadType"  
            },  
            {  
                "value": "1",  
                "idShort": "loadId"  
            },  
            {  
                "value": "0",  
                "idShort": "height"  
            },  
            {  
                "value": "0",  
                "idShort": "depth"  
            },  
            {  
                "value": "0",  
                "idShort": "side"  
            }  
        ],  
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
            "name": "Operation"  
        },  
        "metadata": {}  
    },  
    "operationResult": {  
        "type": "StructuredValue",  
        "value": {},  
        "metadata": {}  
    },  
    "outputVariable": {  
        "type": "StructuredValue",  
        "value": [  
            {  
                "value": "",  
                "idShort": "CommandStatus"  
            }  
        ],  
        "metadata": {}  
    },  
    "refI4AASId": {  
        "type": "Text",  
        "value": "urn:ngsi-v2:RAMI40:I4AAS:AGV:AGV1",  
        "metadata": {}  
    },  
    "refI4AssetId": {  
        "type": "Text",  
        "value": "urn:ngsi-v2:RAMI40:I4Asset:AGV:AGV1",  
        "metadata": {}  
    },  
    "refI4SubmodelId": {  
        "type": "Text",  
        "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AGV1",  
        "metadata": {}  
    },  
    "requestId": {  
        "type": "Text",  
        "value": "3b85ce8a-e8dd-4918-b327-c049e7b3d127",  
        "metadata": {}  
    },  
    "semanticId": {  
        "type": "StructuredValue",  
        "value": {  
            "keys": []  
        },  
        "metadata": {}  
    },  
    "timeout": {  
        "type": "Number",  
        "value": 0,  
        "metadata": {}  
    },  
    "valueId": {  
        "type": "Text",  
        "value": "unused",  
        "metadata": {}  
    }  
}  
```  
</details>  
#### I4SubmodelElementOperation Valeurs clés NGSI-LD Exemple  
Voici un exemple d'une I4SubmodelElementOperation au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4SubmodelElementOperation:OperationalCapability:MRobotExecuteTask:AASMRobotVI",  
  "type": "I4SubmodelElementOperation",  
  "category": "PARAMETER",  
  "descriptions": [  
    {  
      "language": "en",  
      "text": "Submodel operational capability [contains various data related to the operation capability of sensor]"  
    }  
  ],  
  "executionState": "initiated",  
  "hasDataSpecification": [],  
  "idShort": "MRobotExecuteTask",  
  "inoutputVariable": [],  
  "inputVariable": [  
    {  
      "value": "review",  
      "hasDataSpecification": [],  
      "idShort": "TaskID",  
      "category": "CONSTANT",  
      "valueType": {  
        "dataObjectType": {  
          "name": "arg.DataType"  
        }  
      },  
      "kind": "Instance",  
      "descriptions": [  
        {  
          "language": "en",  
          "text": "To give the task id to be executed"  
        }  
      ],  
      "modelType": {  
        "name": "OperationVariable"  
      }  
    }  
  ],  
  "kind": "Instance",  
  "modelType": {  
    "name": "Operation"  
  },  
  "operationResult": {  
    "success": true,  
    "isException": false,  
    "entity": {},  
    "entityType": "string",  
    "messages": [  
      {  
        "messageType": "info",  
        "text": "no message text",  
        "code": "no code"  
      }  
    ]  
  },  
  "outputVariable": [  
    {  
      "value": "review",  
      "hasDataSpecification": [],  
      "idShort": "CommandStatus",  
      "category": "CONSTANT",  
      "valueType": {  
        "dataObjectType": {  
          "name": "arg.DataType"  
        }  
      },  
      "kind": "Instance",  
      "descriptions": [  
        {  
          "language": "en",  
          "text": "To let the the service consumer know that the command has been received and will be processed"  
        }  
      ],  
      "modelType": {  
        "name": "OperationVariable"  
      }  
    }  
  ],  
  "refI4AASId": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
  "refI4AssetId": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
  "refI4SubmodelId": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AASMRobotVI",  
  "requestId": "review",  
  "semanticId": {  
    "keys": [  
      {  
        "type": "Submodel",  
        "local": false,  
        "value": "",  
        "index": 0,  
        "idType": ""  
      }  
    ]  
  },  
  "timeout": 0,  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.AAS/context.jsonld"  
  ]  
}  
```  
</details>  
#### I4SubmodelElementOperation NGSI-LD normalisé Exemple  
Voici un exemple d'une I4SubmodelElementOperation au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4SubmodelElementOperation:OperationalCapability:drop:AGV1",  
  "type": "I4SubmodelElementOperation",  
  "category": {  
    "type": "Property",  
    "value": "CONSTANT"  
  },  
  "descriptions": {  
    "type": "Property",  
    "value": [  
      {  
        "language": "en",  
        "text": "Request the AGV to drop a load"  
      }  
    ]  
  },  
  "hasDataSpecification": {  
    "type": "Property",  
    "value": "None"  
  },  
  "idShort": {  
    "type": "Property",  
    "value": "drop"  
  },  
  "inoutputVariable": {  
    "type": "Property",  
    "value": []  
  },  
  "inputVariable": {  
    "type": "Property",  
    "value": [  
      {  
        "value": "EURO",  
        "idShort": "loadType"  
      },  
      {  
        "value": "1",  
        "idShort": "loadId"  
      },  
      {  
        "value": "0",  
        "idShort": "height"  
      },  
      {  
        "value": "0",  
        "idShort": "depth"  
      },  
      {  
        "value": "0",  
        "idShort": "side"  
      }  
    ]  
  },  
  "kind": {  
    "type": "Property",  
    "value": "Instance"  
  },  
  "modelType": {  
    "type": "Property",  
    "value": {  
      "name": "Operation"  
    }  
  },  
  "operationResult": {  
    "type": "Property",  
    "value": {}  
  },  
  "outputVariable": {  
    "type": "Property",  
    "value": [  
      {  
        "value": "",  
        "idShort": "CommandStatus"  
      }  
    ]  
  },  
  "refI4AASId": {  
    "type": "Property",  
    "value": "urn:ngsi-v2:RAMI40:I4AAS:AGV:AGV1"  
  },  
  "refI4AssetId": {  
    "type": "Property",  
    "value": "urn:ngsi-v2:RAMI40:I4Asset:AGV:AGV1"  
  },  
  "refI4SubmodelId": {  
    "type": "Property",  
    "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AGV1"  
  },  
  "requestId": {  
    "type": "Property",  
    "value": "3b85ce8a-e8dd-4918-b327-c049e7b3d127"  
  },  
  "semanticId": {  
    "type": "Property",  
    "value": {  
      "keys": []  
    }  
  },  
  "timeout": {  
    "type": "Property",  
    "value": 0  
  },  
  "valueId": {  
    "type": "Property",  
    "value": "unused"  
  }  
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
