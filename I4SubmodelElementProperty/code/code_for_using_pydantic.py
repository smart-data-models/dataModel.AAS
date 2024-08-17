from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Constraint(BaseModel):
    type: Optional[str] = Field(
        None,
        description='Link, url, constraint ID (AAS Version 3.0RC02) or description of the constrain to be applied',
    )


class Description(BaseModel):
    language: Optional[str] = Field(
        None,
        description='Substring identifying the language. Acronym according to ISO 639-1',
    )
    text: Optional[str] = Field(None, description='The Description text is filled here')


class HasDataSpecificationItem(BaseModel):
    type: Optional[str] = Field(
        None,
        description='Link, url or description of the specified data. DataSpecification template conformant to IEC61360',
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class ModelType(BaseModel):
    name: Optional[str] = Field(
        None,
        description='Property of the item. Usually -Operation- is set for this type',
    )


class Key(BaseModel):
    idType: Optional[str] = Field(None, description='References the ID of the type')
    index: Optional[float] = Field(None, description='Integer value of the item')
    local: Optional[bool] = Field(None, description='Describes a local or not item')
    value: Optional[str] = Field(
        None, description='Describes/includes the corresponding value'
    )


class SemanticId(BaseModel):
    keys: Optional[List[Key]] = Field(
        None,
        description='Set of keys linked to the sematicID of the model in an object',
    )


class Type6(Enum):
    I4SubmodelElementProperty = 'I4SubmodelElementProperty'


class DataObjectType(BaseModel):
    name: Optional[str] = Field(None, description='Name of the property')


class ValueType(BaseModel):
    dataObjectType: Optional[DataObjectType] = Field(
        None,
        description='Property of the item. string, integer, float, num etc. are used set for this type',
    )


class I4SubmodelElementProperty(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    category: Optional[str] = Field(
        None,
        description='The category is a value that gives further meta information w.r.t. to the class of the element',
    )
    constraints: Optional[List[Constraint]] = Field(
        None,
        description='Constraints which tells which values can be taken simultaneously. RAMI4.0 Asset Administration Shell specification. Version 3.0RC02',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    descriptions: Optional[List[Description]] = Field(
        None,
        description='For adding detailed knowledge about the Element in different languages',
    )
    hasDataSpecification: Optional[List[HasDataSpecificationItem]] = Field(
        None,
        description='Element that can be extended by using data specification templates. A data specification template defines a named set of additional attributes an element may or shall have. RAMI4.0 specification',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    idShort: Optional[str] = Field(
        None,
        description='Short id is the (short) name of the SubmodelElement within RAMI40 environment',
    )
    kind: Optional[str] = Field(
        None,
        description="For the distinction of 'type' and 'instance', the term 'kind' is used",
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    modelType: Optional[ModelType] = Field(
        None,
        description="For the distinction of 'type' and 'instance', the term 'kind' is used",
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    refI4AASId: Optional[str] = Field(
        None,
        description='References the root Asset Administration Shell which this SubmodelElement belongs to',
    )
    refI4AssetId: Optional[str] = Field(
        None,
        description='References the root Asset which this SubmodelElement belongs to',
    )
    refI4SubmodelId: Optional[str] = Field(
        None,
        description='References the root Submodel which this SubmodelElement belongs to',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    semanticId: Optional[SemanticId] = Field(
        None,
        description='It refers to an external information source, which explains the formulation of the submodel element',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None,
        description='It has to be RAMI4.0 I4SubmodelElementProperty NGSI Entity type to represent a RAMI4.0 AAS Digital Twin Submodel Operation component',
    )
    value: Optional[Union[int, str, float]] = Field(
        None, description='Property.The given value in string/integer format'
    )
    valueId: Optional[str] = Field(
        None, description='ID of the item of the submodel elements'
    )
    valueType: Optional[ValueType] = Field(
        None, description='Property.The value type used in string format'
    )
