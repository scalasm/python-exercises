from typing import List, Any
import re


class IpAddress:
    """Simple class representing an IPV4 address"""
    def __init__(self, *args):
        self._octets = args

    def is_valid(self) -> bool:
        if len(self._octets) != 4:
            return False

        for octet in self._octets:
            if not (octet >= 0 and octet <= 255):
                return False
        return True

    def __getitem__(self, index: int) -> int:
        if index < 0 or index > 4:
            raise IndexError( "Valid Index is between 0 and 3 included!" )
        
        return self._octets[index]

    @classmethod
    def from_str(cls, ip_as_string: str) -> Any:
        ip_address_pattern = re.compile( r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})" )
        octet_matches = ip_address_pattern.match( ip_as_string )
        
        octets = [int(group) for group in octet_matches.groups()]

        return cls(*octets)
