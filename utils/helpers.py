from typing import Type


def list_to_id_dict(init_list: list, objects_class: Type):
    if len(init_list) == 0:
        return dict()

    is_the_correct_type = all(isinstance(i, objects_class) for i in init_list)

    if not is_the_correct_type:
        raise ValueError("Incorrect datatypes for the input list or object")

    if all(hasattr(i, "id") for i in init_list):
        return {element.id: element for element in init_list}
    else:
        raise ValueError("Object must have 'id' attribute")
