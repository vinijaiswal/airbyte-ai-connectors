# Airbyte Greenhouse AI Connector

Type-safe Greenhouse API connector with full IDE autocomplete support for AI applications.

**Package Version:** 0.17.1

**Connector Version:** 0.1.0

**SDK Version:** 0.1.0

## Installation

```bash
uv pip install airbyte-ai-greenhouse
```

## Usage

```python
from airbyte_ai_greenhouse import GreenhouseConnector
from airbyte_ai_greenhouse.models import GreenhouseAuthConfig

# Create connector
connector = GreenhouseConnector(auth_config=GreenhouseAuthConfig(api_key="..."))

# Use typed methods with full IDE autocomplete
# (See Available Operations below for all methods)
```

## Available Operations

### Candidates Operations
- `list_candidates()` - Returns a paginated list of all candidates in the organization
- `get_candidate()` - Get a single candidate by ID

### Applications Operations
- `list_applications()` - Returns a paginated list of all applications
- `get_application()` - Get a single application by ID

### Jobs Operations
- `list_jobs()` - Returns a paginated list of all jobs in the organization
- `get_job()` - Get a single job by ID

### Offers Operations
- `list_offers()` - Returns a paginated list of all offers
- `get_offer()` - Get a single offer by ID

### Users Operations
- `list_users()` - Returns a paginated list of all users
- `get_user()` - Get a single user by ID

### Departments Operations
- `list_departments()` - Returns a paginated list of all departments
- `get_department()` - Get a single department by ID

### Offices Operations
- `list_offices()` - Returns a paginated list of all offices
- `get_office()` - Get a single office by ID

### Job_Posts Operations
- `list_job_posts()` - Returns a paginated list of all job posts
- `get_job_post()` - Get a single job post by ID

### Sources Operations
- `list_sources()` - Returns a paginated list of all sources

### Scheduled_Interviews Operations
- `list_scheduled_interviews()` - Returns a paginated list of all scheduled interviews
- `get_scheduled_interview()` - Get a single scheduled interview by ID

### Application_Attachment Operations
- `download_application_attachment()` - Downloads an attachment (resume, cover letter, etc.) for an application by index.
The attachment URL is a temporary signed AWS S3 URL that expires within 7 days.
Files should be downloaded immediately after retrieval.


### Candidate_Attachment Operations
- `download_candidate_attachment()` - Downloads an attachment (resume, cover letter, etc.) for a candidate by index.
The attachment URL is a temporary signed AWS S3 URL that expires within 7 days.
Files should be downloaded immediately after retrieval.


## Type Definitions

All response types are fully typed using TypedDict for IDE autocomplete support.
Import types from `airbyte_ai_greenhouse.types`.

## Documentation

Generated from OpenAPI 3.0 specification.

For API documentation, see the service's official API docs.
