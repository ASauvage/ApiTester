

class Error:
    @property
    def explicit_content(self):
        return "UnknownError"

    def __str__(self):
        return "{}: Unexpected error occured".format(
            self.explicit_content
        )

    def as_dict(self):
        return dict(
            explicit_content=self.explicit_content
        )


class MissingFieldError(Error):
    @property
    def explicit_content(self):
        return "MissingFieldError"

    def __init__(self, field):
        self.field = field

    def __str__(self):
        return "{}: field '{}' is missing".format(
            self.explicit_content,
            self.field
        )

    def as_dict(self):
        return dict(
            explicit_content=self.explicit_content,
            field=self.field
        )


class WrongTypeError(Error):
    @property
    def explicit_content(self):
        return "WrongTypeError"

    def __init__(self, field, received, expected):
        self.field = field
        self.received = received
        self.expected = expected

    def __str__(self):
        return "{}: '{}' should be a(n) {} not {}".format(
            self.explicit_content,
            self.field,
            self.expected,
            self.received
        )

    def as_dict(self):
        return dict(
            explicit_content=self.explicit_content,
            field=self.field,
            received=self.received,
            expected=self.expected
        )


class WrongValueError(Error):
    @property
    def explicit_content(self):
        return "WrongValueError"

    def __init__(self, field, received, expected):
        self.field = field
        self.received = received
        self.expected = expected

    def __str__(self):
        return "{}: '{}' should be in {} but got '{}' instead".format(
            self.explicit_content,
            self.field,
            self.expected,
            self.received
        )

    def as_dict(self):
        return dict(
            explicit_content=self.explicit_content,
            field=self.field,
            received=self.received,
            expected=self.expected
        )


class RegexError(Error):
    @property
    def explicit_content(self):
        return "RegexError"

    def __init__(self, field, pattern):
        self.field = field
        self.pattern = pattern

    def __str__(self):
        return "{}: '{}' should match pattern '{}'".format(
            self.explicit_content,
            self.field,
            self.pattern
        )

    def as_dict(self):
        return dict(
            explicit_content=self.explicit_content,
            field=self.field,
            pattern=self.pattern
        )


class MinLenghtError(Error):
    @property
    def explicit_content(self):
        return "MinLenghtError"

    def __init__(self, field, received, expected):
        self.field = field
        self.received = received
        self.expected = expected

    def __str__(self):
        return "{}: '{}' got {} values but {} minimum required".format(
            self.explicit_content,
            self.field,
            self.received,
            self.expected
        )

    def as_dict(self):
        return dict(
            explicit_content=self.explicit_content,
            field=self.field,
            received=self.received,
            expected=self.expected
        )


class MaxLenghtError(Error):
    @property
    def explicit_content(self):
        return "MaxLenghtError"

    def __init__(self, field, received, expected):
        self.field = field
        self.received = received
        self.expected = expected

    def __str__(self):
        return "{}: '{}' got {} values but {} maximum required".format(
            self.explicit_content,
            self.field,
            self.received,
            self.expected
        )

    def as_dict(self):
        return dict(
            explicit_content=self.explicit_content,
            field=self.field,
            received=self.received,
            expected=self.expected
        )
