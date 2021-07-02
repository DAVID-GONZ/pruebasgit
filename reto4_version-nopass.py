# from pruebas import pruebas_codigo_estudiante


operaciones_usuario = ["udea.edu.co", "ingeniaudea.co", "twitter.com", "atras",
                       "atras", "adelante", "facebook.com", "facebook.com"]
pagina_default = "google.com"
operaciones_usuario2 = ['udemy.com', 'atras', 'adelante', 'facebook.com',
                       'atras', 'atras', 'adelante', 'udemy.com', 'adelante']
pagina_default2 = 'google.com'
p_back = []
p_forward = []
actual = 'google.com'


def new_url(new):
    global p_back, actual, p_forward
    if new is not None and new != str(actual):
        p_back.append(actual)
        actual = str(new)
        p_forward = []
    else:
        pass
    return p_back, actual, p_forward


def back():
    global p_back, actual, p_forward
    if not p_back:
        pass
    else:
        last_back = p_back.pop()
        p_forward.append(actual)
        actual = last_back
    return p_back, actual, p_forward


def forward():
    global p_back, actual, p_forward
    if not p_forward:
        pass
    else:
        last_forward = p_forward.pop()
        p_back.append(actual)
        actual = last_forward
    return p_back, actual, p_forward


def process_data(operations, default_page):
    global p_back, actual, p_forward
    for i in operations:
        if i == "atras":
            back()
        elif i == "adelante":
            forward()
        else:
            new_url(i)
    default_page = actual
    actual = default_page
    return p_back, actual, p_forward


processing = process_data(operaciones_usuario, pagina_default)
print(processing)
# new1 = str(input('New Page:'))
# print(new_url(new1))
#
# new2 = str(input('New Page:'))
# print(new_url(new2))
#
# new3 = str(input('New Page:'))
# print(new_url(new3))
#
# back1 = back(p_back, p_forward)
# print(back1)
#
# back2 = back(p_back, p_forward)
# print(back2)
#
# forward1 = forward(p_back, p_forward)
# print(forward1)
#
# new4 = str(input('New Page:'))
# print(new_url(new4))
#
# new5 = str(input('New Page:'))
# print(new_url(new5))
#
# print(type(p_forward), type(p_back), type(actual))

# # def actualizar_estado_pestana(operaciones_usuario, pagina_default):
# #     return pila_atras, pagina_actual, pila_adelante
#
#
# #pruebas_codigo_estudiante(actualizar_estado_pestana)
