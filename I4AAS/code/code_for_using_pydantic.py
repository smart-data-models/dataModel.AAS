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
    revision: str = Field(
        ...,
        description='AAS Revision number is the number in line with release of specification',
    )
    version: str = Field(
        ...,
        description='AAS Version number is the number in line with release of specification',
    )


class Type(Enum):
    Asset = 'Asset'


class Key(BaseModel):
    idType: str = Field(
        ..., description='Property. Type of the Identifier, eg.IRI or IRDI'
    )
    index: int = Field(
        ..., description='Property. Index encodes the position in the original sequence'
    )
    local: bool = Field(
        ...,
        description='Property. It defines whether the asset is created locally or globally',
    )
    type: Type = Field(..., description='Property. Type (description) of the asset')
    value: str = Field(
        ...,
        description='Property. Here comes the id pointing to the definition of asset',
    )


class Asset(BaseModel):
    keys: List[Key] = Field(..., description='Keys for the Asset')


class ConceptDictionary(BaseModel):
    type: Optional[str] = Field(
        None,
        description='Link, url, reference or description of the specified I4.0 concept',
    )


class Description(BaseModel):
    language: str = Field(
        ...,
        description='Substring identifying the language. Acronym according to ISO 639-1',
    )
    text: str = Field(..., description='The Description text is filled here')


class HasDataSpecificationItem(BaseModel):
    type: Optional[str] = Field(
        None, description='Link, url or descriptionof the specified data'
    )


class Identification(BaseModel):
    id: AnyUrl = Field(
        ...,
        description='Identity information that unambiguously distinguishes one AAS from another one. RAMI4.0 environmet ',
    )
    idType: str = Field(..., description='Type of the Identifier, eg.IRI or IRDI')


class Type1(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type1


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type2(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type2


class Type3(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type3


class Type4(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type4


class Type5(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type5


class Type6(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type6


class ModelType(BaseModel):
    name: str = Field(
        ..., description='Description of the referenced property of the item'
    )


class Type7(Enum):
    Submodel = 'Submodel'


class Key1(BaseModel):
    idType: str = Field(
        ...,
        description='Identity information that unambiguously distinguishes one submodel from another one. Can be IRI or IRDI',
    )
    index: float = Field(
        ..., description='Index encodes the position in the original sequence'
    )
    local: bool = Field(
        ...,
        description='It defines whether the submodel is created locally or globally',
    )
    type: Type7 = Field(..., description='Type (description) of the submodel')
    value: str = Field(
        ...,
        description='The id of the submodel pointing to the definition of the Submodel',
    )


class Submodel(BaseModel):
    keys: List[Key1] = Field(..., description='keys for the submodel')


class Type8(Enum):
    I4AAS = 'I4AAS'


class I4AAS(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    administration: Optional[Administration] = Field(
        None, description='AAS administration information'
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    asset: Optional[Asset] = Field(
        None, description='The Asset descripton is filled here'
    )
    category: Optional[str] = Field(
        None,
        description='The category is a value that gives further meta information w.r.t. to the class of the element',
    )
    conceptDictionaries: Optional[List[ConceptDictionary]] = Field(
        None,
        description='The Asset itself can also define its own dictionary that contains semantic definitions of its submodel elements. These semantic definitions are called concept descriptions (ConceptDescription or concept dictionary). This array will contain ref ids to RAMI4.0 specific concepts used within this model',
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
        description='For adding detailed knowldedge about the AAS in different languages',
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
        None,
        description='short id is the (short) name of the ASSET ADMINISTRATION SHELL',
    )
    identification: Optional[Identification] = Field(
        None, description='Identification of the AAS for the asset. RAMI4.0 environment'
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
    refI4AssetId: Optional[AnyUrl] = Field(
        None, description='References the root Asset linked to this AAS'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    submodels: Optional[List[Submodel]] = Field(
        None,
        description='AAS contains complex set of informations, submodels provide a separate category for this complex data',
    )
    type: Optional[Type8] = Field(
        None,
        description='It has to be RAMI4.0 I4AAS NGSI Entity type to represent a RAMI4.0 AAS Digital Twin',
    )
