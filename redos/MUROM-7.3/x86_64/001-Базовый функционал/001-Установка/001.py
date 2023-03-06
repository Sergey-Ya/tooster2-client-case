from apps.build.lib import testinglib, buildlib

class TestCase(testinglib.BaseTestCase):

    def __init__(self):
        super().__init__()
        self.CASE_NAME = 'deploy_base_packages'
        self.CASE_NAME_TITLE = 'Развертывание с базовым набором пакетов'
        self.CASE_ENV_LST = [buildlib.ENV_ALL]
        self.CASE_ENV_PKGS = [buildlib.PKGS_BASE]
        self.CASE_HOSTS = [
            self.Host()
        ]

    def set_up(self):
        self.HOST1 = self.CASE_HOSTS[0]
        self.USER1 = self.HOST1.create_user()

    def testing(self):
        x_session = self.HOST1.gdm_auth(self.USER1)
        sealert_app = x_session.run_app('sealert')
        self.HOST1.screen.find_text('Оповещений нет', lang='rus', window=sealert_app.window)
