<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: I4AAS  
=============<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4AAS/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Basato su IDTA-01001-3-0, descrive un albero generico di Asset Administration Shell - AAS, componente di RAMI4.0**.  
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
- `administration[object]`: Informazioni sull'amministrazione dell'AAS  	- `revision[string]`: Il numero di revisione AAS è il numero in linea con il rilascio della specifica.    
	- `version[string]`: Il numero di versione AAS è il numero in linea con il rilascio della specifica.    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `asset[object]`: La descrizione dell'asset viene compilata qui  	- `keys[array]`: Chiavi per l'asset    
- `category[string]`: La categoria è un valore che fornisce ulteriori metainformazioni sulla classe dell'elemento.  - `conceptDictionaries[array]`: L'Asset stesso può anche definire un proprio dizionario che contiene le definizioni semantiche degli elementi del suo sottomodello. Queste definizioni semantiche sono chiamate descrizioni di concetti (ConceptDescription o dizionario dei concetti). Questo array conterrà gli id dei concetti specifici di RAMI4.0 utilizzati in questo modello.  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `descriptions[array]`: Per aggiungere conoscenze dettagliate sull'AAS in diverse lingue  - `hasDataSpecification[array]`: La specifica dei dati definisce gli attributi aggiuntivi che un asset può avere. Specifiche RAMI4.0  - `id[*]`: Identificatore univoco dell'entità  - `idShort[string]`: short id è il nome (breve) della SHELL DI AMMINISTRAZIONE DELLE ASSET  - `identification[object]`: Identificazione dell'AAS per l'asset. Ambiente RAMI4.0  	- `id[uri]`: Informazioni sull'identità che distinguono senza ambiguità un AAS da un altro. Ambiente RAMI4.0    
	- `idType[string]`: Tipo di identificatore, ad es. IRI o IRDI    
