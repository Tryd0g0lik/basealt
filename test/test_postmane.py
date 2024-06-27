import pytest
import aiohttp
from aiohttp import web
from project.oop.postmane import Postmen
from project.oop.basic import BasicBranches

@pytest.fixture
def aiohttp_client():
	session = aiohttp.ClientSession()
	return session

@pytest.mark.asyncio
async def test_get_api_request(aiohttp_client):
    # Set up mock server
    async def handle(request):
        return web.json_response({'data': 'mock_data'})

    app = web.Application() # server
    app.router.add_get('/api/sisyphus/', handle)
    app.router.add_get('/api/p10/', handle)
    client = await aiohttp_client(app)

    # Test the get_api_request method
    pathnames = ['sisyphus/', 'p10/']
    postmen = Postmen(pathnames)
    data = await postmen.get_api_request('http://localhost:{}/api/'.format(client.server.port))

    assert isinstance(data, list)
    assert len(data) == 2
    assert all(isinstance(item, dict) for item in data)
    assert all('data' in item and item['data'] == 'mock_data' for item in data)

    # Test error handling
    pathnames = ['sisyphus/', 'invalid/']
    postmen = Postmen(pathnames)
    with pytest.raises(ValueError) as exc_info:
        await postmen.get_api_request('http://localhost:{}/api/'.format(client.server.port))
    assert '[Error.message]:' in str(exc_info.value)
