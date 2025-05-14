from django.db import models

class Author(models.Model):
    name = models.CharField(
        max_length=50)
    surname = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    album_count = models.PositiveIntegerField(
        default=0,
    )
    image = models.ImageField(
        upload_to='authors',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'



class Song(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    song_image = models.ImageField(upload_to='songs/image')
    file = models.FileField(upload_to='songs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
       return self.name

    class Meta:
       verbose_name = 'Song'
       verbose_name_plural = 'Songs'



class Proposal(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'