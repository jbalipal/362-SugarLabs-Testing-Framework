import pytest

def pytest_addoption(parser):
	parser.addoption("--cmdInput", action="append", default=[], help="inputs go here")

def pytest_generate_tests(metafunc):
	if 'cmdInput' in metafunc.fixturenames:
		metafunc.parametrize("cmdInput", metafunc.config.getoption('cmdInput'))
