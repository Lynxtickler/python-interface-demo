import inspect
from functools import wraps


def _validate_implementation(obj_or_class, interface_class):
    cls = obj_or_class if isinstance(obj_or_class, type) else type(obj_or_class)

    # Check methods and properties in the interface
    for name, member in inspect.getmembers(interface_class):
        if inspect.isfunction(member) or isinstance(member, property):
            # Ensure the decorated class has the same member
            if not hasattr(cls, name):
                raise TypeError(
                    f"Class '{cls.__name__}' must implement '{name}' from '{interface_class.__name__}'."
                )

            # If it's a property, ensure all relevant parts are implemented
            if isinstance(member, property):
                for accessor in ["fget", "fset", "fdel"]:
                    interface_part = getattr(member, accessor)
                    if interface_part and not getattr(
                        getattr(cls, name), accessor, None
                    ):
                        raise TypeError(
                            f"Class '{cls.__name__}' must implement the {accessor} of property '{name}' from '{interface_class.__name__}'."
                        )


def implements(interface_class):
    """
    Decorator to act as a pseudo keyword, which enforces that the decorated
    class implements all abstract methods and properties defined in the
    interface class.
    """

    def decorator(cls):
        _validate_implementation(cls, interface_class)
        return cls

    return decorator


def check_implements(arg_name, interface_class):
    """
    Decorator to validate that a specific argument to a method implements the specified interface.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            # Extract the argument by its name
            bound_args = inspect.signature(func).bind(*args, **kwargs)
            bound_args.apply_defaults()
            obj = bound_args.arguments.get(arg_name)
            if obj is None:
                raise ValueError(f"The argument '{arg_name}' cannot be None.")
            _validate_implementation(obj, interface_class)
            return result

        return wrapper

    return decorator
