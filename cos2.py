import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display


class f0c:
    f0cc = 0

# создание модулирующего сигнала такие как амплитуда несущей волны A_c
# частота несущей волны f_c
# продолжительность сигнала duration
# начальная фаза ф_0_с
# амплитуда сигнала A_m и частота ф_0_с


def generate_signal(A_c, f_c, duration, φ_0_c, A_m, f_m):

    t = np.linspace(0, duration, int(duration * 1000), endpoint=False)
    x_m = A_m * np.sin(2 * np.pi * 4 * t) + abs(A_m)

    f0c.f0cc += (np.cumsum(2 * np.pi * f_c * (1 + x_m) * 1 / len(t)))

    x = A_c * np.sin(f0c.f0cc)
    return t, x, x_m


def plot_signal(A_c, f_c, duration, φ_0_c, A_m, f_m):
    t, x, x_m = generate_signal(A_c, f_c, duration, φ_0_c, A_m, f_m)

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(t, x_m)
    plt.title("Модулирующий сигнал")
    plt.xlabel("Время (сек)")
    plt.ylabel("Значение модулирующего сигнала")
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(t, x)
    plt.title("Сгенерированный сигнал x(t)")
    plt.xlabel("Время (сек)")
    plt.ylabel("Значение сигнала")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


amplitude_m_slider = widgets.FloatSlider(
    value=1.0, min=0.1, max=5.0, step=0.1, description='Амплитуда модулирующего:')
frequency_m_slider = widgets.FloatSlider(
    value=2.0, min=0.1, max=1.0, step=0.1, description='Частота модулирующего (f_m):')
duration_slider = widgets.FloatSlider(
    value=1.0, min=0.1, max=10.0, step=0.1, description='Продолжительность (сек):')

interactive_plot = widgets.interactive(plot_signal, A_c=widgets.fixed(1.0), f_c=widgets.fixed(
    5.0), duration=duration_slider, φ_0_c=widgets.fixed(0.0), A_m=amplitude_m_slider, f_m=frequency_m_slider)

display(interactive_plot)
