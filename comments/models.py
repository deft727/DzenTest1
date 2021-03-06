from django.db import models
from django.conf import settings


from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Post(models.Model):

    class Meta:
        verbose_name = 'Пост'

    author = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Автор коммента',on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name='Заголовок Поста')
    text = models.TextField()
    comments = GenericRelation('comment')

    def __str__(self):
        return self.title


class Comment(models.Model):

    class Meta:
        verbose_name = 'Коммент'

    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Автор коммента',on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст комментария')
    parent = models.ForeignKey(
                                    'self',
                                    verbose_name='Комментарий родителя',
                                    blank=True,null=True,related_name='children',
                                    on_delete=models.CASCADE
                                )
    child = models.BooleanField(default=False)
    # 
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now=True,verbose_name='Дата создания комментария')

    def __str__(self): 
        return str(self.id)

    @property
    def get_parent(self):
        if  not self.parent:
            return ""
        return self.parent