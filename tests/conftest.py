# pylint: disable=redefined-outer-name
from pytest_socket import disable_socket


def pytest_runtest_setup() -> None:
    disable_socket()