- `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `modelType[object]`: Per la distinzione tra "tipo" e "istanza", si usa il termine "tipo".  	- `name[string]`: Descrizione della proprietà di riferimento dell'elemento    
- `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `refI4AssetId[uri]`: Riferimenti all'asset principale collegato a questo AAS  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `submodels[array]`: AAS contiene un insieme complesso di informazioni, i sottomodelli forniscono una categoria separata per questi dati complessi.  - `type[string]`: Deve essere di tipo Entità RAMI4.0 I4AAS NGSI per rappresentare un gemello digitale RAMI4.0 AAS.  <!-- /30-PropertiesList -->  
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
I4AAS:    
  description: 'Based on IDTA-01001-3-0, describes a generic Asset Administration Shell - AAS - tree, component of the RAMI4.0'    
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
      description: AAS administration information    
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
      required:    
        - version    
        - revision    
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
    asset:    
      description: The Asset descripton is filled here    
      properties:    
        keys:    
          description: Keys for the Asset    
          items:    
            - properties:    
                idType:    
                  description: 'Property. Type of the Identifier, eg.IRI or IRDI'    
                  type: string    
                index:    
                  description: Property. Index encodes the position in the original sequence    
                  type: integer    
                local:    
                  description: Property. It defines whether the asset is created locally or globally    
                  type: boolean    
                type:    
                  description: Property. Type (description) of the asset    
                  enum:    
                    - Asset    
                  type: string    
                value:    
                  description: Property. Here comes the id pointing to the definition of asset    
                  type: string    
              required:    
                - type    
                - local    
                - value    
                - index    
                - idType    
              type: object    
          type: array    
          x-ngsi:    
            type: Property    
      required:    
        - keys    
      type: object    
      x-ngsi:    
        type: Property    
    category:    
      description: The category is a value that gives further meta information w.r.t. to the class of the element    
      type: string    
      x-ngsi:    
        type: Property    
    conceptDictionaries:    
      description: The Asset itself can also define its own dictionary that contains semantic definitions of its submodel elements. These semantic definitions are called concept descriptions (ConceptDescription or concept dictionary). This array will contain ref ids to RAMI4.0 specific concepts used within this model    
      items:    
        properties:    
          type:    
            description: 'Link, url, reference or description of the specified I4.0 concept'    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
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
      description: For adding detailed knowldedge about the AAS in different languages    
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
        required:    
          - language    
          - text    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    hasDataSpecification:    
      description: Data specification defines the additional attributes an asset may have. RAMI4.0 specification    
      items:    
        properties:    
          type:    
            description: 'Link, url or descriptionof the specified data'    
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
      description: short id is the (short) name of the ASSET ADMINISTRATION SHELL    
      type: string    
      x-ngsi:    
        type: Property    
    identification:    
      description: Identification of the AAS for the asset. RAMI4.0 environment    
      properties:    
        id:    
          description: 'Identity information that unambiguously distinguishes one AAS from another one. RAMI4.0 environmet '    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        idType:    
          description: 'Type of the Identifier, eg.IRI or IRDI'    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - idType    
        - id    
      type: object    
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
          description: Description of the referenced property of the item    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - name    
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
    refI4AssetId:    
      description: References the root Asset linked to this AAS    
      format: uri    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    submodels:    
      description: 'AAS contains complex set of informations, submodels provide a separate category for this complex data'    
      items:    
        description: It clearly identify the attribute of data    
        properties:    
          keys:    
            description: keys for the submodel    
            items:    
              properties:    
                idType:    
                  description: Identity information that unambiguously distinguishes one submodel from another one. Can be IRI or IRDI    
                  type: string    
                  x-ngsi:    
                    type: Property    
                index:    
                  description: Index encodes the position in the original sequence    
                  type: number    
                  x-ngsi:    
                    type: Property    
                local:    
                  description: It defines whether the submodel is created locally or globally    
                  type: boolean    
                  x-ngsi:    
                    type: Property    
                type:    
                  description: Type (description) of the submodel    
                  enum:    
                    - Submodel    
                  type: string    
                  x-ngsi:    
                    type: Property    
                value:    
                  description: The id of the submodel pointing to the definition of the Submodel    
                  type: string    
                  x-ngsi:    
                    type: Property    
              required:    
                - type    
                - local    
                - value    
                - index    
                - idType    
              type: object    
            type: array    
            x-ngsi:    
              type: Property    
        required:    
          - keys    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: It has to be RAMI4.0 I4AAS NGSI Entity type to represent a RAMI4.0 AAS Digital Twin    
      enum:    
        - I4AAS    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2023/04/IDTA-01001-3-0_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AAS/blob/master/I4AAS/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.AAS/I4AAS/schema.json    
  x-model-tags: Corosect    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### Valori chiave I4AAS NGSI-v2 Esempio  
