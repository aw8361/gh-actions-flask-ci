from gh_actions_flask_ci import create_app


def test_config():
    app = create_app("gh_actions_flask_ci.config.Config")
    assert not app.config["TESTING"]


def test_testing_config():
    app = create_app("gh_actions_flask_ci.config.TestingConfig")
    assert app.config["TESTING"]
