from reportlab.platypus import Paragraph


class StrikeThroughParagraph(Paragraph):
    def __init__(self, text, style):
        super().__init__(text, style)

    def draw(self):
        super().draw()
        if hasattr(self, 'blPara') and self.blPara:

            for i, frag in enumerate(self.blPara.lines):
                line_width = self.width
                y = self.height - (i + 0.5) * self.style.leading
                self.canv.setLineWidth(0.5)
                self.canv.line(0, y, line_width, y)

