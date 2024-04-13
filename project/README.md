# Создание видео бегущей строки

### Загрузить сервер: Python3 manage.py runserver

### Тест: Python3 manage.py test
### Адрес: localhost:8000
## Для работы необходимо установить библиотеки:
 - python3-moviepy
 - imagemagick
 - Django==5.0.4
 - Requests==2.31.0
 - django_extensions
#### Внутри есть сборка под линукс через доккер-файл
 ## Для функции генерации строки, все что необходимо (не для сервера) Для Goglecolab:
### !apt update
### !apt install python3.12
### !apt install python3-moviepy
### !apt-get install imagemagick
### !wget https://www.imagemagick.org/download/ImageMagick.tar.gz
### !tar xf ImageMagick.tar.gz 
### !cd ImageMagick-7* && ./configure && ./configure --with-modules && make && make -j 6 && make install
### !ldconfig /usr/local/lib

### from moviepy.config import change_settings
### change_settings({"IMAGEMAGICK_BINARY": "/usr/local/bin/magick"})


# Функция генерации бегущей строки.
### Созданная в виде отдельного класса.
### Создать экземпляр класса можно например так:
   ## n = GenerateMarqueeEffect() - это создаст экземпляр с установками по умолчанию
### Параметры:
' GenerateMarqueeEffect(
        text="text",
        font_color="#00364a",
        background_color="#e392fe",  ##e392fe
        size_font=70,
        duration_clip=3,
        width_video=100,
       height_video=100
        ) '
## 1. Параметр text присваивает значение текста:
### пример:
##    n = GenerateMarqueeEffect(text="Your text")
###    По умолчанию задано "text"
## 2. Выбрать цвет шрифта (font_color) и фона (background_color)
## Цвета необходимо задавать в формате Hex '#ffffff'
### пример:
##    n = GenerateMarqueeEffect(font_color=#ffffff)
## 3. Выбрать размер шрифта (size_font)
### Пример:
## n = GenerateMarqueeEffect(size_font = 100)
## 4. Выбрать длительность создаваемого видео (duration_clip):
### Пример:
## n = GenerateMarqueeEffect(duration_clip = 3)
## 5. Задать ширину и длинну окна (width_video, height_video):
Пример:
### n = GenerateMarqueeEffect(width_video=100,height_video=100)
## 6. Можно задать адресс куда будет сохраняться видео и его название. 
## Параметр address
## По умолчанию видео называется "moving_text.mp4", и сохраняется в текущей директории
## Так же параметры можно задавать спомощью функций:
##    set_text_string(str:str)
##    set_color_font(color:str)
##    set_color_background(color:str)
##    set_size_font(size: float)
##    set_duration_clip(duration_clip:float)
##    set_width_video(width_video: int)
##    set_height_video(height_video: int)
## И вернуть заданные:
##    get_text_string() -> str
##    get_color_font() -> str
##    get_color_background() -> str
##    get_size_font() -> float
##    get_duration_clip() -> float
##    get_width_video() -> float
##    get_height_video() -> float
## Функция генерации бегущей строки:    
#    create_movie()
### Например:
##    n = GenerateMarqueeEffect().create_movie()
### Или
##    n = GenerateMarqueeEffect()
##    n.create_movie()

