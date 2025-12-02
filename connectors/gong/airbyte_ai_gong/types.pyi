"""
Auto-generated type definitions for gong connector.

Generated from OpenAPI specification schemas.
"""
from typing import TypedDict, NotRequired, Any

# ===== RESPONSE TYPE DEFINITIONS =====

class PaginationRecords(TypedDict):
    """Pagination metadata"""
    totalRecords: NotRequired[int]
    currentPageSize: NotRequired[int]
    currentPageNumber: NotRequired[int]
    cursor: NotRequired[str]

class User(TypedDict):
    """User object"""
    id: NotRequired[str]
    emailAddress: NotRequired[str]
    firstName: NotRequired[str]
    lastName: NotRequired[str]
    active: NotRequired[bool]
    createdDate: NotRequired[str]

class UsersResponse(TypedDict):
    """Response containing list of users"""
    users: NotRequired[list[User]]
    records: NotRequired[PaginationRecords]
    requestId: NotRequired[str]

class UserResponse(TypedDict):
    """Response containing single user"""
    user: NotRequired[User]
    requestId: NotRequired[str]

class Call(TypedDict):
    """Call object"""
    id: NotRequired[str]
    url: NotRequired[str]
    title: NotRequired[str]
    started: NotRequired[str]
    duration: NotRequired[int]
    primaryUserId: NotRequired[str]
    direction: NotRequired[str]
    system: NotRequired[str]
    scope: NotRequired[str]
    language: NotRequired[str]

class CallsResponse(TypedDict):
    """Response containing list of calls"""
    calls: NotRequired[list[Call]]
    records: NotRequired[PaginationRecords]
    requestId: NotRequired[str]

class CallResponse(TypedDict):
    """Response containing single call"""
    call: NotRequired[Call]
    requestId: NotRequired[str]

class Workspace(TypedDict):
    """Workspace object"""
    workspaceId: NotRequired[str]
    name: NotRequired[str]

class WorkspacesResponse(TypedDict):
    """Response containing list of workspaces"""
    workspaces: NotRequired[list[Workspace]]
    requestId: NotRequired[str]

class CallTranscript(TypedDict):
    """Call transcript object"""
    callId: NotRequired[str]
    transcript: NotRequired[list[dict[str, Any]]]

class TranscriptsResponse(TypedDict):
    """Response containing call transcripts"""
    callTranscripts: NotRequired[list[CallTranscript]]
    records: NotRequired[PaginationRecords]
    requestId: NotRequired[str]

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class UsersListParams(TypedDict):
    """Parameters for users.list operation"""
    cursor: NotRequired[str]

class UsersGetParams(TypedDict):
    """Parameters for users.get operation"""
    id: str

class CallsListParams(TypedDict):
    """Parameters for calls.list operation"""
    fromDateTime: str
    toDateTime: str
    cursor: NotRequired[str]

class CallsGetParams(TypedDict):
    """Parameters for calls.get operation"""
    id: str

class WorkspacesListParams(TypedDict):
    """Parameters for workspaces.list operation"""
    pass

class CallTranscriptsListParams(TypedDict):
    """Parameters for call_transcripts.list operation"""
    pass
