import pytest
from project.oop.postmane import Postmen

@pytest.mark.asyncio
async  def test_compare_version_release():
	# Test on returns a list. It's list contain more than one list
	packages_sisyphus = [
		{'name': '0ad', 'version': '0.0.26', 'release': 'alt0_9_alpha'},
		{'name': '0ad-debuginfo', 'version': '0.0.26', 'release': 'alt0_9_alpha'},
		{'name': '389-ds-base', 'version': '2.4.5', 'release': 'alt1'}
	]
	packages_p10 = [
		{'name': '0ad', 'version': '0.0.25', 'release': 'alt0_9_alpha'},
		{'name': '0ad-debuginfo', 'version': '0.0.25', 'release': 'alt0_9_alpha'},
		{'name': '389-ds-base', 'version': '2.4.4', 'release': 'alt1'}
	]

	result = await Postmen.compare_version_release(packages_sisyphus, packages_p10)
	assert isinstance(result, dict)
	assert len(result) >= 2

	# Test that long lists returned
	assert len(result[0].keys()[0]) == "sisyphus"
	assert len(result[1].keys()[0]) == "p10"