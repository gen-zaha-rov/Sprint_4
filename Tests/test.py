import pytest
from main import BooksCollector 


class TestBook:

    def test_add_new_book_valid_name(self, collector):  #тест на добавление новой книги с валидным названием
        collector.add_new_book('Форма жизни №4')
        assert 'Форма жизни №4' in collector.books_genre

    @pytest.mark.parametrize('name', 
                             [
    '',
    'Очень длинное название книги, которое больше 40 символов'
])
    
    def test_add_new_book_invalid_names(self, collector, name):  #тест на добавление новой книги с невалидными названиями
        initial_books_count = len(collector.get_books_genre())
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == initial_books_count


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


@pytest.mark.parametrize('book_to_remove, initial_favorites, expected_favorites', [
    # Удаление существующей книги
    ('Anna Karenina', ['Anna Karenina', 'War and Peace'], ['War and Peace']),
    # Попытка удаления несуществующей книги
    ('Crime and Punishment', ['Anna Karenina', 'War and Peace'], ['Anna Karenina', 'War and Peace']),
    # Удаление из пустого списка
    ('Anna Karenina', [], []),
    # Удаление с учетом регистра
    ('anna karenina', ['Anna Karenina'], ['Anna Karenina']),
    # Удаление пустой строки
    ('', ['Anna Karenina', ''], ['Anna Karenina']),
])
def test_delete_book_from_favorites(collector, book_to_remove, initial_favorites, expected_favorites):  #тест на удаление книг из списка Избранных
    # устанавливаем начальное состояние избранных книг
    collector.favorites = initial_favorites.copy()
    
    # пытаемся удалить книгу
    collector.delete_book_from_favorites(book_to_remove)
    
    # убеждаемся, что список избранного соответствует ожиданиям
    assert collector.get_list_of_favorites_books() == expected_favorites
                          