import unittest
import identidock

class TestCase(unittest.TestCase):

    # initialize flask app
    def setUp(self):
        identidock.app.config["TESTING"] = True
        self.app = identidock.app.test_client()

    # send "moby dock" to name field
    # check response data . it include "hello" and "Moby dock"
    def test_get_mainpage(self):
        page = self.app.post("/", data=dict(name="Moby Dock"))
        assert page.status_code == 200
        assert 'Hello' in str(page.data)
        assert 'Moby Dock' in str(page.data)

    # escape test
    def test_html_escaping(self):
        page = self.app.post("/", data=dict(name='"><b>TEST</b><!--'))
        assert '<b>' not in str(page.data)

if __name__ == '__main__':
    unittest.main()
