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


class Administration(BaseModel):
    revision: Optional[str] = Field(
        None,
        description='AAS Revision number is the number in line with release of specification',
    )
    version: Optional[str] = Field(
        None,
        description='AAS version number is the number in line with release of specification',
    )


class Key(BaseModel):
    idType: Optional[str] = Field(None, description='Property. idType of the item')
    index: Optional[int] = Field(
        None, description='Property. Integer related to the item'
    )
    local: Optional[bool] = Field(
        None, description='Property. True if this is local item. False if not'
    )
    type: Optional[str] = None
    value: Optional[str] = Field(None, description='Property. Value of the item')


class AssetIdentificationModelRef(BaseModel):
    keys: Optional[List[Key]] = Field(None, description='keys for the asset instance')


class Key1(BaseModel):
    idType: Optional[str] = Field(None, description='Property. idType of the item')
    index: Optional[int] = Field(None, description='Property. Order of the item')
    local: Optional[bool] = Field(
        None, description='Property. Whether if the item is local'
    )
    type: Optional[str] = None
    value: Optional[str] = Field(None, description='Property. Value of the item')


class BillOfMaterialRef(BaseModel):
    keys: Optional[List[Key1]] = Field(None, description='Keys for the Semantic ID')


class Description(BaseModel):
    language: Optional[str] = Field(
        None,
        description='Substring identifying the language. Acronym according to ISO 639-1',
    )
    text: Optional[str] = Field(None, description='Add the description text here')


class HasDataSpecificationItem(BaseModel):
    type: Optional[str] = Field(
        None, description='Link, url or description of the specified data'
    )


class Identification(BaseModel):
    id: Optional[AnyUrl] = Field(
        None,
        description='Identity information that unambiguously distinguishes one RAMI Instance from another one',
    )
    idType: Optional[str] = Field(
        None, description='Type of the Identifier, eg.IRI or IRD'
    )


class Kind(Enum):
    Instance = 'Instance'


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
    name: Optional[str] = Field(None, description='Type of the referenced item')


class Type6(Enum):
    I4Asset = 'I4Asset'


class I4Asset(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    administration: Optional[Administration] = Field(
        None, description='Instance administration information'
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    assetIdentificationModelRef: Optional[AssetIdentificationModelRef] = Field(
        None,
        description='An asset typically may be represented by several different identification properties like for example the serial number, its RFID code etc. Such local identification properties are defined in the asset identification submodel',
    )
    billOfMaterialRef: Optional[BillOfMaterialRef] = Field(
        None,
        description='A complex asset is composed out of other entities and assets. These entities and assets being part of the asset are specified in the bill of material',
    )
    category: Optional[str] = Field(
        None,
        description='The category is a value that gives further meta information w.r.t. to the class of the AAS',
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
        None, description='For adding detailed knowledge in different languages'
    )
    hasDataSpecification: Optional[List[HasDataSpecificationItem]] = Field(
        None,
        description='Data specification defines the additional attributes an asset may have. RAMI4.0 specification',
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
        None, description='Short id (name) of the RAMI Instance'
    )
    identification: Optional[Identification] = Field(
        None, description='Identification of the AAS -Asset- Instance object'
    )
    kind: Optional[Kind] = Field(
        None, description='Kind of the Schema. This is restricted to Instance'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    modelType: Optional[ModelType] = Field(
        None, description='Instance model type according to IDTA'
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
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None, description='It has to be RAMI4.0 I4Asset NGSI Entity type'
    )
