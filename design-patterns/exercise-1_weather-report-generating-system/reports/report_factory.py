from reports.text_report import TextReport
from reports.json_report import JSONReport
from reports.html_report import HTMLReport

class ReportFactory:
    @staticmethod
    def get_report(format_type):
        if format_type == 'text':
            return TextReport()
        elif format_type == 'json':
            return JSONReport()
        elif format_type == 'html':
            return HTMLReport()
        else:
            raise ValueError("Unknown format type")
