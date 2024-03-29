from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

# test_main_url_is_exist adalah tes untuk mengecek apakah path URL /main/ dapat diakses.
# test_main_using_main_template adalah tes untuk mengecek apakah halaman /main/ di-render menggunakan template main.html.