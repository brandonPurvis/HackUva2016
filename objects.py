from datetime import datetime


class Assignment():
    def __init__(self, name, due, length):
        self.name = name
        self.due = datetime.strptime(due, "%m~%d~%Y~%H")
        self.length = int(length)

    def __str__(self):
        return "[Assignment {} {} {}]".format(self.name, self.due, self.length)


    def __cmp__(self, other):
        return self.till_due() - other.till_due()
    
    def html(self):
        return "<p>{}</p>".format(str(self))

    def till_due(self):
        return (self.due - datetime.now()).total_seconds()/3600
