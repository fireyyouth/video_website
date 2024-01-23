import json
import jieba
from app.models import Preview

preview_list = []
data = json.load(open('init_data.json'))
for item in data:
    preview = Preview(title=item['title'], img=item['img'])
    preview.title_tsvector = ' '.join(jieba.cut(preview.title, cut_all=True))
    preview_list.append(preview)
    
Preview.objects.bulk_create(preview_list)