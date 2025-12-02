"""
Auto-generated greenhouse connector. Do not edit manually.

Generated from OpenAPI specification.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Any, Dict, overload, Self
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
from pathlib import Path

if TYPE_CHECKING:
    from ._vendored.connector_sdk.executor import ExecutorProtocol
    from .types import (
        Application,
        ApplicationsGetParams,
        ApplicationsListParams,
        Candidate,
        CandidatesGetParams,
        CandidatesListParams,
        Job,
        JobsGetParams,
        JobsListParams,
    )


class GreenhouseConnector:
    """
    Type-safe Greenhouse API connector.

    Auto-generated from OpenAPI specification with full type safety.
    """

    connector_name = "greenhouse"
    connector_version = "1.0.0"
    vendored_sdk_version = "0.1.0"  # Version of vendored connector-sdk

    def __init__(self, executor: ExecutorProtocol):
        """Initialize connector with an executor."""
        self._executor = executor
        self.candidates = CandidatesQuery(self)
        self.applications = ApplicationsQuery(self)
        self.jobs = JobsQuery(self)

    @classmethod
    def create(
        cls,
        secrets: Optional[dict[str, str]] = None,
        config_path: Optional[str] = None,
        connector_id: Optional[str] = None,
        airbyte_client_id: Optional[str] = None,
        airbyte_client_secret: Optional[str] = None,
        airbyte_connector_api_url: Optional[str] = None    ) -> Self:
        """
        Create a new greenhouse connector instance.

        Supports both local and hosted execution modes:
        - Local mode: Provide `secrets` for direct API calls
        - Hosted mode: Provide `connector_id`, `airbyte_client_id`, and `airbyte_client_secret` for hosted execution

        Args:
            secrets: API secrets/credentials (required for local mode)
            config_path: Optional path to connector config (uses bundled default if None)
            connector_id: Connector ID (required for hosted mode)
            airbyte_client_id: Airbyte OAuth client ID (required for hosted mode)
            airbyte_client_secret: Airbyte OAuth client secret (required for hosted mode)
        Returns:
            Configured GreenhouseConnector instance

        Examples:
            # Local mode (direct API calls)
            connector = GreenhouseConnector.create(secrets={"api_key": "sk_..."})

            # Hosted mode (executed on Airbyte cloud)
            connector = GreenhouseConnector.create(
                connector_id="connector-456",
                airbyte_client_id="client_abc123",
                airbyte_client_secret="secret_xyz789"
            )
        """
        # Hosted mode: connector_id, airbyte_client_id, and airbyte_client_secret provided
        if connector_id and airbyte_client_id and airbyte_client_secret:
            from ._vendored.connector_sdk.executor import HostedExecutor
            executor = HostedExecutor(
                connector_id=connector_id,
                airbyte_client_id=airbyte_client_id,
                airbyte_client_secret=airbyte_client_secret,
                api_url=airbyte_connector_api_url,
            )
            return cls(executor)

        # Local mode: secrets required
        if not secrets:
            raise ValueError(
                "Either provide (connector_id, airbyte_client_id, airbyte_client_secret) for hosted mode "
                "or secrets for local mode"
            )

        from ._vendored.connector_sdk.executor import LocalExecutor

        if not config_path:
            config_path = str(cls.get_default_config_path())

        executor = LocalExecutor(config_path=config_path, secrets=secrets)
        connector = cls(executor)

        # Update base_url with server variables if provided

        return connector

    @classmethod
    def get_default_config_path(cls) -> Path:
        """Get path to bundled connector config."""
        return Path(__file__).parent / "connector.yaml"

    # ===== TYPED EXECUTE METHOD (Recommended Interface) =====
    @overload
    async def execute(
        self,
        resource: Literal["candidates"],
        verb: Literal["list"],
        params: "CandidatesListParams"
    ) -> "dict[str, Any]": ...
    @overload
    async def execute(
        self,
        resource: Literal["candidates"],
        verb: Literal["get"],
        params: "CandidatesGetParams"
    ) -> "Candidate": ...
    @overload
    async def execute(
        self,
        resource: Literal["applications"],
        verb: Literal["list"],
        params: "ApplicationsListParams"
    ) -> "dict[str, Any]": ...
    @overload
    async def execute(
        self,
        resource: Literal["applications"],
        verb: Literal["get"],
        params: "ApplicationsGetParams"
    ) -> "Application": ...
    @overload
    async def execute(
        self,
        resource: Literal["jobs"],
        verb: Literal["list"],
        params: "JobsListParams"
    ) -> "dict[str, Any]": ...
    @overload
    async def execute(
        self,
        resource: Literal["jobs"],
        verb: Literal["get"],
        params: "JobsGetParams"
    ) -> "Job": ...

    @overload
    async def execute(
        self,
        resource: str,
        verb: str,
        params: Dict[str, Any]
    ) -> Dict[str, Any]: ...

    async def execute(
        self,
        resource: str,
        verb: str,
        params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Execute a resource operation with full type safety.

        This is the recommended interface for blessed connectors as it:
        - Uses the same signature as non-blessed connectors
        - Provides full IDE autocomplete for resource/verb/params
        - Makes migration from generic to blessed connectors seamless

        Args:
            resource: Resource name (e.g., "customers")
            verb: Operation verb (e.g., "create", "get", "list")
            params: Operation parameters (typed based on resource+verb)

        Returns:
            Typed response based on the operation

        Example:
            customer = await connector.execute(
                resource="customers",
                verb="get",
                params={"id": "cus_123"}
            )
        """
        from ._vendored.connector_sdk.executor import ExecutionConfig

        # Use ExecutionConfig for both local and hosted executors
        config = ExecutionConfig(
            resource=resource,
            verb=verb,
            params=params
        )

        result = await self._executor.execute(config)

        if not result.success:
            raise RuntimeError(f"Execution failed: {result.error}")

        return result.data



