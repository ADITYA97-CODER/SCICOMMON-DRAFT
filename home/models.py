from django.db import models
from django.contrib.auth.models import User
class Note(models.Model):
     note_id = models.CharField(max_length=100, unique=True, null=True,blank=True,
                                help_text="Required. Alphanumeric characters only.")
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     def __str__(self):
         return self.note_id

class comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.author.username}'s comment on {self.created_at}"

    def get_children(self):
        return comment.objects.filter(parent=self)

    def has_children(self):
        return comment.objects.filter(parent=self).exists()

    class Meta:
        ordering = ['-created_at']
    
    # Other fields for the note, such as title and content, can be added here
    
