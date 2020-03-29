def get_insert_position_form_sorted_array(
    array, new_word, accident: bool = False
) -> int:
    if not array:
        return 0

    if accident:
        return search_insert_position_with_accident_sorted_array(array, new_word)
    return search_insert_position_with_descending_sorted_array(array, new_word)


def search_insert_position_with_accident_sorted_array(array, new_word):
    raise NotImplementedError(
        "search insert position with accident order for new words in array had not implemented"
    )


def search_insert_position_with_descending_sorted_array(array, new_word):
    for i in range(0, len(array)):
        if array[i] < new_word:
            return i

    return len(array)
