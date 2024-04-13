from marquee_effect import *
import unittest


class Test(unittest.TestCase):
    def test_default_constructor_color(self):
        n = GenerateMarqueeEffect(font_color="#ffffff", background_color="#000000")
        self.assertEqual(str(n.get_color_font()), "#ffffff")
        self.assertEqual(str(n.get_color_background()), "#000000")

    def test_init_constructor_color(self):
        n = GenerateMarqueeEffect(font_color="#00364a", background_color="#791a3e")
        self.assertEqual((n.get_color_font()), "#00364a")
        self.assertEqual(str(n.get_color_background()), "#791a3e")

    def test_init_setters_color(self):
        n = GenerateMarqueeEffect()
        n.set_color_font("#00364a")
        n.set_color_background("#791a3e")
        self.assertEqual((n.get_color_font()), "#00364a")
        self.assertEqual(str(n.get_color_background()), "#791a3e")

    def test_font(self):
        n = GenerateMarqueeEffect()
        self.assertEqual(n.get_size_font(), 70)
        n.set_size_font(18)
        self.assertEqual(n.get_size_font(), 18)
        n = GenerateMarqueeEffect(size_font=22)
        self.assertEqual(n.get_size_font(), 22)

    def test_duration_clip(self):
        n = GenerateMarqueeEffect()
        self.assertEqual(n.get_duration_clip(), 3)
        n.set_duration_clip(18)
        self.assertEqual(n.get_duration_clip(), 18)
        n = GenerateMarqueeEffect(duration_clip=22)
        self.assertEqual(n.get_duration_clip(), 22)

    def test_width_video(self):
        n = GenerateMarqueeEffect()
        self.assertEqual(n.get_width_video(), 100)
        n.set_width_video(18)
        self.assertEqual(n.get_width_video(), 18)
        n = GenerateMarqueeEffect(width_video=22)
        self.assertEqual(n.get_width_video(), 22)

    def test_height_video(self):
        n = GenerateMarqueeEffect()
        self.assertEqual(n.get_height_video(), 100)
        n.set_height_video(18)
        self.assertEqual(n.get_height_video(), 18)
        n = GenerateMarqueeEffect(height_video=22)
        self.assertEqual(n.get_height_video(), 22)

    def test_text_string(self):
        n = GenerateMarqueeEffect()
        self.assertEqual(n.get_text_string(), "text")
        n.set_text_string("18")
        self.assertEqual(n.get_text_string(), "18")
        n = GenerateMarqueeEffect(text="22")
        self.assertEqual(n.get_text_string(), "22")
        n = GenerateMarqueeEffect(text="")
        self.assertEqual(n.get_text_string(), "text")

    def test_create_movie(self):
        n = GenerateMarqueeEffect().create_movie()
        self.assertEqual(n, 0)
        n = GenerateMarqueeEffect(text="").create_movie()
        self.assertEqual(n, 0)
        n = GenerateMarqueeEffect(font_color="#ffffff").create_movie()
        self.assertEqual(n, 0)
        n = GenerateMarqueeEffect(background_color="#ffffff").create_movie()
        self.assertEqual(n, 0)
        t = "a" * 1000
        n = GenerateMarqueeEffect(text=t).create_movie()
        self.assertEqual(n, 0)
        n = GenerateMarqueeEffect(font_color="#ffffff").create_movie()
        self.assertEqual(n, 0)
        n = GenerateMarqueeEffect(background_color="#ffffff").create_movie()
        self.assertEqual(n, 0)
        n = GenerateMarqueeEffect(background_color="#e32400").create_movie()
        self.assertEqual(n, 0)

    def test_check_var(self):
        n = GenerateMarqueeEffect(font_color="255 ,192, 204").create_movie()
        self.assertEqual(n, -1)
        n = GenerateMarqueeEffect(
            text="t",
            height_video=-5,
            width_video=5,
            duration_clip=3,
            size_font=1,
            background_color="#e32400",
        ).create_movie()
        self.assertEqual(n, -1)
        n = GenerateMarqueeEffect(
            text="t",
            height_video="n",
            width_video=5,
            duration_clip=3,
            size_font=1,
            background_color="#e32400",
        ).create_movie()
        self.assertEqual(n, -1)
        n = GenerateMarqueeEffect(
            width_video=5, size_font="ú", background_color="#e32400"
        ).create_movie()
        self.assertEqual(n, -1)
        n = GenerateMarqueeEffect(
            width_video=5,
            duration_clip="ú",
            size_font=1,
            background_color="#e32400",
        ).create_movie()
        self.assertEqual(n, -1)
        n = GenerateMarqueeEffect(
            width_video=-5,
            duration_clip=3,
            size_font=1,
            background_color="#e32400",
        ).create_movie()
        self.assertEqual(n, -1)
        n = GenerateMarqueeEffect(
            width_video=5,
            duration_clip="k",
            size_font=1,
            background_color="#e32400",
        ).create_movie()
        self.assertEqual(n, -1)


if __name__ == "__main__":
    unittest.main()
