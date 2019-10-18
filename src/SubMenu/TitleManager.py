class TitleManager:
    "classe gérant les titres dans un menu"
    def __init__(self,titles):
        self.titles = titles

    def draw(self, frame):
        for i in  self.titles:
            i.draw(frame)
