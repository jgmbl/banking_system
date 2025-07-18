def object_lists_to_dict(
    init_list: list,
    dict_key,
    *,
    validation=None,
    validation_mode=None,
    reference=None,
):
    if validation:
        list_validation(
            init_list, mode=validation_mode, mode_reference=reference
        )

    if len(init_list) == 0:
        return dict()

    return {getattr(item, dict_key): item for item in init_list}


def list_validation(init_list: list, *, mode=tuple(), mode_reference=tuple()):
    if init_list is None:
        raise ValueError("Provided None value for list parameter")
    if not isinstance(init_list, list):
        raise TypeError("Provided parameter must be a list")

    if len(mode) != len(mode_reference):
        raise ValueError("mode and mode_reference must have the same length")

    for mode, value in zip(mode, mode_reference):
        if mode == "datatype":
            if value is None:
                raise ValueError("Missing 'value' for for mode='datatype'")

            is_the_correct_type = all(isinstance(i, value) for i in init_list)

            if not is_the_correct_type:
                raise ValueError(f"All elements must be type {value.__name__}")

        if mode == "has_attribute":
            if value is None:
                raise ValueError("Missing 'value' for for mode='is_attribute'")
            for i in init_list:
                if not hasattr(i, value):
                    raise AttributeError(
                        f"Class {i.__class__.__name__}is "
                        f"has no attribute {value}"
                    )
