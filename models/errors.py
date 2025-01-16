from typing import Any, List


class Error:
    @property
    def explicit_content(self) -> str:
        return "UnknownError"

    def __str__(self) -> str:
        return "{}: Unexpected error occured".format(
            self.explicit_content
        )

    def as_dict(self) -> dict:
        return dict(
            explicit_content=self.explicit_content
        )


class MissingFieldError(Error):
    @property
    def explicit_content(self) -> str:
        return "MissingFieldError"

    def __init__(self, field: List[str | int]):
        self.field = field

    def __str__(self) -> str:
        return "{}: field '{}' is missing".format(
            self.explicit_content,
            '.'.join(map(str, self.field)),
        )

    def as_dict(self) -> dict:
        return dict(
            explicit_content=self.explicit_content,
            field=self.field
        )


class WrongTypeError(Error):
    @property
    def explicit_content(self) -> str:
        return "WrongTypeError"

    def __init__(self, field: List[str | int], received: type, expected: List[type]):
        self.field = field
        self.received = received
        self.expected = expected

    def __str__(self) -> str:
        return "{}: '{}' should be a(n) {} not '{}'".format(
            self.explicit_content,
            '.'.join(map(str, self.field)),
            [x.__name__ for x in self.expected],
            self.received.__name__
        )

    def as_dict(self) -> dict:
        return dict(
            explicit_content=self.explicit_content,
            field=self.field,
            received=self.received,
            expected=self.expected
        )


class WrongValueError(Error):
    @property
    def explicit_content(self) -> str:
        return "WrongValueError"

    def __init__(self, field: List[str | int], received: Any, expected: List[Any]):
        self.field = field
        self.received = received
        self.expected = expected

    def __str__(self) -> str:
        return "{}: '{}' should be in {} but got '{}' instead".format(
            self.explicit_content,
            '.'.join(map(str, self.field)),
            self.expected,
            self.received
        )

    def as_dict(self) -> dict:
        return dict(
            explicit_content=self.explicit_content,
            field=self.field,
            received=self.received,
            expected=self.expected
        )


class WrongFormatError(Error):
    @property
    def explicit_content(self) -> str:
        return "WrongFormatError"

    def __init__(self, field: List[str | int], received: type, expected: str):
        self.field = field
        self.received = received
        self.expected = expected

    def __str__(self) -> str:
        return "{}: '{}' should be a(n) '{}' but got '{}' instead".format(
            self.explicit_content,
            '.'.join(map(str, self.field)),
            self.expected,
            self.received.__name__
        )

    def as_dict(self) -> dict:
        return dict(
            explicit_content=self.explicit_content,
            field=self.field,
            received=self.received,
            expected=self.expected
        )


class WrongDatetimeFormatError(Error):
    @property
    def explicit_content(self) -> str:
        return "WrongFormatError"

    def __init__(self, field: List[str | int], received: str, format: str):
        self.field = field
        self.received = received
        self.format = format

    def __str__(self) -> str:
        return "{}: '{}' does not follow the '{}' format, got '{}'".format(
            self.explicit_content,
            '.'.join(map(str, self.field)),
            self.format,
            self.received
        )

    def as_dict(self) -> dict:
        return dict(
            explicit_content=self.explicit_content,
            field=self.field,
            format=self.format,
            received=self.received
        )


class RegexError(Error):
    @property
    def explicit_content(self) -> str:
        return "RegexError"

    def __init__(self, field: List[str | int], pattern: str, value: str):
        self.field = field
        self.pattern = pattern
        self.value = value

    def __str__(self) -> str:
        return "{}: '{}' should match pattern '{}' but got '{}'".format(
            self.explicit_content,
            '.'.join(map(str, self.field)),
            self.pattern,
            self.value
        )

    def as_dict(self) -> dict:
        return dict(
            explicit_content=self.explicit_content,
            field=self.field,
            pattern=self.pattern,
            value=self.value
        )


class EmptyStringError(Error):
    @property
    def explicit_content(self) -> str:
        return "EmptyStringError"

    def __init__(self, field: List[str | int]):
        self.field = field

    def __str__(self) -> str:
        return "{}: '{}' return an empty string".format(
            self.explicit_content,
            '.'.join(map(str, self.field))
        )

    def as_dict(self) -> dict:
        return dict(
            explicit_content=self.explicit_content,
            field=self.field
        )


class MinLenghtError(Error):
    @property
    def explicit_content(self) -> str:
        return "MinLenghtError"

    def __init__(self, field: List[str | int], received: int, expected: int):
        self.field = field
        self.received = received
        self.expected = expected

    def __str__(self) -> str:
        return "{}: '{}' got {} values but {} minimum required".format(
            self.explicit_content,
            '.'.join(map(str, self.field)),
            self.received,
            self.expected
        )

    def as_dict(self) -> dict:
        return dict(
            explicit_content=self.explicit_content,
            field=self.field,
            received=self.received,
            expected=self.expected
        )


class MaxLenghtError(Error):
    @property
    def explicit_content(self) -> str:
        return "MaxLenghtError"

    def __init__(self, field: List[str | int], received: int, expected: int):
        self.field = field
        self.received = received
        self.expected = expected

    def __str__(self) -> str:
        return "{}: '{}' got {} values but {} maximum required".format(
            self.explicit_content,
            '.'.join(map(str, self.field)),
            self.received,
            self.expected
        )

    def as_dict(self) -> dict:
        return dict(
            explicit_content=self.explicit_content,
            field=self.field,
            received=self.received,
            expected=self.expected
        )
