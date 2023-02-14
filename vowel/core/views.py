from django.shortcuts import render
def vowel(request):
    return render(request,'index.html')

def clac(request):
    v_count=0
    c_count=0
    vol=['a','e','i','o','u',]
    if request.method=='POST':
        t=request.POST['text'].lower()
        
        for i in t:
            
            if not i.isalpha():
                continue
            elif i in vol:
                v_count+=1
            else:
                c_count+=1
           
        return render(request,'index.html',{'vowel':v_count,'consonants':c_count,'text':t})
    else:
        return render(request,'index.html')
            

# Create your views here.
