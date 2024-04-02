<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: I4AAS  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4AAS/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Basierend auf IDTA-01001-3-0, beschreibt einen generischen Asset Administration Shell - AAS - Baum, Komponente des RAMI4.0**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße    
- `administration[object]`: Informationen zur Verwaltung der AAS  	- `revision[string]`: Die AAS-Revisionsnummer ist die Nummer, die der Veröffentlichung der Spezifikation entspricht.    
	- `version[string]`: Die AAS-Versionsnummer ist die Nummer, die der Veröffentlichung der Spezifikation entspricht.    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `asset[object]`: Die Asset-Beschreibung wird hier ausgefüllt  	- `keys[array]`: Schlüssel für das Asset    
- `category[string]`: Die Kategorie ist ein Wert, der weitere Metainformationen über die Klasse des Elements enthält.  - `conceptDictionaries[array]`: Das Asset selbst kann auch sein eigenes Wörterbuch definieren, das semantische Definitionen seiner Teilmodellelemente enthält. Diese semantischen Definitionen werden Konzeptbeschreibungen genannt (ConceptDescription oder concept dictionary). Dieses Array enthält Referenz-IDs zu RAMI4.0-spezifischen Konzepten, die in diesem Modell verwendet werden  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `descriptions[array]`: Hinzufügen von detailliertem Wissen über die AAS in verschiedenen Sprachen  - `hasDataSpecification[array]`: Die Datenspezifikation definiert die zusätzlichen Attribute, die ein Asset haben kann. RAMI4.0 Spezifikation  - `id[*]`: Eindeutiger Bezeichner der Entität  - `idShort[string]`: short id ist der (kurze) Name der ASSET ADMINISTRATION SHELL  - `identification[object]`: Identifizierung des AAS für das Asset. RAMI4.0-Umgebung  	- `id[uri]`: Identitätsinformation, die ein AAS eindeutig von einem anderen unterscheidet. RAMI4.0-Umgebung    
	- `idType[string]`: Art des Identifikators, z. B. IRI oder IRDI    
- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `modelType[object]`: Für die Unterscheidung von "Typ" und "Instanz" wird der Begriff "Art" verwendet  	- `name[string]`: Beschreibung der referenzierten Eigenschaft des Artikels    
- `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `refI4AssetId[uri]`: Verweist auf das mit dieser AAS verknüpfte Stamm-Asset  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `submodels[array]`: AAS enthält komplexe Informationen, Untermodelle bieten eine eigene Kategorie für diese komplexen Daten  - `type[string]`: Es muss eine RAMI4.0 I4AAS NGSI Entität sein, um einen RAMI4.0 AAS Digital Twin zu repräsentieren.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### I4AAS NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein I4AAS im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### I4AAS NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein I4AAS im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### I4AAS NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein I4AAS im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### I4AAS NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein I4AAS im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
