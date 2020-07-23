from whiptail.runner import stdcheck, stdin, stdout

class whiptail:
    def __init__(self, widht, height):
        self.widht = widht
        self.height = height

    def msgbox(self, title, text):
        return stdin(
            f"whiptail --title {title} --msgbox {text} {self.widht} {self.height}")

    def yesno(self, title, text):
        return stdin(
            f"whiptail --title {title} --yesno {text} {self.widht} {self.height}")

    def infobox(self, title, text):
        return stdin(
            f"whiptail --title {title} --infobox {text} {self.widht} {self.height}")

    def inputbox(self, title, text):
        return stdout(
            f"whiptail --title {title} --inputbox {text} {self.widht} {self.height}")

    def passwordbox(self, title, text):
        return stdout(
            f"whiptail --title {title} --passwordbox {text} {self.widht} {self.height}")


    def checklist(self, title, text, options):
        items = []
        for index in options:
            items.append(
                f'"{list(options.keys()).index(index)}" "{index} - {options.get(index)}" OFF ')
        test = "".join(items)
        return stdcheck(
            f'whiptail --title "{title}" --checklist --fb "{text}" {self.widht} {self.height} 6 {test} 3>&1 1>&2 2>&3')

    def radiolist(self, title, text, options):
        items = []
        for index in options:
            items.append(
                f'"{list(options.keys()).index(index)}" "{index} - {options.get(index)}" OFF ')
        test = "".join(items)
        return stdcheck(
            f'whiptail --title "{title}" --radiolist "{text}" {self.widht} {self.height} 12 {test} 3>&1 1>&2 2>&3')



    # # to implement
    # def gauge(self, title, text):
    #     return stdin(f'whiptail --title {title} --gauge {text} {self.widht} {self.height}')

    # # to implement
    # def textbox(self, title, file):
    #     print("to implement")

    # # to implement
    # def menu(self, title, list):
    #     print("to implement")

# test = whiptail(20, 120)

# test.msgbox("msg", "Testing")
# test.yesno("msg", "testing")
# test.infobox("msg", "testing")
# test.inputbox("msg", "testing")
# test.passwordbox("msg", "testing")

# lista = {"Docker": "Docker as Docker", "Docker-compose": "Is a docker compose"}

# print(test.radiolist("Testando", "Este item foi criado para teste", lista))
# print(test.checklist("Testando", "Este item foi criado para teste", lista))