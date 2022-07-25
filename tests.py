from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_book_twice_false(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_negative_rating_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', -5)
        assert collector.books_rating['Гордость и предубеждение и зомби']==1

    def test_get_book_rating_books_with_rating_3(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 3)
        collector.get_book_rating('Гордость и предубеждение и зомби')
        assert collector.books_rating['Гордость и предубеждение и зомби'] ==3

    def test_get_books_with_specific_rating_books_with_rating_5(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 5)
        assert 'Что делать, если ваш кот хочет вас убить' in collector.get_books_with_specific_rating(5) and 'Гордость и предубеждение и зомби' in collector.get_books_with_specific_rating(5)

    def test_get_books_rating_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert type(collector.books_rating) is dict

    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.favorites)==2

    def test_add_book_in_favorites_book_not_in_rating(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.favorites

    def test_delete_book_from_favorite_successful_deleting(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' not in collector.favorites

    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert type(collector.favorites) is list and len(collector.favorites)==2