from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from models import Hyb
import json

message = "No Item found"
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def query(request, algo, uid, mid):
    hyb = Hyb.objects.filter(algo=algo, uid=uid, mid=mid)
    if hyb is None or len(hyb) == 0:
        return HttpResponse(message)
    obj = hyb[0]
    result = "userid: %s, movieid: %s, original rating: %s, BiasedMF: %s, RegSVD: %s, BPMF: %s, ItemKNN: %s, Hybrid: %s" % (obj.uid, obj.mid, obj.ori_rat, obj.biasedmf, obj.regsvd, obj.bpmf, obj.itemknn, obj.hyb)
    return HttpResponse(result)

def error(request):
    return HttpResponse(message)

#def query(request, algo, uid, mid):
#    hyb = Hyb.objects.filter(algo=algo, uid=uid, mid=mid)
#    if hyb is None or len(hyb) == 0:
#        return HttpResponse("No Item found")
#    obj = hyb[0]
#    result = "%s %s %s %s %s %s %s %s" % (obj.uid, obj.mid, obj.ori_rat, obj.biasedmf, obj.regsvd, obj.bpmf, obj.itemknn, obj.hyb)
#
#    # return html
#    template = loader.get_template('detail.html')
#    context = Context({
#        'result': result
#    })
#    return HttpResponse(template.render(context))
