import subprocess
from django.shortcuts import render
from django.http import StreamingHttpResponse

def download(request, url):
    process = subprocess.Popen(
        ['yt-dlp', '-o', '-', url],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1024*8
    )

    def stream_generator():
        while True
            chunk = process.stdout.read(8192)
            if not chunk:
                break
            yield chunk
        process.stdout.close()
        process.wait()

    response = StreamingHttpResponse(stream_generator(), content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="video.mp4"'
    return response


def index(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        return download(request, url)

    template_name = 'index.html'
    return render(request, template_name)

