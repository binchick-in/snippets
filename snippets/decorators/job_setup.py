from functools import wraps


def basic_job_setup(f: callable) -> callable:
    """Basic job setup decroator
    Wrap your entry function with this and add
    bootstrapping code

    Example Usage:

        @basic_job_setup
        def main():
            print("Do stuff...")
    """

    @wraps(f)
    def setup(*args, **kwargs):
        # Job Setup Code Here
        return f(*args, **kwargs)

    return setup


def parametarized_job_setup(x: str) -> callable:
    """Parameterized job setup decorator
    Wrap your entry function with this and do stuff with
    the param(s) before your entry function runs.

    Example Usage:

        @parametarized_job_setup("my parameter")
        def main():
            print("Do stuff...")
    """

    def inner_setup(f: callable) -> callable:
        @wraps(f)
        def setup(*args, **kwargs):
            # Job Setup Code Here
            # Probably do something with 'x'
            return f(*args, **kwargs)

        return setup

    return inner_setup
