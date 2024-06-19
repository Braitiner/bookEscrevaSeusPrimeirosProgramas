BUFF_SIZE = 1024
def download_length(response, output, length):
    times = length / BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Download %d" % (((time * BUFF_SIZE)/length)*100))

def download(response, output):
    total_downloaded = 0
    while True:
        data = reponse.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Download {bytes}'.format(bytes=total_downloaded))

