import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label = "janela interna", tag = "junto"):
    dpg.add_text("SISTEMA ETE - Análise de dados")
    dpg.add_input_text(label = " 1º Semana.", default_value = "Insira aqui!")

    dpg.add_text("Concentração de Mercúrio.")
    dpg.add_slider_float(label = "mcg/L.", default_value = 5, max_value = 10)

    dpg.add_text("Concentração de Chumbo.")
    dpg.add_slider_float(label = "mg/L.", default_value = 5, max_value = 10)

    dpg.add_text("Concentração de Alumínio.")
    dpg.add_slider_float(label = "mg/L.", default_value = 5, max_value = 10)

    dpg.add_text("Escala de potabilidade.")
    dpg.add_slider_int(label = "%.", max_value = 100)

dpg.create_viewport(title = "Sistema ETE", width = 800, height = 600)
dpg.show_viewport()
dpg.set_primary_window("junto", True)
dpg.setup_dearpygui()
dpg.start_dearpygui()
dpg.destroy_context()
