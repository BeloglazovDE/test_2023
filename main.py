###################################################################
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# for i in l:
#         i = 1
# print(l) # Так нельзя, можно итерироваться по индексам
#
# for i in range(len(l)):
#         l[i] = 1
# print(l)
###################################################################
# class Node:
#         def __init__(self, data):
#                 self.data = data
#                 self.left =  None
#                 self.right = None
#
# class BinTree:
#         def __init__(self):
#                 self.root = None
#
#         def __find(self, node, parent, value): # Вспомогательный метод для поиска вершины, куда будем добавлять
#                 if node is None:
#                         return None, parent, False # Если узла нет
#
#                 if value == node.data: # Если значения добавляемого и текущего узла равны, то добавлять ничего не надо
#                         return node, parent, True # Последний True - флаг того, не надо добавлять вершину
#
#                 if value < node.data: # Если значение добавляемого меньше, чем значение текущего узла
#                         if node.left: # Если у текущего узла есть левый потомок
#                                 return self.__find(node.left, node, value)
#
#                 if value > node.data: # Аналогично для правого
#                         if node.right:
#                                 return self.__find(node.right, node, value)
#
#                 return node, parent, False # Если дошли до конца, то добавляем
#
#         def append(self, obj):
#                 if self.root is None: # Если еще нет вершин
#                         self.root = obj
#                         return obj
#
#                 s, p, fl_find = self.__find(self.root, None, obj.data)
#
#                 if not fl_find and s: # Если надо добавить и значение вершины не есть None, то добавляем к ней
#                         if obj.data < s.data:
#                                 s.left = obj
#                         else:
#                                 s.right = obj
#
#                 return obj
#
#         def make_tree_list(self, node, l=[]): # Метод показа дерева обходом в глубину
#                 if node is None:
#                         return
#
#                 self.make_tree_list(node.left, l)
#                 l.append(node.data)
#                 self.make_tree_list(node.right, l)
#
#
#         def __iter__(self):
#                 if self.root is None:
#                         return iter([])
#                 else:
#                         l = []
#                         self.make_tree_list(self.root, l)
#                         return iter(l)
#
# a = BinTree()
# b = BinTree()
# for i in [10, 5, 7, 16, 13, 2, 20]:
#         a.append(Node(i))
#
# for i in b:
#         print(i)
###################################################################
# from pathlib import Path
# import os
#
# class TextLoader:
#     def __init__(self, path):
#         self.path = path
#         if not Path(self.path).is_dir():
#             raise IndexError('Неверный путь')
#
#
#     def __len__(self):
#         return sum([1 for _ in Path(self.path).iterdir()])
#
#     def __getitem__(self, item):
#         return os.listdir(self.path)[item]
#
# a = TextLoader('C:\python\main_project\Python\data')
#
# print(len(a))
# print(a[0])
###################################################################
# class PrintMean(Exception):
#     pass
#
# class PrintDispersion(Exception):
#     pass
#
# class PrintLen(Exception):
#     pass
#
#
# def analytics():
#     print('start')
#     try:
#         while True:
#             try:
#                 l = yield
#                 print(f'Input {l}')
#             except PrintMean:
#                 print('Mean', end=' ')
#                 yield sum(l)/len(l)
#
#             except PrintLen:
#                 print('Length', end=' ')
#                 yield len(l)
#
#             except PrintDispersion:
#                 print('Dispersion', end=' ')
#                 yield round(sum(map(lambda x: x**2/len(l), (map(lambda x: x - sum(l)/len(l), l))))**0.5, 5) # Можно, конечно, и с помощью библиотек
#
#     finally:
#         print('stop')
#
# a = analytics()
# next(a)
# a.send([1, 2, 3, 4])
#
# print(a.throw(PrintLen))
# next(a)
# print(a.throw(PrintDispersion))
# next(a)
# print(a.throw(PrintMean))
# next(a)
#
# a.send([1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# print(a.throw(PrintLen))
# next(a)
# print(a.throw(PrintDispersion))
# next(a)
# print(a.throw(PrintMean))
# next(a)
###################################################################
# def test(a):
#     print('start')
#     try:
#         while True:
#             try:
#                 x = yield
#                 a.append(x)
#             finally:
#                 None
#     finally:
#         print('stop')
#
# A = []
# B = []
#
# a = test(A)
# b = test(B)
#
# try:
#     next(a)
#     next(b)
#     a.send(12)
#     b.send(11)
# except:
#     pass
# print(A, B)

# open('1488.txt', 'w').write('')
class Disconnect(Exception): # Для остановки работы с определенным пользователем
    pass

def write_to_file(f_obj): # На вход нам подали имя файла для соответствующего пользователя
    print(f'start write_to_file({f_obj})')
    # try:
    while True:
        try:
            print('Пускаю запись')
            message = yield
            # print('here')
            print('message = ', message)
            (open(f_obj, 'a').write(message))
        except Disconnect:
            None


w = []
w.append(write_to_file('3.txt'))
next(w[0])
w[0].send('1111')

