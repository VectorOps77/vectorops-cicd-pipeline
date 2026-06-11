from app.main import project_health


def test_project_health_green():
    assert project_health("green") == "Project is healthy."


def test_project_health_yellow():
    assert project_health("yellow") == "Project has moderate risk."


def test_project_health_red():
    assert project_health("red") == "Project requires immediate attention."