class CandidatesQuery:
    """
    Query class for Candidates resource operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        **kwargs
    ) -> "dict[str, Any]":
        """
        List candidates

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("candidates", "list", params)
    async def get(
        self,
        id: Optional[str] = None,
        **kwargs
    ) -> "Candidate":
        """
        Get a candidate

        Args:
            id: Candidate ID
            **kwargs: Additional parameters

        Returns:
            Candidate
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("candidates", "get", params)
class ApplicationsQuery:
    """
    Query class for Applications resource operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        created_before: Optional[str] = None,
        created_after: Optional[str] = None,
        last_activity_after: Optional[str] = None,
        job_id: Optional[int] = None,
        status: Optional[str] = None,
        **kwargs
    ) -> "dict[str, Any]":
        """
        List applications

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            created_before: Filter by applications created before this timestamp
            created_after: Filter by applications created after this timestamp
            last_activity_after: Filter by applications with activity after this timestamp
            job_id: Filter by job ID
            status: Filter by application status
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            "created_before": created_before,
            "created_after": created_after,
            "last_activity_after": last_activity_after,
            "job_id": job_id,
            "status": status,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("applications", "list", params)
    async def get(
        self,
        id: Optional[str] = None,
        **kwargs
    ) -> "Application":
        """
        Get an application

        Args:
            id: Application ID
            **kwargs: Additional parameters

        Returns:
            Application
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("applications", "get", params)
class JobsQuery:
    """
    Query class for Jobs resource operations.
    """

    def __init__(self, connector: GreenhouseConnector):
        """Initialize query with connector reference."""
        self._connector = connector

    async def list(
        self,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        **kwargs
    ) -> "dict[str, Any]":
        """
        List jobs

        Args:
            per_page: Number of items to return per page (max 500)
            page: Page number for pagination
            **kwargs: Additional parameters

        Returns:
            dict[str, Any]
        """
        params = {k: v for k, v in {
            "per_page": per_page,
            "page": page,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("jobs", "list", params)
    async def get(
        self,
        id: Optional[str] = None,
        **kwargs
    ) -> "Job":
        """
        Get a job

        Args:
            id: Job ID
            **kwargs: Additional parameters

        Returns:
            Job
        """
        params = {k: v for k, v in {
            "id": id,
            **kwargs
        }.items() if v is not None}

        return await self._connector.execute("jobs", "get", params)