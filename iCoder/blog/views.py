from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import get_dict

# Create your views here.

def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request, 'blog/blogHome.html', context)
    #return HttpResponse("BLOG home")

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    repDict = {}
    for reply in replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno] = [reply]
        else:
            repDict[reply.parent.sno].append(reply)

    #print(comments, replies)
    print(repDict)
    context = {'post':post, 'comments':comments, 'user':request.user, 'replyDict':repDict}
    return render(request, 'blog/blogPost.html', context)
    #return HttpResponse(f"This is blogPOST {slug}")

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')

        if parentSno == '':
            comment = BlogComment(user=user, comment=comment, post=post)
            comment.save()
            messages.success(request, "Your comment has posted Successfully!")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(user=user, comment=comment, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has posted Successfully!")

        return redirect(f'/blog/{post.slug}')
            