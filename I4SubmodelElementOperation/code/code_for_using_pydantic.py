from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

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


class Description(BaseModel):
    language: Optional[str] = Field(
        None,
        description='Substring identifying the language. Acronym according to ISO 639-1',
    )
    text: Optional[str] = Field(None, description='The Description text is filled here')


class ExecutionState(Enum):
    canceled = 'canceled'
    completed = 'completed'
    failed = 'failed'
    initiated = 'initiated'
    running = 'running'
    timeout = 'timeout'


class HasDataSpecificationItem(BaseModel):
    type: Optional[str] = Field(
        None,
        description='Link, url or description of the specified data. DataSpecification template conformant to IEC61360',
    )


class Constraint(BaseModel):
    type: Optional[str] = Field(
        None,
        description='Link, url, constraint ID (AAS Version 3.0RC02) or description of the constrain to be applied',
    )


class ModelType(BaseModel):
    name: Optional[str] = Field(None, description='Property of the item')


class DataObjectType(BaseModel):
    name: Optional[str] = Field(None, description='Property of the item. Object type')


class ValueType(BaseModel):
    dataObjectType: Optional[DataObjectType] = Field(
        None,
        description='Property of the item. string, integer, float, num etc. are used set for this type',
    )


class InoutputVariableItem(BaseModel):
    category: Optional[str] = Field(
        None,
        description='The category is a value that gives further meta information w.r.t. to the class of the element',
    )
    constraints: Optional[List[Constraint]] = Field(
        None,
        description='Constraints an inoutput Variable may have. RAMI4.0 Asset Administration Shell specification. Version 3.0RC02',
    )
    descriptions: Optional[List[Description]] = Field(
        None,
        description='For adding detailed knowledge about the Element in different languages',
    )
    hasDataSpecification: Optional[List[HasDataSpecificationItem]] = Field(
        None,
        description='Element that can be extended by using data specification templates. A data specification template defines a named set of additional attributes an element may or shall have. RAMI4.0 specification',
    )
    idShort: Optional[str] = Field(
        None,
        description='short id is the (short) name of the inoutput Value -variable name- within RAMI40 environment',
    )
    kind: Optional[str] = Field(
        None,
        description="For the distinction of 'type' and 'instance', the term 'kind' is used",
    )
    modelType: Optional[ModelType] = Field(
        None,
        description="For the distinction of 'type' and 'instance', the term 'kind' is used",
    )
    value: Optional[str] = Field(
        None, description='The obtained value in string format'
    )
    valueType: Optional[ValueType] = Field(
        None, description='The value type used in string format'
    )


class ModelType1(BaseModel):
    name: Optional[str] = Field(
        None,
        description='Property of the item. Usually -OperationVariable- is set for this type',
    )


class ValueType1(BaseModel):
    dataObjectType: Optional[DataObjectType] = Field(
        None,
        description='Property of the item. string, integer, float, num etc. are used set for this type',
    )


