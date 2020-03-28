import re
from unittest import TestCase as BaseTestCase


class TestCase(BaseTestCase):
    def assertRegexIn(self, expected_regex, container, message=None):
        if isinstance(expected_regex, str):
            expected_regex = re.compile(expected_regex)

        found_match = False
        for item in container:
            if expected_regex.search(item):
                found_match = True
                break

        if not found_match:
            error_message = (
                f"Regex didn't match: {expected_regex.pattern} not found in {container}"
            )
            raise self.failureException(error_message)
