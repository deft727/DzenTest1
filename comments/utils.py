
def get_children(qs_child):
    res=[]
    for comment in qs_child:

        com = {
            'id': comment.id,
            'text':comment.text,
            'timestamp':comment.timestamp.strftime('%Y-%m-%d %H:%m'),
            'author':comment.user,
            'is_child':comment.child,
            'parent_id':comment.get_parent
            }
        if comment.children.exists():
            com['children'] = get_children(comment.children.all())
        res.append(com)
    return res
            


def create_comment_tree(qs):
    res = []
    for comment in qs:
        com = {
            'id': comment.id,
            'text':comment.text,
            'timestamp':comment.timestamp.strftime('%Y-%m-%d %H:%m'),
            'author':comment.user,
            'is_child':comment.child,
            'parent_id':comment.get_parent
            }
        if comment.children:
            com['children'] = get_children(comment.children.all())
        if not comment.child:
            res.append(com)

    # print(res,'create')
    return res

