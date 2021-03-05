from django.shortcuts import render
from django.http import HttpResponse
from management.models import Fm as fb
import os
# Create your views here.
def index(request):
	if request.method == 'GET':
		data = fb.objects.all()
		#下表获取
		d_descipt = data[1].descipt
		#传输字典
		context = {
			'cs' : 'wanan',
			'lists' : data 
		}

		return render(request,'index.html',context)
		
	else:
		title = request.POST['title']
		descipt = request.POST['descipt']
		img = request.FILES['img']
		ffb = fb(title=title,descipt=descipt,img=img.name)
		ffb.save()
		#保存图片
		imgdir = os.path.join('statics',img.name)
		with open(imgdir,'wb+') as f:
			f.write(img.read())
		return HttpResponse(imgdir)








				#filter() 方法用于查询符合条件的数据。返回是列表集合
		#d_filter = fb.objects.filter(id=13)

		'''exclude() 方法用于查询不符合条件的数据。返回的是 QuerySet 类型数据，类似于 list，里面放的是不满足条件的模型类的对象，可用索引下标取出模型类的对象'''
		#d_exclude = fb.objects.exclude(id=1)
		#get() 方法用于查询符合条件的返回模型类的对象符合条件的对象只能为一个，如果符合筛选条件的对象超过了一个或者没有一个都会抛出错误。
		'''order_by() 方法用于对查询结果进行排序。

        返回的是 QuerySet类型数据，类似于list，里面放的是排序后的模型类的对象，可用索引下标取出模型类的对象。

		注意：

		a、参数的字段名要加引号。
		b、降序为在字段前面加个负号 -。'''



