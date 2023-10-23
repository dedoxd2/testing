import pytest
from app1.models import Product


@pytest.mark.parametrize("title, category, description, slug, reqular_price, discount_price, validity",
                         [
                             ("New Title", 1, "New Description",
                              "slug", "4.99", "3.99", True),
                             ("", 1, "New Description",
                              "slug", "4.99", "3.99", True),
                             ("New Title", 1, "", "slug", "4.99", "3.99", True),
                             ("New Title", 1, "New Description",
                              "", "4.99", "3.99", True),
                             ("New Title", 1, "New Description",
                              "slug", "", "3.99", False),
                             ("New Title", 1, "New Description",
                              "slug", "4.99", "", False),

                         ]
                         )
def test_product_instance(db, product_factory, title, category, description, slug, reqular_price, discount_price, validity):

    test = product_factory(title=title, category_id=category, description=description,
                           slug=slug, reqular_price=reqular_price, discount_price=discount_price)
    item = Product.objects.all().count()
    print(item)

    assert item == validity
