import pytest
from project.oop.basic import BasicBranches
from project.env import APP_API_BRANCH_1, APP_API_BRANCH_2

def test_basic_branches():
    pathnames = [APP_API_BRANCH_1, APP_API_BRANCH_2]
    branches = BasicBranches(pathnames)
    assert branches.pathnames == pathnames
    assert BasicBranches.validate(pathnames) == True


    pathnames = [APP_API_BRANCH_1, 103]
    with pytest.raises(ValueError) as exc_info:
        BasicBranches(pathnames)
    assert '[Error]: What something wrong at "BasicPostman" from the "basic.py".' in str(exc_info.value)

