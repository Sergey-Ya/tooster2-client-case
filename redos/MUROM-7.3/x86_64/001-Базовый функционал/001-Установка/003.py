from apps.build.lib import testinglib, buildlib

class TestCase(testinglib.BaseTestCase):

    def __init__(self):
        super().__init__()
        self.CASE_MODE = 'auto'
        self.CASE_IS_TRACKED = False
        self.CASE_NAME = 'test_case'
        self.CASE_NAME_TITLE = 'test case'
        self.CASE_PACKAGES_USED = []
        self.CASE_HOSTS = [
            self.Host()
        ]

    def set_up(self):
        self.HOST1 = self.CASE_HOSTS[0]
        self.ROOT1 = self.HOST1.root

    def testing(self):
        pass

