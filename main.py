import subprocess
import requests
from pydub import AudioSegment
from datetime import datetime

# 设置起始和结束编号！！！
start_number = 
end_number = 

def download_ts_files(start, end):
    urls = []
    for i in range(start, end + 1):
        # 这里根据你要爬取的电台也要修改！！！
        # url = f'https://broadcast.tx.xmcdn.com/live/536_64_240716_000001_{i:04x}.ts'  
        response = requests.get(url)
        if response.status_code == 200:
            temp_filename = f'temp_{i}.ts'
            with open(temp_filename, 'wb') as f:
                f.write(response.content)
            urls.append(temp_filename)
            print(f"Downloaded: {url}")
        else:
            print(f"Failed to download: {url}")
    return urls

def concatenate_ts_files(ts_files, output_filename):
    with open("file_list.txt", "w") as f:
        for ts_file in ts_files:
            f.write(f"file '{ts_file}'\n")

    subprocess.run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', 'file_list.txt', '-c', 'copy', output_filename], check=True)
    print(f"Concatenated into: {output_filename}")

def convert_to_mp3(ts_file, output_filename):
    subprocess.run(['ffmpeg', '-y', '-i', ts_file, '-q:a', '0', '-map', 'a', output_filename], check=True)
    print(f"Converted to MP3: {output_filename}")

def normalize_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    normalized_audio = audio.normalize()
    normalized_audio.export(file_path, format='mp3')
    print(f"Normalized: {file_path}")

# 下载 TS 文件
ts_files = download_ts_files(start_number, end_number)

# 合并所有 TS 文件
concatenated_ts = 'concatenated.ts'
concatenate_ts_files(ts_files, concatenated_ts)

# 转换为 MP3
date = datetime.now().strftime('%Y-%m-%d')
mp3_filename = f'{date}.mp3'
convert_to_mp3(concatenated_ts, mp3_filename)

# 标准化音频
normalize_audio(mp3_filename)
