# Airbyte Gong AI Connector

Type-safe Gong API connector with full IDE autocomplete support for AI applications.

**Version:** 1.0.0

## Installation

```bash
uv pip install airbyte-ai-gong
```

## Usage

```python
from airbyte_ai_gong import GongConnector

# Create connector
connector = GongConnector.create(secrets={"api_key": "your_api_key"})

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Users Operations
- `list_users()` - List users
- `get_user()` - Get a user

### Calls Operations
- `list_calls()` - List calls
- `get_call()` - Get a call

### Workspaces Operations
- `list_workspaces()` - List workspaces

### Call_Transcripts Operations
- `get_call_transcripts()` - Retrieve call transcripts

## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_gong.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
