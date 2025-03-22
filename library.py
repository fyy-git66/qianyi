import json
import os

class Book:
    def __init__(self, title, author, isbn, year, status='在库'):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.status = status

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'year': self.year,
            'status': self.status
        }

class Library:
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return [Book(**book) for book in json.load(f)]
        return []

    def save_books(self):
        with open(self.filename, 'w') as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def add_book(self, book):
        if any(b.isbn == book.isbn for b in self.books):
            print("错误：ISBN已存在！")
            return
        self.books.append(book)
        self.save_books()
        print("图书添加成功！")

    def delete_book(self, isbn):
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                del self.books[i]
                self.save_books()
                print("图书删除成功！")
                return
        print("错误：找不到该ISBN的图书")

    def search_book(self, keyword):
        results = []
        for book in self.books:
            if keyword.lower() in (book.title.lower() or 
                                  book.author.lower() or 
                                  book.isbn.lower()):
                results.append(book)
        return results

    def display_books(self):
        if not self.books:
            print("当前没有图书记录")
            return
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book.title} - {book.author} ({book.year})")
            print(f"   ISBN: {book.isbn} 状态: {book.status}")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == '在库':
                    book.status = '已借出'
                    self.save_books()
                    print("借书成功！")
                else:
                    print("该图书已被借出")
                return
        print("错误：找不到该ISBN的图书")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == '已借出':
                    book.status = '在库'
                    self.save_books()
                    print("还书成功！")
                else:
                    print("该图书无需归还")
                return
        print("错误：找不到该ISBN的图书")

def main():
    library = Library()
    
    while True:
        print("\n===== 图书管理系统 =====")
        print("1. 添加图书")
        print("2. 删除图书")
        print("3. 搜索图书")
        print("4. 显示所有图书")
        print("5. 借阅图书")
        print("6. 归还图书")
        print("0. 退出系统")
        
        choice = input("请选择操作：")
        
        if choice == '1':
            title = input("请输入书名：")
            author = input("请输入作者：")
            isbn = input("请输入ISBN：")
            year = input("请输入出版年份：")
            library.add_book(Book(title, author, isbn, year))
        
        elif choice == '2':
            isbn = input("请输入要删除的图书ISBN：")
            library.delete_book(isbn)
        
        elif choice == '3':
            keyword = input("请输入搜索关键词（书名/作者/ISBN）：")
            results = library.search_book(keyword)
            if results:
                print("\n=== 搜索结果 ===")
                for book in results:
                    print(f"{book.title} - {book.author} ({book.year})")
                    print(f"ISBN: {book.isbn} 状态: {book.status}")
            else:
                print("未找到相关图书")
        
        elif choice == '4':
            print("\n=== 所有图书 ===")
            library.display_books()
        
        elif choice == '5':
            isbn = input("请输入要借阅的图书ISBN：")
            library.borrow_book(isbn)
        
        elif choice == '6':
            isbn = input("请输入要归还的图书ISBN：")
            library.return_book(isbn)
        
        elif choice == '0':
            print("感谢使用，再见！")
            break
        
        else:
            print("无效的输入，请重新选择")

if __name__ == "__main__":
    main()




##fruits = ["apple","banana","cherry"]
##
##for index, fruit in enumerate(fruits,start=1):
##   print(f"第{index}个水果是{fruit}")


#     [ 遍历开始 ]
##↓
##for 当前图书 in 所有现存图书:
##   ↓
##   检查 当前图书.isbn == 新书.isbn
##   ↓
##   将比较结果(True/False)传递给any()
##↓
##[ 遍历结束 ]
##↓
##any()判断是否存在至少一个True'''
##
##    #完成CRUD操作的函数的编写
##    #存入书籍
######



##            if keyworld.strip():
##                break



























