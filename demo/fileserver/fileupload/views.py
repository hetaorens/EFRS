from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(file.name, file)
        return render(request, 'fileupload/upload_success.html')
    return render(request, 'fileupload/upload.html')



def check_file(request):
    if request.method == 'POST' and request.POST.get('filename'):
        filename = request.POST['filename']
        fs = FileSystemStorage()
        file_exists = fs.exists(filename)
        if file_exists:
            return render(request, 'fileupload/check.html', {'filename': filename, 'file_exists': file_exists, 'download_url': fs.url(filename)})
        else:
            return render(request, 'fileupload/check.html', {'filename': filename, 'file_exists': file_exists})
    return render(request, 'fileupload/check.html')
 

 
def home(request):
    return render(request, 'fileupload/home.html')






