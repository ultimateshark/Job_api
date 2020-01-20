from django.shortcuts import render
from ratelimit.decorators import ratelimit
from django.http import JsonResponse
from .models import AllPosts
import math
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from random import randint
# Create your views here.
def GenerateJobId():
    allids=AllPosts.objects.values('job_id').all()
    new_id=randint(10000,99999)
    while True:
        if new_id not in allids:
            break
        else:
            new_id=randint(10000,99999)
    return new_id


@csrf_exempt
@ratelimit(key='ip',rate='100/h')
def Getpostpage(request):
    try:
        limit,page=25,1
        if request.GET.get('limit'):
            limit=int(request.GET.get('limit'))
            if limit<=1:
                return JsonResponse({'code':103,'message':'Invalid Limit','description':'The Limit Set Is Invalid'})
        if request.GET.get('page'):
            page=int(request.GET.get('page'))
            if page<1:
                return JsonResponse({'code':104,'message':'Invalid Page','description':'The Page Requested for could not be found on the server'})
        try:
            posts=AllPosts.objects.all()
            total=math.ceil(len(posts)/limit)
            pages=[x for x in range(1,total)]
            posts=posts[limit*(page-1):limit*page+1]
            count=len(posts)
            allposts=[]
            for post in posts:
                allposts.append({'id':post.job_id,'role':post.role,'locations':post.locations,'min_experience':post.min_experience,'max_experience':post.max_experience,'salary_from':post.salary_range_from,'salary_to':post.salary_range_to,'description':post.description,'skills':post.required_skills,'perks':post.perks,'post_date':post.date_posted})
            return JsonResponse({'responsecode':200,'metadata':{"resultset": {
                                                                  "count": count,
                                                                  "offset": limit*(page-1)+1,
                                                                  "limit": limit
                                                                },
                                                                'pagedata':{'currentpage':page,'pagelist':pages},
                                                                'data':allposts
                                                                }})
        except:
            return JsonResponse({'code':105,'message':'Invalid Request','description':'The Page Requested for could not be found on the server'})
    except:
            return JsonResponse({'code':106,'message':'Something Bad Happened','description':'The request could not be processed.'})


@csrf_exempt
@ratelimit(key='ip',rate='100/h')
def Createpost(request):
    try:
        if request.method=="POST":
            job_id=GenerateJobId()
            role=request.GET.get('role')
            locations=request.GET.get('locations')
            min_experience=int(request.GET.get('min_experience'))
            max_experience=int(request.GET.get('max_experience'))
            salary_range_from=float(request.GET.get('salary_range_from'))
            salary_range_to=float(request.GET.get('salary_range_to'))
            description=request.GET.get('description')
            required_skills=request.GET.get('required_skills')
            perks=request.GET.get('perks')
            date_posted=datetime.now()
            new_post=AllPosts(job_id=job_id,role=role,locations=locations,min_experience=min_experience,max_experience=max_experience,salary_range_from=salary_range_from,salary_range_to=salary_range_to,description=description,required_skills=required_skills,perks=perks,date_posted=date_posted)
            new_post.save()
            return JsonResponse({'responsecode':201,'message':"Job Post Created",'description':'The Job Post With the given details was sucessfully created'})
        else:
            return JsonResponse({'code':105,'message':'Invalid Request','description':'The request could not be processed as the method is Invalid.'})
    except:
        return JsonResponse({'code':106,'message':'Something Bad Happened','description':'The request could not be processed.'})
