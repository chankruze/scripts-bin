import os
# import time
from win10toast import ToastNotifier


def repeat():
    try:
        choice = list(str(input("\nWanna repeat? [Y/N]: ")).lower())[0]

        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            repeat()
    except IndexError:
        return repeat()


def show_notification(title, body, **kwargs):
    icon_path = kwargs.get('icon_path', '')
    duration = kwargs.get('duration', 5)

    if duration == "":
        duration = 5

    # change dir to the scripts location
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    # create instance
    toast = ToastNotifier()

    if icon_path:
        toast.show_toast(title, body, icon_path=icon_path, duration=duration)
    else:
        toast.show_toast(title, body)


if __name__ == "__main__":
    proceed = True
    count = 1

    while proceed:
        print(f"\n#{count}")
        n_name = str(input("Notification name: "))
        n_message = str(input("Message to show: "))
        n_icon_path = str(input("Enter icon path (default: python logo): "))
        n_duration = input("Enter Duration(default: 5): ")

        show_notification(n_name, n_message, icon_path=n_icon_path, duration=n_duration)

        count += 1
        proceed = repeat()
