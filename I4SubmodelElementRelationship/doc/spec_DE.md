<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: I4SubmodelElementBeziehung  
===================================<!-- /10-Header -->  
<!-- 15-License -->  
Open License  
Dokument generiert automatisch: [https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60]  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Basierend auf IDTA-01001-3-0, beschreibt einen generischen RAMI4.0 SubmodelElement, der eine Beziehung zu einem referenzierten Asset Administration Shell darstellt.**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  
Liste der Eigenschaften  
<sup><sub>[*] Wenn kein Typ in einem Attribut vorhanden ist, da es mehrere Typen oder unterschiedliche Formate/Mustern haben könnte</sub></sup>  
- `address[object]`: Die Adress für die Post.  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel Spanien.  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Gegend, in der die Straßenadresse liegt, und die in der Region befindliche Adresse.  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich die Gemeinde befindet, und die im Land liegt.  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art Verwaltungsgliederung, die in einigen Ländern vom lokalen Pemerintah verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postbezugsquellen. Zum Beispiel 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Postleitzahl. Zum Beispiel 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Adresse  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Zahl, die eine bestimmte Eigenschaft auf einer öffentlichen Straße identifiziert.    
- `alternateName[string]`: Eine alternative Bezeichnung für dieses Objekt  - `areaServed[string]`: Die geografische Region, in der ein Dienst oder angebotene Sache bereitgestellt wird.  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: Die Kategorie ist ein Wert, der weitere Meta-Information zu den Klassen des Elements liefert.  - `dataProvider[string]`: Eine Zeichenfolge, die den Anbieter der harmonisierten Datenentität identifiziert.  - `dateCreated[date-time]`: Entitätserstellungszeitstempel. Dies wird normalerweise von der Speichersoftware zugewiesen.  - `dateModified[date-time]`: Zeitstempel der letzten Änderung des Entitäts. Dies wird normalerweise von der Speicherdiensteplattform zugewiesen.  - `description[string]`: Eine Beschreibung dieses Artikels  - `descriptions[array]`: Für die Erweiterung detaillierter Kenntnisse über das Element in verschiedenen Sprachen.  - `first[string]`: Bezieht sich auf das erste Referenzelement des Beziehungselements.  - `hasDataSpecification[array]`: Element, der durch die Verwendung von Daten-Spezifikationsvorlagen erweitert werden kann. Eine Daten-Spezifikationsvorlage definiert einen benannten Satz zusätzlicher Attribute, die ein Element haben kann. RAMI4.0-Spezifikation  - `id[*]`: Eindeutige Identifikationsnummer der Entität  - `idShort[string]`: Der kurze ID ist der (kurze) Name des SubmodelElements innerhalb der RAMI40 Umgebung.  - `kind[string]`: Für die Unterscheidung von 'Type' und 'Instanz' wird der Begriff 'Kind' verwendet.  - `location[*]`: Geodätische Referenz für das Objekt. Es kann ein Punkt, eine Linienstring, ein Polygon, mehrere Punkte, mehrere Linienstrings oder ein Multipolygon sein.  - `modelType[object]`: Für die Unterscheidung von 'Type' und 'Instanz' wird der Begriff 'Kind' verwendet.  	- `name[string]`: Eigenschaft des Artikels. In der Regel wird für diesen Typ -Operation- gesetzt.    
- `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste, die einen JSON-kodierten Sequenz von Zeichen enthält, die sich an die eindeutigen IDs der Eigentümer verweist.  - `refI4AASId[string]`: Bezieht sich auf den Wurzel-Asset-Verwaltungsschalter, zu dem dieses Submodellelement gehört.  - `refI4AssetId[string]`: Bezieht sich auf die Wurzel-Asset, zu dem dieses Submodellelement gehört.  - `second[string]`: Bezieht sich auf das zweite Referenzelement des Element-Elements.  - `seeAlso[*]`: Liste von URI, die auf zusätzliche Ressourcen zu diesem Artikel verweisen.  - `semanticId[object]`: Es bezieht sich auf eine externe Informationsquelle, die die Formulierung des Untermodells-Elements erklärt.  	- `keys[array]`: Schlüssel für die semantische ID    
- `source[string]`: Eine Sequenz von Zeichen, die den ursprünglichen Ursprung der Datenquelle als URL angibt. Es wird empfohlen, den vollständig qualifizierten Domainnamen des Datenanbieters zu verwenden oder die URL zum Datenobjekt.  - `type[string]`: Es muss ein RAMI4.0 I4SubmodelElementRelationship NGSI Entity-Typ sein, um ein RAMI4.0 AAS Digital Twin Submodel Beziehungskomponente darzustellen.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Datenmodellbeschreibung von Eigenschaften  
Sortiert alphabetisch (klicke für Details)  
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
Beispiel-Payloads  
#### I4SubmodelElementRelationship NGSI-v2 Key-Values Beispiel  
Hier ist ein Beispiel für ein I4SubmodelElementRelationship in JSON-LD-Format als Schlüssel-Wert-Paare. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und den Kontextdaten eines einzelnen Entitäts zurückgibt.  
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
#### I4SubmodelElementRelationship NGSI-v2 normalized Example  
Hier ist ein Beispiel für ein I4SubmodelElementRelationship in JSON-LD-Format als normalisiert. Dies ist mit NGSI-v2 kompatibel, wenn keine Optionen verwendet werden und die Kontextdaten eines einzelnen Entitäts zurückgibt.  
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
#### I4SubmodelElementRelationship NGSI-LD Schlüssel-Werte Beispiel '  
Hier ist ein Beispiel für ein I4SubmodelElementRelationship im JSON-LD-Format als Schlüssel-Wert-Paare. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und gibt die Kontextdaten einer einzelnen Entität zurück.  
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
#### I4SubmodelElementRelationship NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein I4SubmodelElementRelationship im JSON-LD-Format als normalisiert. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und gibt die Kontextdaten einer einzelnen Entität zurück.  
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
Schau dir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) an, um herauszufinden, wie man mit Magnitude-Einheiten umgeht.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
