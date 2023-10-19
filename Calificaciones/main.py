import flet as ft
from linked_list import LinkedList
from student import Student

def main(page: ft.Page):
    def reset_error():
        error_name.value = ""
        error_grade.value = ""
        error_grade.visible = False
        error_name.visible = False

    def error_inputs(nombre, calificacion):
        result = True
        reset_error()
        if nombre == "":
            error_name.visible = True
            error_name.value = "Ingresa un nombre"
            result = False

        if calificacion == "":
            error_grade.visible = True
            error_grade.value = "Ingresa una calificación valida"
            result = False

        dot = False
        for char in calificacion:
            if not char.isdigit():
                if char == '.' and not dot:
                    dot = True
                else:
                    error_grade.visible = True
                    error_grade.value = "Ingresa una calificación valida"
                    result = False

        return result
    
    def handle_end(e):
        current = students.primero
        previous = None

        while current:
            student = current.valor

            if student.calificacion < 7.0:
                failed_students.insert(student)

                if previous:
                    previous.next_node = current.next_node
                else:
                    students.primero = current.next_node

                current = current.next_node
            else:
                previous = current
                current = current.next_node

        print_students()

    def handle_submit(e):
        nombre = input_name.value
        calificacion = input_grade.value
        if error_inputs(nombre, calificacion):
            if float(calificacion) > 10:
                error_grade.visible = True
                error_grade.value = "Ingresa una calificación entre 0 y 10"
            else:
                reset_error()
                input_name.value = ""
                input_grade.value = ""
                student = Student(nombre, float(calificacion))
                students.insert(student)
                print_students()

        page.update()

    def print_students():
        columna1.controls.clear()
        columna2.controls.clear()
        students_list = students.get_list()
        failed_students_list = failed_students.get_list()

        columna1.controls.append(ft.Text(f"Estudiantes Que Estan Aprobados", size=30))
        columna2.controls.append(ft.Text(f"Estudiantes Que Estan Reprobados"))

        for student in students_list:
            columna1.controls.append(ft.Text(f"{student.nombre}: {student.calificacion}"))
        for student in failed_students_list:
            columna2.controls.append(ft.Text(f"{student.nombre}: {student.calificacion}"))

        page.update()

    students = LinkedList()
    failed_students = LinkedList()
    input_name = ft.TextField(label="Nombre", width=400, bgcolor=ft.colors.WHITE10)
    input_grade = ft.TextField(label="Calificación", width=200, bgcolor=ft.colors.WHITE10)
    btn_submit = ft.ElevatedButton("Subir", on_click=handle_submit)
    btn_end = ft.ElevatedButton("Ver reprobados", on_click=handle_end)
    error_name = ft.Text(visible=False)
    error_grade = ft.Text(visible=False)
    columna1 = ft.Column([ft.Text(f"Estudiantes que estan Aprobados")])
    columna2 = ft.Column([ft.Text(f"Estudiantes que estan Reprobados")])
    row_students = ft.Row([columna1, columna2],alignment=ft.MainAxisAlignment.SPACE_AROUND)
    container_students = ft.Container(row_students, alignment=ft.alignment.top_center, border_radius=ft.border_radius.all(5), border=ft.border.all(5, ft.colors.DEEP_PURPLE_400), expand=True)

    main_container = ft.Container(ft.Column([input_name, error_name, input_grade, error_grade, btn_submit,btn_end], spacing=15), alignment=ft.alignment.top_center, margin=ft.margin.all(10))

    page.add(ft.Row([main_container,container_students],height=600))

ft.app(main)
