from dataclasses import dataclass


@dataclass
class SteamGame:
    appName: str
    appId: int

    # Minimal price, in cents.
    minimal_cent: int
