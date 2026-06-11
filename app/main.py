def project_health(status: str) -> str:
    """Return a project health message based on status."""
    status = status.lower().strip()

    if status == "green":
        return "Project is healthy."
    if status == "yellow":
        return "Project has moderate risk."
    if status == "red":
        return "Project requires immediate attention."

    return "Unknown project status."


if __name__ == "__main__":
    print(project_health("yellow"))