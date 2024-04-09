<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: I4SubmodelElementEigenschaft  
=====================================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.AAS/blob/master/I4SubmodelElementProperty/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Basierend auf IDTA-01001-3-0, bildet ein generisches RAMI4.0 SubmodelElement ab, das ein PROPERTY oder Attribut eines referenzierten AAS darstellt. RAMI4.0 Standard**  
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: Die Kategorie ist ein Wert, der weitere Metainformationen über die Klasse des Elements enthält.  - `constraints[array]`: Constraints, die angeben, welche Werte gleichzeitig genommen werden können. RAMI4.0 Asset Administration Shell Spezifikation. Version 3.0RC02  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `descriptions[array]`: Zum Hinzufügen detaillierter Kenntnisse über das Element in verschiedenen Sprachen  - `hasDataSpecification[array]`: Element, das mit Hilfe von Datenspezifikationsvorlagen erweitert werden kann. Eine Datenspezifikationsvorlage definiert einen benannten Satz zusätzlicher Attribute, die ein Element haben kann oder soll. RAMI4.0-Spezifikation  - `id[*]`: Eindeutiger Bezeichner der Entität  - `idShort[string]`: Short id ist der (kurze) Name des SubmodelElements in der RAMI40-Umgebung  - `kind[string]`: Für die Unterscheidung von "Typ" und "Instanz" wird der Begriff "Art" verwendet  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `modelType[object]`: Für die Unterscheidung von "Typ" und "Instanz" wird der Begriff "Art" verwendet  	- `name[string]`: Eigenschaft des Objekts. Normalerweise ist -Operation- für diesen Typ festgelegt    
- `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `refI4AASId[string]`: Verweist auf die Stamm-Assetverwaltungsschale, zu der dieses SubmodelElement gehört  - `refI4AssetId[string]`: Verweist auf das Stamm-Asset, zu dem dieses SubmodelElement gehört  - `refI4SubmodelId[string]`: Verweist auf das Wurzel-Submodell, zu dem dieses SubmodelElement gehört  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `semanticId[object]`: Sie verweist auf eine externe Informationsquelle, die die Formulierung des Teilmodellelements erklärt  	- `keys[array]`: Gruppe von Schlüsseln, die mit der sematicID des Modells in einem Objekt verbunden sind    
- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: Es muss ein RAMI4.0 I4SubmodelElementProperty NGSI Entity Typ sein, um eine RAMI4.0 AAS Digital Twin Submodel Operation Komponente darzustellen  - `value[['integer', 'string', 'number']]`: Eigenschaft: Der angegebene Wert im String/Integer-Format  - `valueId[string]`: ID des Elements der Untermodellelemente  - `valueType[object]`: Eigenschaft: Der Wertetyp im String-Format  	- `dataObjectType[object]`: Eigenschaft des Objekts. String, Integer, Float, Num usw. werden für diesen Typ verwendet.    
<!-- /30-PropertiesList -->  
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
I4SubmodelElementProperty:    
  description: 'Based on IDTA-01001-3-0, maps a generic RAMI4.0 SubmodelElement representing a PROPERTY or attribute of a referenced AAS. RAMI4.0 Standard'    
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
    constraints:    
      description: Constraints which tells which values can be taken simultaneously. RAMI4.0 Asset Administration Shell specification. Version 3.0RC02    
      items:    
        properties:    
          type:    
            description: 'Link, url, constraint ID (AAS Version 3.0RC02) or description of the constrain to be applied'    
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
      description: For adding detailed knowledge about the Element in different languages    
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
      description: Element that can be extended by using data specification templates. A data specification template defines a named set of additional attributes an element may or shall have. RAMI4.0 specification    
      items:    
        description: Every element of the data specification    
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
      description: Short id is the (short) name of the SubmodelElement within RAMI40 environment    
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
          description: Set of keys linked to the sematicID of the model in an object    
          items:    
            description: Every object containing the keys    
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
      description: It has to be RAMI4.0 I4SubmodelElementProperty NGSI Entity type to represent a RAMI4.0 AAS Digital Twin Submodel Operation component    
      enum:    
        - I4SubmodelElementProperty    
      type: string    
      x-ngsi:    
        type: Property    
    value:    
      description: Property.The given value in string/integer format    
      type:    
        - integer    
        - string    
        - number    
    valueId:    
      description: ID of the item of the submodel elements    
      type: string    
      x-ngsi:    
        type: Property    
    valueType:    
      description: Property.The value type used in string format    
      properties:    
        dataObjectType:    
          description: 'Property of the item. string, integer, float, num etc. are used set for this type'    
          properties:    
            name:    
              description: Name of the property    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
      type: object    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://industrialdigitaltwin.org/en/wp-content/uploads/sites/2/2023/04/IDTA-01001-3-0_SpecificationAssetAdministrationShell_Part1_Metamodel.pdf    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.AAS/blob/master/I4SubmodelElementProperty/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.AAS/I4SubmodelElementProperty/schema.json    
  x-model-tags: Corosect    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### I4SubmodelElementProperty NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine I4SubmodelElementProperty im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:AssetConditionMonitoring:MRobotStatus:AASMRobotVI",  
    "type": "I4SubmodelElementProperty",  
    "category": "PARAMETER",  
    "constraints": [],  
    "descriptions": [  
        {  
            "language": "en",  
            "text": "Telling about the overall status of the robot"  
        }  
    ],  
    "hasDataSpecification": [],  
    "idShort": "MRobotStatus",  
    "kind": "Instance",  
    "modelType": {  
        "name": "Property"  
    },  
    "refI4AASId": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
    "refI4AssetId": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
    "refI4SubmodelId": "urn:ngsi-v2:RAMI40:I4Submodel:AssetConditionMonitoring:AASMRobotVI",  
    "semanticId": {  
        "keys": [  
            {  
                "type": "ConceptDescription",  
                "local": true,  
                "value": "0173-1#02-ABC132#001",  
                "index": 0,  
                "idType": "IRDI"  
            }  
        ]  
    },  
    "value": 21,  
    "valueId": "ref033X",  
    "valueType": {  
        "dataObjectType": {  
            "name": "string"  
        }  
    }  
}  
```  
</details>  
#### I4SubmodelElementProperty NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine I4SubmodelElementProperty im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:OperationalData:VIResults:AASMRobotVI",  
    "type": "I4SubmodelElementProperty",  
    "idShort": {  
        "type": "Text",  
        "value": "VIResults",  
        "metadata": {}  
    },  
    "refI4AASId": {  
        "type": "Text",  
        "value": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
        "metadata": {}  
    },  
    "refI4AssetId": {  
        "type": "Text",  
        "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
        "metadata": {}  
    },  
    "refI4SubmodelId": {  
        "type": "Text",  
        "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalData:AASMRobotVI",  
        "metadata": {}  
    },  
    "value": {  
        "type": "Text",  
        "value": {  
            "Egg percentage": 14.385,  
            "Crate_ID": 1  
        },  
        "metadata": {}  
    }  
}  
```  
</details>  
#### I4SubmodelElementProperty NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine I4SubmodelElementProperty im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:AssetConditionMonitoring:MRobotStatus:AASMRobotVI",  
    "type": "I4SubmodelElementProperty",  
    "category": "PARAMETER",  
    "constraints": [],  
    "descriptions": [  
        {  
            "language": "en",  
            "text": "Telling about the overall status of the robot"  
        }  
    ],  
    "hasDataSpecification": [],  
    "idShort": "MRobotStatus",  
    "kind": "Instance",  
    "modelType": {  
        "name": "Property"  
    },  
    "refI4AASId": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI",  
    "refI4AssetId": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI",  
    "refI4SubmodelId": "urn:ngsi-v2:RAMI40:I4Submodel:AssetConditionMonitoring:AASMRobotVI",  
    "semanticId": {  
        "keys": [  
            {  
                "type": "ConceptDescription",  
                "local": true,  
                "value": "0173-1#02-ABC132#001",  
                "index": 0,  
                "idType": "IRDI"  
            }  
        ]  
    },  
    "value": 21,  
    "valueId": "ref033X",  
    "valueType": {  
        "dataObjectType": {  
            "name": "string"  
        }  
    },  
     "@context": [  
    "https://smart-data-models.github.io/dataModel.AAS/context.jsonld"  
  ]  
}  
```  
</details>  
#### I4SubmodelElementProperty NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine I4SubmodelElementProperty im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-v2:RAMI40:I4SubmodelElementProperty:OperationalData:VIResults:AASMRobotVI",  
  "type": "I4SubmodelElementProperty",  
  "idShort": {  
    "type": "Property",  
    "value": "VIResults"  
  },  
  "refI4AASId": {  
    "type": "Property",  
    "value": "urn:ngsi-v2:RAMI40:I4AAS:MRobotVI:AASMRobotVI"  
  },  
  "refI4AssetId": {  
    "type": "Property",  
    "value": "urn:ngsi-v2:RAMI40:I4Asset:MRobotVI:AASMRobotVI"  
  },  
  "refI4SubmodelId": {  
    "type": "Property",  
    "value": "urn:ngsi-v2:RAMI40:I4Submodel:OperationalData:AASMRobotVI"  
  },  
  "value": {  
    "type": "Property",  
    "value": {  
      "Egg percentage": 14.385,  
      "Crate_ID": 1  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
