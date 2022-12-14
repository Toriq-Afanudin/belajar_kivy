from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatIconButton as md


class SimpleApp(MDApp):
    def build(self):
        return md(
            text="Hello World",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            icon="language-python",
        )


if __name__ == "__main__":
    SimpleApp().run()
