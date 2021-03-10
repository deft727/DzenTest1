# занимается исключительно тем что ищет есть ли дети у обьекта
def get_children(qs_child):
    res=[]
    # итерируемя по кверисету
    for comment in qs_child:

        com = {
            'id': comment.id,
            'text':comment.text,
            'timestamp':comment.timestamp.strftime('%Y-%m-%d %H:%m'),
            'author':comment.user,
            'is_child':comment.child,
            'parent_id':comment.get_parent
            }
            # если есть дети добавляем в наш дикт чилдрен и добавляем в список наш новый коммент
        if comment.children.exists():
            com['children'] = get_children(comment.children.all())
        res.append(com)
    return res
            

# create_comment_tree основная ф-я , итерируемся по кверисету не зная есть ли дети,создаем дикт
# дальше првоеряем есть ли дети, если есть то создаем ключ чилдрен и записываем туда рез работы гет чилдрен
# 
def create_comment_tree(qs):
    res = []
    # у каждого коммента есть набор аттрибутов из который формируем список
    for comment in qs:
        com = {
            'id': comment.id,
            'text':comment.text,
            # метод дейтайтам обьекта (strftime в каком виде хочу представить)
            'timestamp':comment.timestamp.strftime('%Y-%m-%d %H:%m'),
            'author':comment.user,
            'is_child':comment.child,
            # не можеи обратиться напрямую comment.parent.id если нету будет ошибка
            # делаем в можели ф-ю которая возвращет пустую строку или парента
            'parent_id':comment.get_parent
            }
        if comment.children:
            # есть ли у этого коментария дети,если есть записываем в ключ результат работы ф-и get_children
            com['children'] = get_children(comment.children.all())
            #
        if not comment.child:
            res.append(com)

    # print(res,'create')
    return res

