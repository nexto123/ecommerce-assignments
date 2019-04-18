from .models import Category
from .models import Category

#A link that runs throufh all the pages 
def menu_links(request):
	links = Category.objects.all()
	return dict(links=links)