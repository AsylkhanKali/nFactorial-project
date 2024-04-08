from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import NewsPost, Category, Comment
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone

def news_grid(request):
    news_list = NewsPost.objects.all().order_by('-date_posted', '-time_posted')

    category_id = request.GET.get('category')
    if category_id:
        news_list = news_list.filter(category__id=category_id)

    query = request.GET.get('q')
    if query:
        news_list = news_list.filter(Q(title__icontains=query) | Q(main_text__icontains=query))

    paginator = Paginator(news_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'current_category_id': int(category_id) if category_id else None,
        'query': query
    }
    return render(request, 'news_grid.html', context)



def news_detail(request, pk):
    news_post = get_object_or_404(NewsPost, pk=pk)
    if request.method == "POST":
        author = "Anonymous"
        text = request.POST.get("comment")
        if text:
            comment = Comment(post=news_post, author=author, text=text, created_date=timezone.now())
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        news_post.views += 1
        news_post.save()

    comments = news_post.comments.all().order_by("-created_date")
    return render(request, 'news_detail.html', {'news_post': news_post, 'comments': comments})