Ecco un esempio di I4AAS in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
  "type": "I4AAS",  
  "administration": {  
    "version": "1.0",  
    "revision": "1.0"  
  },  
  "asset": {  
    "keys": [  
      {  
        "type": "Asset",  
        "local": true,  
        "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
        "index": 0,  
        "idType": "IRI"  
      }  
    ]  
  },  
  "category": "CONSTANT",  
  "conceptDictionaries": [],  
  "descriptions": [  
    {  
      "language": "en",  
      "text": "AAS of AASMRobotVI"  
    }  
  ],  
  "hasDataSpecification": [],  
  "idShort": "AASMRobotVI",  
  "identification": {  
    "idType": "IRI",  
    "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI"  
  },  
  "modelType": {  
    "name": "AssetAdministrationShell"  
  },  
  "refI4AssetId": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
  "submodels": [  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:AssetConditionMonitoring:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:Nameplate:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalData:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    }  
  ]  
}  
```  
</details>  
#### I4AAS NGSI-v2 normalizzato Esempio  
Ecco un esempio di I4AAS in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
  "type": "I4AAS",  
  "administration": {  
    "type": "StructuredValue",  
    "value": {  
      "version": "1.0",  
      "revision": "1.0"  
    }  
  },  
  "asset": {  
    "type": "StructuredValue",  
    "value": {  
      "keys": [  
        {  
          "type": "Asset",  
          "local": true,  
          "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    }  
  },  
  "category": {  
    "type": "Text",  
    "value": "CONSTANT"  
  },  
  "conceptDictionaries": {  
    "type": "array",  
    "value": []  
  },  
  "descriptions": {  
    "type": "array",  
    "value": [  
      {  
        "language": "en",  
        "text": "AAS of AASMRobotVI"  
      }  
    ]  
  },  
  "hasDataSpecification": {  
    "type": "array",  
    "value": []  
  },  
  "idShort": {  
    "type": "Text",  
    "value": "AASMRobotVI"  
  },  
  "identification": {  
    "type": "StructuredValue",  
    "value": {  
      "idType": "IRI",  
      "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI"  
    }  
  },  
  "modelType": {  
    "type": "StructuredValue",  
    "value": {  
      "name": "AssetAdministrationShell"  
    }  
  },  
  "refI4AssetId": {  
    "type": "Text",  
    "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI"  
  },  
  "submodels": {  
    "type": "array",  
    "value": [  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:AssetConditionMonitoring:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:Nameplate:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalData:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      }  
    ]  
  }  
}  
```  
</details>  
#### Valori chiave I4AAS NGSI-LD Esempio  
Ecco un esempio di I4AAS in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
  "type": "I4AAS",  
  "administration": {  
    "version": "1.0",  
    "revision": "1.0"  
  },  
  "asset": {  
    "keys": [  
      {  
        "type": "Asset",  
        "local": true,  
        "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
        "index": 0,  
        "idType": "IRI"  
      }  
    ]  
  },  
  "category": "CONSTANT",  
  "conceptDictionaries": [],  
  "descriptions": [  
    {  
      "language": "en",  
      "text": "AAS of AASMRobotVI"  
    }  
  ],  
  "hasDataSpecification": [],  
  "idShort": "AASMRobotVI",  
  "identification": {  
    "idType": "IRI",  
    "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI"  
  },  
  "modelType": {  
    "name": "AssetAdministrationShell"  
  },  
  "refI4AssetId": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
  "submodels": [  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:AssetConditionMonitoring:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:Nameplate:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    },  
    {  
      "keys": [  
        {  
          "type": "Submodel",  
          "local": false,  
          "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalData:AASMRobotVI",  
          "index": 0,  
          "idType": "IRI"  
        }  
      ]  
    }  
  ],  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.AAS/context.jsonld"  
  ]  
}  
```  
</details>  
#### I4AAS NGSI-LD normalizzato Esempio  
Ecco un esempio di I4AAS in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
  "type": "I4AAS",  
  "administration": {  
    "type": "Property",  
    "value": {  
      "version": "1.0",  
      "revision": "1.0"  
    }  
  },  
  "asset": {  
    "type": "Property",  
    "value": {  
      "keys": [  
        {  
          "type": "Asset",  
          "local": true,  
          "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
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
  "conceptDictionaries": {  
    "type": "Property",  
    "value": []  
  },  
  "descriptions": {  
    "type": "Property",  
    "value": [  
      {  
        "language": "en",  
        "text": "AAS of AASMRobotVI"  
      }  
    ]  
  },  
  "hasDataSpecification": {  
    "type": "Property",  
    "value": []  
  },  
  "idShort": {  
    "type": "Property",  
    "value": "AASMRobotVI"  
  },  
  "identification": {  
    "type": "Property",  
    "value": {  
      "idType": "IRI",  
      "id": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI"  
    }  
  },  
  "modelType": {  
    "type": "Property",  
    "value": {  
      "name": "AssetAdministrationShell"  
    }  
  },  
  "refI4AssetId": {  
    "type": "Property",  
    "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI"  
  },  
  "submodels": {  
    "type": "Property",  
    "value": [  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalCapability:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:AssetConditionMonitoring:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:TechnicalData:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:Nameplate:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      },  
      {  
        "keys": [  
          {  
            "type": "Submodel",  
            "local": false,  
            "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalData:AASMRobotVI",  
            "index": 0,  
            "idType": "IRI"  
          }  
        ]  
      }  
    ]  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
