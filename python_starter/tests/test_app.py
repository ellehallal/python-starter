import pytest
from python_starter.app import App


class TestApp:

    def test_run(self):
        app = App()
        message = app.run()
        assert "Hello world!" in message
