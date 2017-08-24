from __future__ import unicode_literals
# from ..login_app.models import User
from django.db import models

# Create your models here.
class ItemManager(models.Manager):
    def itemVal(self, postdata):
        results = {'status': False, 'errors': []}
        if not postdata['item'] or len(postdata['item']) <1:
            results['errors'].append('item must be more then 1 character')
            results['status'] = True
        if results['status'] == False:
            if len(self.filter(item = postdata['item'])) == 0:
                results['item'] = self.create(item = postdata['item'])
            else:
                results['errors'].append('item is already on wish list')
                results['status'] = True
        print postdata['item']
        return results

class Item(models.Model):
    item = models.CharField(max_length= 255)
    created_at = models.DateTimeField(auto_now_add= True)
    objects = ItemManager()