import subprocess

def get_thump(file, out):
    x = f'ffmpeg -i {file} -ss 00:00:10 -vframes 1 {out}'
    c = subprocess.check_output(x, shell=True)
    print(c)