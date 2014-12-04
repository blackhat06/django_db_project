from django.contrib import admin

# Register your models here.
from .models import Author, Book, Conference, Journal, AcadmicPaper, BookChapterPaper, JournalPaper

class AuthorAdmin(admin.ModelAdmin):
    class Meta:
        model = Author
        
admin.site.register(Author,AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    class Meta:
        model = Book
        
admin.site.register(Book,BookAdmin)

class ConferenceAdmin(admin.ModelAdmin):
    class Meta:
        model = Conference
        
admin.site.register(Conference,ConferenceAdmin)

class JournalAdmin(admin.ModelAdmin):
    class Meta:
        model = Journal
        
admin.site.register(Journal,JournalAdmin)

class AcadmicPaperAdmin(admin.ModelAdmin):
    class Meta:
        model = AcadmicPaper
        
admin.site.register(AcadmicPaper,AcadmicPaperAdmin)




class BookChapterPaperAdmin(admin.ModelAdmin):
    class Meta:
        model = BookChapterPaper
        
admin.site.register(BookChapterPaper,BookChapterPaperAdmin)



class JournalPaperAdmin(admin.ModelAdmin):
    class Meta:
        model = JournalPaper
        
admin.site.register(JournalPaper,JournalPaperAdmin)





