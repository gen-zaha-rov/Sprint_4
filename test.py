import pytest
from main import BooksCollector 


class TestBook:

    @pytest.fixture
    def collector(self):
        return BooksCollector()
    

    def test_add_new_book_valid_name(self, collector):  #тест на добавление новой книги с валидным названием
        collector.add_new_book('Форма жизни №4')
        assert 'Форма жизни №4' in collector.books_genre


    def test_add_new_book_invalid_name(self, collector):  #тест на добавление новой книги с невалидным названием
        collector.add_new_book('')
        collector.add_new_book('x' * 41)
        assert len(collector.books_genre) == 0 


    def test_add_new_book_twice(self,collector):  #тест на добавление новой книги дважды 
        collector.add_new_book('Отцы и дети')
        collector.add_new_book('Отцы и дети')
        cnt_books = len(collector.get_books_genre())
        assert cnt_books == 1


    def test_set_book_genre_valid(self, collector):  #тест на добавление книги с валидным жанром
        collector.add_new_book('Этюд в багровых тонах')
        collector.set_book_genre('Этюд в багровых тонах', 'Детективы')
        assert collector.books_genre['Этюд в багровых тонах'] == 'Детективы'  


    def test_set_book_genre_invalid(self, collector):  #тест на добавление книги с невалидным жанром
        collector.add_new_book('SuperBetter')
        collector.set_book_genre('SuperBetter', 'Психология')
        assert collector.books_genre['SuperBetter'] == '' 


    def test_get_books_with_specific_genre(self, collector):  #тест на вывод книг с определённым жанром
        collector.add_new_book('Оно')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Дракула', 'Ужасы')
        books = collector.get_books_with_specific_genre('Ужасы')
        assert len(books) == 2
        assert 'Оно' in books
        assert 'Дракула' in books


    def test_get_books_genre(self, collector):  #тест на получение словаря books_genre
        collector.add_new_book('Колобок')
        assert collector.get_books_genre() == {'Колобок': ''}       


    def test_get_books_for_children(self, collector):  #тест на то, что в подборку для детей попадают рарзрешенные жанры и не попадают запрещённые
        collector.add_new_book('Детская книга')
        collector.add_new_book('Взрослая книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        collector.set_book_genre('Взрослая книга', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Детская книга' in children_books
        assert 'Взрослая книга' not in children_books


    def test_add_book_in_favorites(self, collector):  #тест на добавление книги в список Избранных 
        collector.add_new_book('Война миров')
        collector.set_book_genre('Война миров', 'Фантастика')
        collector.add_book_in_favorites('Война миров')
        assert 'Война миров' in collector.get_list_of_favorites_books()   


    def test_delete_book_from_favorites(self, collector):  #тест на удаление книги из списка Избранных
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('Горе от ума', 'Комедии')
        collector.add_book_in_favorites('Горе от ума')
        collector.delete_book_from_favorites('Горе от ума')
        assert 'Горе от ума' not in collector.get_list_of_favorites_books()	                             