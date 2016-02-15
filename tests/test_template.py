from gofetch import template

from unittest import TestCase


class RenderTemplateTestCase(TestCase):

    SIMPLE_TEMPLATE = """
SELECT {{ fields }}
FROM {{ database_and_table }}
WHERE {{ condition }}
;"""

    SIMPLE_PARAM_DICT = {
        "fields": "*",
        "database_and_table": "test_db.test",
        "condition": "b > 1"
    }

    def test_render_string(self):
        EXPECTED = """
SELECT *
FROM test_db.test
WHERE b > 1
;"""
        result = template._render_string_template(self.SIMPLE_TEMPLATE, self.SIMPLE_PARAM_DICT)
        self.assertEquals(EXPECTED, result)

    def test_render_file(self):
        # 'simple_template.sql'
        self.fail("test not implemented")
