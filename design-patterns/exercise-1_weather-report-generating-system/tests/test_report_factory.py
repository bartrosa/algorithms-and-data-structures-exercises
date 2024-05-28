import pytest
from reports.report_factory import ReportFactory
from reports.text_report import TextReport
from reports.json_report import JSONReport
from reports.html_report import HTMLReport

def test_report_factory_text():
    report = ReportFactory.get_report("text")
    assert isinstance(report, TextReport)

def test_report_factory_json():
    report = ReportFactory.get_report("json")
    assert isinstance(report, JSONReport)

def test_report_factory_html():
    report = ReportFactory.get_report("html")
    assert isinstance(report, HTMLReport)

def test_report_factory_invalid():
    with pytest.raises(ValueError):
        ReportFactory.get_report("invalid")
