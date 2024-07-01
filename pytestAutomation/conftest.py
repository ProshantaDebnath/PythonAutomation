import pytest


@pytest.fixture()
def setup():
    print('Setup method is executing')
    yield
    print('Yield method is executing.')


@pytest.fixture()
def dataLoad():
    print('User Profile data')
    return ["Proshanta", "Debnath", "deb@gmail.com"]


@pytest.fixture(params=["chrome", "Firefox", "IE"])
def crossBrowser(request):
    return request.param
