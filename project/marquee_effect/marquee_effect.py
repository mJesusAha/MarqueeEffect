import moviepy.editor as mp
from sys import platform


class GenerateMarqueeEffect:
    """Содержит скрипт позволяющий создать видео бегущей строки с пользовательским текстом"""

    def __init__(
        self,
        text="text",
        font_color="#00364a",
        background_color="#e392fe",
        size_font=70,
        duration_clip=3,
        width_video=100,
        height_video=100,
        address="moving_text.mp4",
    ):
        self.duration_clip_ = duration_clip
        self.width_video_ = width_video
        self.height_video_ = height_video
        self.font_color_ = self.convert_color(str(font_color))
        self.font_color_h = font_color
        self.text_: str
        self.set_text_string(text)
        self.background_color_ = self.convert_color(str(background_color))
        self.background_color_h = background_color
        self.size_font_ = size_font
        self.address_ = address
        self.check_var()

    def check_var(self):
        if (
            str(self.size_font_).replace(".", "", 1).isdigit() == True
            and str(self.duration_clip_).replace(".", "", 1).isdigit() == True
            and str(self.width_video_).isdigit() == True
            and str(self.height_video_).isdigit() == True
        ):
            return 0
        else:
            print("Ошибка, должны быть цифры>0")
            return -1

    def convert_color(self, color: str):
        try:
            hex = color.lstrip("#")
            return tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))
        except:
            print("Ошибка, формата цвета")
            return -1

    def get_text_string(self) -> str:  # Получить заданный текст
        return self.text_

    def set_text_string(self, text_string: str):  # Установить текст
        self.text_ = "text" if len(str(text_string)) == 0 else str(text_string)

    def get_color_font(self) -> str:  # Получить значение цвета шрифта
        return self.font_color_h

    def get_color_background(self) -> str:  # Получить значение цвета фона
        return self.background_color_h

    def set_color_background(self, color: str):  # Установить значение цвета фона
        self.background_color_h = color
        self.background_color_ = self.convert_color(color)

    def set_color_font(self, color):  # Установить значение цвета шрифта
        self.font_color_ = self.convert_color(color)
        self.font_color_h = color

    def set_size_font(self, size: float):
        self.size_font_ = size
        self.check_var()

    def get_size_font(self) -> float:
        return self.size_font_

    def set_duration_clip(
        self, duration_clip: float
    ):  # Установить значение длительности видео
        self.duration_clip_ = duration_clip
        self.check_var()

    def get_duration_clip(self) -> float:
        return self.duration_clip_

    def set_width_video(self, width_video: int):  # Установить ширину
        self.width_video_ = width_video
        self.check_var()

    def get_width_video(self) -> float:  # Получить ширину
        return self.width_video_

    def set_height_video(self, height_video: int):  # Установить высоту
        self.height_video_ = height_video
        self.check_var()

    def get_height_video(self) -> float:  # Получить высоту
        return self.height_video_

    def create_movie(self):
        # print("**********", mp.TextClip.list("font")) - доступные шрифты в системе
        try:
            font_ = (
                "DejaVu-Sans-Bold"
                if platform == "linux" or platform == "linux2"
                else "Arial"
            )

            txt_clip = mp.TextClip(
                self.text_,
                fontsize=self.size_font_,
                color=f"rgb{self.font_color_}",
                font=font_,
            ).set_duration(self.duration_clip_)
            bg_clip = mp.ColorClip(
                size=(self.width_video_, self.height_video_),
                color=self.background_color_,
            ).set_duration(self.duration_clip_)

            textclip_width, textclip_height = txt_clip.size

            def translate(t):
                end_pos = (
                    -1 * ((textclip_width)),
                    self.height_video_ / 2 - textclip_height / 2,
                )
                start_pos = (
                    self.width_video_,
                    self.height_video_ / 2 - textclip_height / 2,
                )
                x = int(
                    start_pos[0] + t / self.duration_clip_ * (end_pos[0] - start_pos[0])
                )
                y = int(
                    start_pos[1] + t / self.duration_clip_ * (end_pos[1] - start_pos[1])
                )
                return (x, y)

            txt_moving = txt_clip.set_position(translate)
            video = mp.CompositeVideoClip([bg_clip, txt_moving])
            video.write_videofile(self.address_, fps=60)
            return 0
        except BaseException as e:
            print(f"error:{e}")
            return -1
