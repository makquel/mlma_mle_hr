import pytest
from structs import Buffer


@pytest.fixture(autouse=True, scope="class")
def items_set(request):
    request.cls._proxy_buffer = []


class TestBuffer(object):
    @classmethod
    def setup_class(cls):
        """Set up the state for any class instance."""
        pass

    @classmethod
    def teardown_class(cls):
        """Teardown the state created in setup_class."""
        pass

    def setup_method(self):
        """Called before every method to setup any state."""
        self.buffer = Buffer("FIFO")

    def teardown_method(self):
        """Called after every method to teardown any state."""
        del self.buffer

    def test_init(self):
        assert self.buffer._policy == "FIFO"


if __name__ == "__main__":
    pytest.main([__file__])
