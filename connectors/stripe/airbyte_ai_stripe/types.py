"""
Type definitions for stripe connector.
"""
# Use typing_extensions.TypedDict for Pydantic compatibility on Python < 3.12
try:
    from typing_extensions import TypedDict, NotRequired
except ImportError:
    from typing import TypedDict, NotRequired  # type: ignore[attr-defined]


# ===== RESPONSE TYPE DEFINITIONS =====

class CustomerAddress(TypedDict):
    """Customer's address"""
    line1: NotRequired[str]
    line2: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    postal_code: NotRequired[str]
    country: NotRequired[str]

class Customer(TypedDict):
    """Customer type definition"""
    id: str
    object: str
    email: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    phone: NotRequired[str]
    address: NotRequired[CustomerAddress]
    metadata: NotRequired[dict[str, str]]
    created: NotRequired[int]
    balance: NotRequired[int]
    delinquent: NotRequired[bool]

class CustomerList(TypedDict):
    """CustomerList type definition"""
    object: NotRequired[str]
    data: NotRequired[list[Customer]]
    has_more: NotRequired[bool]
    url: NotRequired[str]

# ===== METADATA TYPE DEFINITIONS =====
# Meta types for operations that extract metadata (e.g., pagination info)

# ===== OPERATION PARAMS TYPE DEFINITIONS =====

class CustomersListParams(TypedDict):
    """Parameters for customers.list operation"""
    limit: NotRequired[int]
    starting_after: NotRequired[str]
    ending_before: NotRequired[str]
    email: NotRequired[str]

class CustomersGetParams(TypedDict):
    """Parameters for customers.get operation"""
    id: str
