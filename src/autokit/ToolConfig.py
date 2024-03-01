from typing import Dict, NamedTuple

from autokit import PlatformData


class ToolConfig(NamedTuple):
    """
    A class to represent the configuration for a tool.

    Attributes
    ----------
    tool_name : str
        The name of the tool.
    platform_data : Dict[str, PlatformData]
        The platform data for the tool.
    python : bool
        Whether the tool should be executed by the Python interpreter.
    """
    tool_name: str
    platform_data: Dict[str, PlatformData]
    python: bool
