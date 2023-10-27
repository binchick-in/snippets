from typing import Any


class DictWrapper:
    """Light weight dictionary wrapper to allow for dot
    access to keys and values. Supports nested dictionaries.

    Example Usage:

    >>> data = {"foo": "bar","bin": {"baz": 1}}
    >>> d = DictWrapper(data)
    >>> d.foo
    'bar'
    >>> d.bin.baz
    1
    """

    def __init__(self, data: dict[Any, Any]):
        self._data = data

    def __getattr__(self, key: Any) -> Any:
        if not self._data.get(key):
            raise KeyError(f"{key} not found in root data")

        if isinstance(self._data[key], dict):
            return DictWrapper(self._data[key])

        return self._data.get(key)
