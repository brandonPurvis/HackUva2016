class Assignment():
    def __init__(self, name, due, length):
        self.name = name
        self.due = due
        self.length = length

    def __str__(self):
        return "[Assignment {} {} {}]".format(self.name, self.due, self.length)

    def html(self):
        return "<p>{}</p>".format(str(self))

