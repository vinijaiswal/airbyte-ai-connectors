# Airbyte Gong AI Connector

Type-safe Gong API connector with full IDE autocomplete support for AI applications.

## Installation

```bash
uv pip install airbyte-ai-gong
```

## Usage

```python
from airbyte_ai_gong import GongConnector
from airbyte_ai_gong.models import GongAuthConfig

# Create connector
connector = GongConnector(auth_config=GongAuthConfig(access_key="...", access_key_secret="..."))

# Use typed methods with full IDE autocomplete
# (See Available Actions below for all methods)
```

## Available Actions

### Users Actions
- `list_users()` - Returns a list of all users in the Gong account
- `get_user()` - Get a single user by ID

### Calls Actions
- `list_calls()` - Retrieve calls data by date range
- `get_call()` - Get specific call data by ID

### Calls_Extensive Actions
- `list_calls_extensive()` - Retrieve detailed call data including participants, interaction stats, and content

### Call_Audio Actions
- `download_call_audio()` - Downloads the audio media file for a call. Temporarily, the request body must be configured with:
{"filter": {"callIds": [CALL_ID]}, "contentSelector": {"exposedFields": {"media": true}}}


### Call_Video Actions
- `download_call_video()` - Downloads the video media file for a call. Temporarily, the request body must be configured with:
{"filter": {"callIds": [CALL_ID]}, "contentSelector": {"exposedFields": {"media": true}}}


### Workspaces Actions
- `list_workspaces()` - List all company workspaces

### Call_Transcripts Actions
- `get_call_transcripts()` - Returns transcripts for calls in a specified date range or specific call IDs

### Stats_Activity_Aggregate Actions
- `get_activity_aggregate()` - Provides aggregated user activity metrics across a specified period

### Stats_Activity_Day_By_Day Actions
- `get_activity_day_by_day()` - Delivers daily user activity metrics across a specified date range

### Stats_Interaction Actions
- `get_interaction_stats()` - Returns interaction stats for users based on calls that have Whisper turned on

### Settings_Scorecards Actions
- `list_scorecards()` - Retrieve all scorecard configurations in the company

### Settings_Trackers Actions
- `list_trackers()` - Retrieve all keyword tracker configurations in the company

### Library_Folders Actions
- `list_library_folders()` - Retrieve the folder structure of the call library

### Library_Folder_Content Actions
- `list_folder_content()` - Retrieve calls in a specific library folder

### Coaching Actions
- `list_coaching_metrics()` - Retrieve coaching metrics for a manager and their direct reports

### Stats_Activity_Scorecards Actions
- `list_answered_scorecards()` - Retrieve answered scorecards for applicable reviewed users or scorecards for a date range

## Type Definitions

All response types are fully typed using Pydantic models for IDE autocomplete support.
Import types from `airbyte_ai_gong.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.

## Version Information

**Package Version:** 0.19.2

**Connector Version:** 0.1.0

**SDK Version:** 0.1.0