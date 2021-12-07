class Property:
    def __init__(
        self,
        *,
        name: str,
        column: str,
        primary_key: bool = False,
        read_only: bool = False
    ):
        self.name = name
        self.column = column
        self.primary_key = primary_key
        self.read_only = read_only
