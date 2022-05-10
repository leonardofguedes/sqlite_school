from add_students import  app_add_student
from add_schedule import app_add_schedule


def app():
    while True:
        question = str(input('Want to add a Student or a Schedule?[stu][sch][end]')).strip().lower()
        if question == 'stu':
            app_add_student()
        elif question == 'sch':
            app_add_schedule()
        else:
            break


if __name__ == '__main__':
    app()