class InputVariableItem(BaseModel):
    category: Optional[str] = Field(
        None,
        description='The category is a value that gives further meta information w.r.t. to the class of the element',
    )
    constraints: Optional[List[Constraint]] = Field(
        None,
        description='Constraints an Input Variable may have. RAMI4.0 Asset Administration Shell specification. Version 3.0RC02',
    )
    descriptions: Optional[List[Description]] = Field(
        None,
        description='For adding detailed knowledge about the Element in different languages',
    )
    hasDataSpecification: Optional[List[HasDataSpecificationItem]] = Field(
        None,
        description='Element that can be extended by using data specification templates. A data specification template defines a named set of additional attributes an element may or shall have. RAMI4.0 specification',
    )
    idShort: Optional[str] = Field(
        None,
        description='short id is the (short) name of the Input Value -variable name- within RAMI40 environment',
    )
    kind: Optional[str] = Field(
        None,
        description="For the distinction of 'type' and 'instance', the term 'kind' is used",
    )
    modelType: Optional[ModelType1] = Field(
        None,
        description="For the distinction of 'type' and 'instance', the term 'kind' is used",
    )
    value: Optional[str] = Field(None, description='The given value in string format')
    valueType: Optional[ValueType1] = Field(
        None, description='The value type used in string format'
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


class ModelType2(BaseModel):
    name: Optional[str] = Field(
        None,
        description='Property of the item. Usually -Operation- is set for this type',
    )


class MessageType(Enum):
    error = 'error'
    exception = 'exception'
    info = 'info'
    warning = 'warning'


class Message(BaseModel):
    code: Optional[str] = Field(
        None, description='Technology-dependent status or error code'
    )
    messageType: Optional[MessageType] = Field(
        None, description='The message type enum'
    )
    text: Optional[str] = Field(
        None,
        description='A message containing more information for the requester about a certain happening in the backend',
    )


class OperationResult(BaseModel):
    entity: Optional[Dict[str, Any]] = Field(
        None, description='Set of properties linked to the operation results'
    )
    entityType: Optional[str] = Field(
        None, description='Entity type description/reference'
    )
    isException: Optional[bool] = Field(None, description='True if it is an exception')
    messages: Optional[List[Message]] = Field(
        None, description='Additional message containing information for the requester'
    )
    success: Optional[bool] = Field(
        None, description='Success true if operation succeed. False if not'
    )


class ModelType3(BaseModel):
    name: Optional[str] = Field(
        None,
        description='Property of the item. Usually -OperationVariable- is set for this type',
    )


class ValueType2(BaseModel):
    dataObjectType: Optional[DataObjectType] = Field(
        None,
        description='Property of the item. string, integer, float, num etc. are used set for this type',
    )


class OutputVariableItem(BaseModel):
    category: Optional[str] = Field(
        None,
        description='The category is a value that gives further meta information w.r.t. to the class of the element',
    )
    constraints: Optional[List[Constraint]] = Field(
        None,
        description='Constraints an Output Variable may have. RAMI4.0 Asset Administration Shell specification. Version 3.0RC02',
    )
    descriptions: Optional[List[Description]] = Field(
        None,
        description='For adding detailed knowledge about the Element in different languages',
    )
    hasDataSpecification: Optional[List[HasDataSpecificationItem]] = Field(
        None,
        description='Element that can be extended by using data specification templates. A data specification template defines a named set of additional attributes an element may or shall have. RAMI4.0 specification',
    )
    idShort: Optional[str] = Field(
        None,
        description='short id is the (short) name of the Output Value -variable name- within RAMI40 environment',
    )
    kind: Optional[str] = Field(
        None,
        description="For the distinction of 'type' and 'instance', the term 'kind' is used",
    )
    modelType: Optional[ModelType3] = Field(
        None,
        description="For the distinction of 'type' and 'instance', the term 'kind' is used",
    )
    value: Optional[str] = Field(
        None, description='The obtained value in string format'
    )
    valueType: Optional[ValueType2] = Field(
        None, description='The value type used in string format'
    )


class Key(BaseModel):
    idType: Optional[str] = Field(None, description='References the ID of the type')
    index: Optional[float] = Field(None, description='Integer value of the item')
    local: Optional[bool] = Field(None, description='Describes a local or not item')
    value: Optional[str] = Field(
        None, description='Describes/includes the corresponding value'
    )


class SemanticId(BaseModel):
    keys: Optional[List[Key]] = Field(None, description='Keys for the semantic id')


class Type6(Enum):
    I4SubmodelElementOperation = 'I4SubmodelElementOperation'


class I4SubmodelElementOperation(BaseModel):
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
    executionState: Optional[ExecutionState] = Field(
        None, description='The operation invocation result state'
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
        description='short id is the (short) name of the SubmodelElement within RAMI40 environment',
    )
    inoutputVariable: Optional[List[InoutputVariableItem]] = Field(
        None,
        description='Array with parameters that are input and output of the operation',
    )
    inputVariable: Optional[List[InputVariableItem]] = Field(
        None, description='Array with input parameters of the operation'
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
    modelType: Optional[ModelType2] = Field(
        None,
        description="For the distinction of 'type' and 'instance', the term 'kind' is used",
    )
    name: Optional[str] = Field(None, description='The name of this item')
    operationResult: Optional[OperationResult] = Field(
        None,
        description='Contains The operation invocation result object with the returned result of an operation invocation',
    )
    outputVariable: Optional[List[OutputVariableItem]] = Field(
        None, description='Array with Output parameters of the operation'
    )
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
    requestId: Optional[str] = Field(
        None,
        description='Client request ID sent -for INPUT- and/or the retrieved value/status -for OUTPUT-. Used to TRACK the operations',
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
    timeout: Optional[float] = Field(
        None,
        description='Represents the timeout value for this command reported by the OPC-UA server',
    )
    type: Optional[Type6] = Field(
        None,
        description='It has to be RAMI4.0 I4SubmodelElementOperation NGSI Entity type to represent a RAMI4.0 AAS Digital Twin Submodel Operation component',
    )
