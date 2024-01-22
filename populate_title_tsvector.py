import jieba
from django.contrib.postgres.search import SearchVector
from django.db.models import Value

def populate(all):
    for item in all:
        tokens = ' '.join(jieba.cut(item.title, cut_all=True))
        item.title_tsvector = Value(tokens)
        item.save()
        