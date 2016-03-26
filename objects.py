from datetime import datetime

class Assignment():
    def __init__(self, name, due, length):
        self.name = name
        self.due = datetime.strptime(due, "%m~%d~%y~%H")
        self.length = int(length)

    def __str__(self):
        return "[Assignment {} {} {}]".format(self.name, self.due, self.length)

    def html(self):
        return "<p>{}</p>".format(str(self))

