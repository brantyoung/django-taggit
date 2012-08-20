django-taggit
=============

和最初 `alex/django-taggit <https://github.com/alex/django-taggit>`_ 的区别
--------------------------------------------------------------------------------

#. 增加 ``TAGGIT_FORCE_LOWERCASE = True`` 配置项，启用后所有标签都会转换成小写对待；
#. 只认中、英文逗号（``，`` 和 ``,``）作为标签的分割符，空格在任何情况下都被认为是标签的一部分。

一般使用方法
--------------

``django-taggit`` 是一个简单易用的 Django 标签 app。把 ``"taggit"`` 加到在你项目中的 ``INSTALLED_APPS`` 中，
然后为你的 model 增加 TaggableManager 就完工了 ::

    from django.db import models

    from taggit.managers import TaggableManager

    class Food(models.Model):
        # ... fields here

        tags = TaggableManager()

接下来你便可以按如下方式使用 API::

    >>> apple = Food.objects.create(name="apple")
    >>> apple.tags.add("red", "green", "delicious")
    >>> apple.tags.all()
    [<Tag: red>, <Tag: green>, <Tag: delicious>]
    >>> apple.tags.remove("green")
    >>> apple.tags.all()
    [<Tag: red>, <Tag: delicious>]
    >>> Food.objects.filter(tags__name__in=["red"])
    [<Food: apple>, <Food: cherry>]

Tags 将会自动显示在表单和后台 admin 中。


``django-taggit`` 依赖 Django 1.1 或更高版本.

For more info checkout out the documentation.  And for questions about usage or
development you can contact the
`mailinglist <http://groups.google.com/group/django-taggit>`_.
