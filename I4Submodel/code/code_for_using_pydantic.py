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
        description='AAS Version number is the number in line with release of specification',
    )


class Description(BaseModel):
    language: Optional[str] = Field(
        None,
        description='Substring identifying the language. Acronym according to ISO 639-1',
    )
    text: Optional[str] = Field(None, description='The Description text is filled here')


class HasDataSpecificationItem(BaseModel):
    type: Optional[str] = Field(
        None, description='Link, url or description of the specified data'
    )


class Identification(BaseModel):
    id: Optional[AnyUrl] = Field(
        None,
        description='Identity information that unambiguously distinguishes one Submodel from another one -NGSI Id-. RAMI4.0 environment ',
    )
    idType: Optional[str] = Field(
        None, description='Type of the Identifier, eg.IRI or IRDI'
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
        None, description='Property of the item. Usually Submodel is set for this type.'
    )


class Qualifier(BaseModel):
    type: Optional[str] = Field(
        None, description='Link, url or description of the qualifier'
    )


class SemanticId(BaseModel):
    keys: Optional[List[str]] = Field(None, description='Keys for the Semantic ID')


class ModelType1(BaseModel):
    name: Optional[str] = Field(
        None, description='Property of the item. Name of the model type'
    )


class SubmodelElement(BaseModel):
    category: Optional[str] = Field(
        None,
        description='The category is a value that gives further meta information w.r.t. to the class of the element',
    )
    idShort: Optional[str] = Field(
        None,
        description='short id is the (short) name of the Submodel within RAMI40 environment',
    )
    modelType: Optional[ModelType1] = None
    refI4SubmodelElement: Optional[str] = Field(
        None,
        description='Link to the NGSI entity -I4SubmodelElementOperation or I4SubmodelElementProperty- that maps the Command/Property of the Submodel',
    )


class Type6(Enum):
    I4Submodel = 'I4Submodel'


class I4Submodel(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    administration: Optional[Administration] = Field(
        None, description='AAS Submodel administration information'
    )
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
        description='For adding detailed knowledge about the AAS in different languages',
    )
    hasDataSpecification: Optional[List[HasDataSpecificationItem]] = Field(
        None,
        description='Data specification defines the additional attributes a Submodel may have. RAMI4.0 specification',
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
        description='short id is the (short) name of the Submodel within RAMI40 environment',
    )
    identification: Optional[Identification] = Field(
        None,
        description='Identification of the Submodel within its AAS. RAMI4.0 environment',
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
        description="For the distinction of 'type' and 'instance', the term 'kind' is used.",
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
    qualifiers: Optional[List[Qualifier]] = Field(
        None,
        description='Qualifiers are used if the semantics of the element is the same independent of its qualifiers. It is only the quality or the meaning of the value for the element that differs',
    )
    refI4AASId: Optional[str] = Field(
        None,
        description='References the root Asset Administration Shell which this Submodel belongs to',
    )
    refI4AssetId: Optional[str] = Field(
        None, description='References the root Asset which this Submodel belongs to'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    semanticId: Optional[SemanticId] = Field(
        None,
        description='It refer to an external information source, which explains the formulation of the submodel',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    submodelElements: Optional[List[SubmodelElement]] = Field(
        None,
        description='Data element which includes the list of Elements -Operations or Commands AND Properties- I4SubmodelElementOperation for RAMI commands / I4SubmodelElementProperty for RAMI Properties',
    )
    type: Optional[Type6] = Field(
        None,
        description='It has to be RAMI4.0 I4Submodel NGSI Entity type to represent a RAMI4.0 AAS Digital Twin Submodel component',
    )
