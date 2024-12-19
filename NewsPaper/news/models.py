from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def update_rating(self):
        posts_rating = 0
        comments_rating = 0
        posts_comments_rating = 0
        posts = Post.objects.filter(author=self)
        for p in posts:
            posts_rating += p.rating
        comments = Comment.objects.filter(user=self.user)
        for c in comments:
            comments_rating += c.rating
        posts_comments = Comment.objects.filter(post__author=self)
        for pc in posts_comments:
            posts_comments_rating += pc.rating

        print(posts_rating)
        print("-------------")
        print(comments_rating)
        print("-------------")
        print(posts_comments_rating)

        self.rating = posts_rating * 3 + comments_rating + posts_comments_rating
        self.save()


class Category(models.Model):
    name_category = models.CharField(max_length=255, default="Default", unique=True)


class Post(models.Model):
    some_datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    PostNews = 'PN'
    PostArticle = 'PA'
    POSITIONS = [(PostArticle, 'Статья'), (PostNews, 'Новость'), ]

    title = models.CharField(max_length=50, verbose_name='Название')
    text = models.TextField()
    rating = models.IntegerField(default=0)
    positions = models.CharField(max_length=2, choices=POSITIONS, default=PostArticle, verbose_name='Тип поста')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f"{self.text[0:124]}..."


class PostCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    some_datetime = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
