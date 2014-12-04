from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    affiliation = models.CharField(max_length=40)
      
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)




class AcadmicPaper(models.Model):
    page_no = models.IntegerField(max_length=5, primary_key=True)
    paper_abstract = models.CharField(max_length=100)
    paper_title = models.CharField(max_length=50)
    cancer_paper = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    
    def __unicode__(self):
        return u'%s %s' % (self.title, self.abstract)
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher_info = models.CharField(max_length=100)
    the_editor = models.CharField(max_length=100)
    the_editor_info = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, primary_key=True)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title
    

class Conference(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    location = models.CharField(max_length=100)
    conference_year = models.DateField()

    def __unicode__(self):
        return self.title
    

class Journal(models.Model):
    title = models.CharField(max_length=100)
    isbn_j = models.CharField(max_length=13, primary_key=True)
    publication_info = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title
    
class JournalPaper(models.Model):
    page_no = models.ForeignKey(AcadmicPaper)
    vol = models.CharField(max_length=50)
    isbn = models.ForeignKey(Journal)
    year = models.DateField()

    def __unicode__(self):
        return self.vol
    
    
class BookChapterPaper(models.Model):
    page_no = models.ForeignKey(AcadmicPaper)
    isbn = models.ForeignKey(Book)
    

    def __unicode__(self):
        return self.isbn
    
    
class ConferencePaper(models.Model):
    page_no = models.ForeignKey(AcadmicPaper)
    title = models.ForeignKey(Conference)
    

    def __unicode__(self):
        return self.title
    
