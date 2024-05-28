import ffmpeg
import os

def extract_audio(video_file, output_audio_file):
    # Открываем входное видео
    input_video = ffmpeg.input(video_file)

    # Извлекаем аудио из входного видео
    audio = input_video.audio

    # Указываем выходной файл для аудио
    output_audio = ffmpeg.output(audio, output_audio_file)

    # Запускаем процесс
    ffmpeg.run(output_audio)


def replace_audio(video_file, audio_file, output_video_file):
    # Открываем входное видео и аудиофайл
    input_video = ffmpeg.input(video_file)
    input_audio = ffmpeg.input(audio_file)

    # Объединяем видео без аудио с новым аудио
    new_video = ffmpeg.concat(input_video['v'], input_audio['a'], v=1, a=1)

    # Указываем выходной файл для видео с новым аудио
    output_video = ffmpeg.output(new_video, output_video_file)

    # Запускаем процесс
    ffmpeg.run(output_video)


# Указываем путь к видеофайлу и путь к выходному аудиофайлу
video_file = r"C:\Users\User\PycharmProjects\Audio\input.mp4"
output_audio_file = r"C:\Users\User\PycharmProjects\Audio\output.mp3"
input_audio_file = r"C:\Users\User\PycharmProjects\Audio\input.mp3"
output_video_file = r"C:\Users\User\PycharmProjects\Audio\output_video.mp4"

# Добавляем путь к папке с ffmpeg.exe в переменную среды PATH
os.environ["PATH"] += os.pathsep + r"C:\Users\User\ffmpeg\bin"

# Вызываем функцию для извлечения аудио
extract_audio(video_file, output_audio_file)

# Вызываем функцию для замены аудио в видео
replace_audio(video_file, input_audio_file, output_video_file)

