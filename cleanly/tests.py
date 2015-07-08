from django.test import TestCase
from .models import Product
from django.core.urlresolvers import reverse
from registration.users import UserModel

# Create your tests here.

def create_product():
    return Product.objects.create(header='Logo Hoodie',
                                  description='Supersoft fleece',
                                  price='19')

class ProductViewTests(TestCase):
    def test_index_view_with_no_products(self):
        response = self.client.get(reverse('cleanly:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [])

    def test_index_view_with_products(self):
        create_product()
        response = self.client.get(reverse('cleanly:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], ['<Product: Logo Hoodie>'])

    def test_detail_view_with_wrong_product_id(self):
        response = self.client.get(reverse('cleanly:detail', args=(2,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_product_id(self):
        p = create_product()
        response = self.client.get(reverse('cleanly:detail', args=(p.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product'].header, p.header)

    def test_registeration(self):
        resp = self.client.post(reverse('registration_register'),
                                data={'username': 'bob',
                                      'email': 'bob@example.com',
                                      'password1': 'secret',
                                      'password2': 'secret'})
        new_user = UserModel().objects.get(username='bob')
        self.assertEqual(302, resp.status_code)
        self.assertEqual(new_user.email, 'bob@example.com')
        self.failUnless(new_user.is_active)
