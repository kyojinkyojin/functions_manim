from manim import *
import numpy as np


class BasicParabol(Scene):
    def construct(self):
        axes = Axes(
            x_range = [-5,5,1],
            y_range = [-10,10,1],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE},
            tips=True,
            x_axis_config={
                "numbers_to_include": np.arange(-5, 5.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
        )
        parabol = axes.plot(lambda x: x**2, color=GREEN)
        self.add(axes)
        self.add(parabol)