from package1.common.helpers import func1
from package1.subpackage1.feature1 import feature1


def feature2() -> str:
    return str(func1()) + str(feature1())
