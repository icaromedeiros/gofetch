from gofetch import template

from unittest import TestCase


class RenderTemplateTestCase(TestCase):

    SIMPLE_TEMPLATE = """
    SELECT {{ fields }}
    FROM {{ database_and_table }}
    WHERE {{ conditions }}
    ;
    """

    SIMPLE_PARAM_DICT = {
        "fields": "*",
        "database_and_table": "test_db.test",
        "condition": "b > 1"
    }

    def test_simple_rendering(self):
        EXPECTED = """
        SELECT {{ fields }}
        FROM {{ database_and_table }}
        WHERE {{ conditions }}
        """
        result = template.render(self.SIMPLE_TEMPLATE, self.SIMPLE_PARAM_DICT)
        self.assertEquals(EXPECTED, result)
