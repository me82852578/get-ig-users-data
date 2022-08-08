

def get_medias_with_comments(cl, user_id, amount=3):

    def parse_list_class_to_list_dict(data):
        new_list = []
        for d in data:
            new_list.append(d.dict())
        return new_list

    medias = parse_list_class_to_list_dict(cl.user_medias(user_id, amount))

    for idx, media in enumerate(medias):
        comments = parse_list_class_to_list_dict(
            cl.media_comments(media["id"])
        )
        medias[idx]["comments"] = comments

    return medias
