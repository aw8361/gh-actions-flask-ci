from gh_actions_flask_ci import create_app

if __name__ == "__main__":
    app = create_app("gh_actions_flask_ci.config.DevelopmentConfig")
    app.run()
