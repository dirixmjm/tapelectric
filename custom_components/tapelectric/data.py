"""Custom types for tapelectric."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import IntegrationTAPElectricApiClient
    from .coordinator import TAPElectricDataUpdateCoordinator


type IntegrationTAPElectricConfigEntry = ConfigEntry[IntegrationTAPElectricData]


@dataclass
class IntegrationTAPElectricData:
    """Data for the TAPElectric integration."""

    client: IntegrationTAPElectricApiClient
    coordinator: TAPElectricDataUpdateCoordinator
    integration: Integration
