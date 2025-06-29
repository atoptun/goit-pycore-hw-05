
class ContactNotFound(Exception):
    strerror: str | None
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        if len(args) > 0 and type(args[0]) == str:
            self.strerror = args[0]
