from django.db.models import Model, TextField


class TodoItem(Model):
    text = TextField()

    def to_dict(self):
        return {'id': self.id, 'text': self.text}
