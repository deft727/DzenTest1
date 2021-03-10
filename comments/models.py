from django.db import models
from django.conf import settings


from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

# сущность к которой приерепляться cоntenttype
class Post(models.Model):

    class Meta:
        verbose_name = 'Пост'
    author = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Автор коммента',on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name='Заголовок Поста')
    text = models.TextField()
                # прикреплять коментарии
    comments = GenericRelation('comment')

    def __str__(self):
        return self.title


class Comment(models.Model):

    class Meta:
        verbose_name = 'Коммент'
                                #дефолтная модель юзера
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Автор коммента',on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст комментария')
    parent = models.ForeignKey(
                                    #селф- в создавшемся инстансе (коммент) есть набор полей юзер,текст,парент
                                    #и в парентах у него может быть (у нового) другой обьект в качестве параметра
                                    #(обьекты ссылаются сами на себя)
                                    'self',
                                    verbose_name='Комментарий родителя',
                                    blank=True,null=True,related_name='children',
                                    on_delete=models.CASCADE
                                )
    child = models.BooleanField(default=False)
    # можно подвязаться к любой сущности (галерея,пост,указав внешний ключ и инстанс ид(object_id) )
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    # инстанс ид конкретной модели которой одвязываеся   
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now=True,verbose_name='Дата создания комментария')

    def __str__(self): 
        return str(self.id)

#  позволит обращаться к "вычисляемым" свойствам не как к функциям, а как к атрибутам
# для гет
    @property
    def get_parent(self):
        if  not self.parent:
            return ""
        return self.parent