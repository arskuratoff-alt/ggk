from main import filter_by_price, sort_by_price

books = [
    {"title": "Book A", "price": 25.0, "rating": 5},
    {"title": "Book B", "price": 10.0, "rating": 4},
    {"title": "Book C", "price": 15.0, "rating": 3}
]


def test_filter_by_price():
    result = filter_by_price(books, 20)
    assert len(result) == 2


def test_sort_by_price():
    result = sort_by_price(books)
    assert result[0]["price"] == 10.0