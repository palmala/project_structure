from package1.common import helpers
from package1.subpackage1 import feature1
import inspect


def feature2() -> str:
    return str(helpers.func1()) + str(feature1.feature1())
