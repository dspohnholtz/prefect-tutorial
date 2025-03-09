from prefect import flow

# Source for code to deploy
SOURCE_REPO='https://github.com/dspohnholtz/prefect-tutorial.git'

if __name__ == '__main__':
    flow.from_source(
        source=SOURCE_REPO,
        entrypoint="first_workflow.py:show_stars",
    ).deploy(
        name="my_first_deployment",
        parameters={
            "github_repos": [
                "PrefectHQ/prefect",
                "pydantic/pydantic",
                "huggingface/transformers"
            ]
        },
        work_pool_name="my-work-pool",
        cron="0 * * * *",  # Run hourly
    )