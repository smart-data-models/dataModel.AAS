<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: I4Submodel  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4Submodel/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Basato su IDTA-01001-3-0, descrive un componente generico del sottomodello della RAMI4.0 Asset Administration Shell**.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica    
- `administration[object]`: Informazioni sull'amministrazione del sottomodello AAS  	- `revision[string]`: Il numero di revisione AAS è il numero in linea con il rilascio della specifica.    
	- `version[string]`: Il numero di versione AAS è il numero in linea con il rilascio della specifica.    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: La categoria è un valore che fornisce ulteriori metainformazioni sulla classe dell'elemento.  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `descriptions[array]`: Per aggiungere conoscenze dettagliate sull'AAS in diverse lingue  - `hasDataSpecification[array]`: La specifica dei dati definisce gli attributi aggiuntivi che un Sottomodello può avere. Specifiche RAMI4.0  - `id[*]`: Identificatore univoco dell'entità  - `idShort[string]`: short id è il nome (breve) del sottomodello all'interno dell'ambiente RAMI40  - `identification[object]`: Identificazione del sottomodello all'interno del suo AAS. Ambiente RAMI4.0  	- `id[uri]`: Informazioni sull'identità che distinguono senza ambiguità un Sottomodello da un altro -NGSI Id-. Ambiente RAMI4.0    
	- `idType[string]`: Tipo di identificatore, ad es. IRI o IRDI    
- `kind[string]`: Per la distinzione tra "tipo" e "istanza", si usa il termine "tipo".  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `modelType[object]`: Per la distinzione tra "tipo" e "istanza" si usa il termine "tipo".  	- `name[string]`: Proprietà dell'elemento. Di solito per questo tipo viene impostato Submodel.    
- `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `qualifiers[array]`: I qualificatori vengono utilizzati se la semantica dell'elemento è la stessa indipendentemente dai suoi qualificatori. È solo la qualità o il significato del valore dell'elemento a differire.  - `refI4AASId[string]`: Riferimenti all'Asset Administration Shell principale a cui appartiene questo sottomodello  - `refI4AssetId[string]`: Riferimenti all'asset principale a cui appartiene questo sottomodello  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `semanticId[object]`: Fa riferimento a una fonte di informazione esterna, che spiega la formulazione del sottomodello.  	- `keys[array]`: Chiavi per l'ID semantico    
- `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `submodelElements[array]`: Elemento di dati che include l'elenco degli elementi -operazioni o comandi e proprietà- I4SubmodelElementOperation per i comandi RAMI / I4SubmodelElementProperty per le proprietà RAMI.  - `type[string]`: Deve essere di tipo Entità RAMI4.0 I4Submodel NGSI per rappresentare un componente del sottomodello RAMI4.0 AAS Digital Twin.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempi di payload  
#### I4Submodel NGSI-v2 valori-chiave Esempio  
Ecco un esempio di I4Submodel in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### I4Submodel NGSI-v2 normalizzato Esempio  
Ecco un esempio di I4Submodel in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano le opzioni e restituisce i dati di contesto di una singola entità.  
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
#### I4Submodel NGSI-LD valori-chiave Esempio  
Ecco un esempio di I4Submodel in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### I4Submodello NGSI-LD normalizzato Esempio  
Ecco un esempio di I4Submodel in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
