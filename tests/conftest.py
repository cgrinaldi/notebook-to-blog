from notebook_to_blog import gist


def pytest_sessionstart(session):
    """Mock out create_gist() so no external API calls."""

    def create_gist(code, gh_creds):
        return "a_uuid"

    gist.create_gist = create_gist
