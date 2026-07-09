from django.db import models


class ContactMessage(models.Model):
    """A message submitted through the public contact form."""

    SUBJECT_CHOICES = [
        ('admissions', 'Admissions'),
        ('academics', 'Academics'),
        ('administration', 'Administration'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='other')
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f'{self.name} — {self.get_subject_display()} ({self.submitted_at:%d %b %Y})'
