def analysis_game_comment_json_to_tuple(json_input, app_id):
    res = set()
    for i in range(len(json_input['data']['list'])):
        comment_id = int(json_input['data']['list'][i]['moment']['extended_entities']['reviews'][0]['id'])
        created_time = int(json_input['data']['list'][i]['moment']['created_time'])
        star = int(json_input['data']['list'][i]['moment']['extended_entities']['reviews'][0]['score'])
        device = json_input['data']['list'][i]['moment']['extended_entities']['reviews'][0]['device']
        author_id = int(json_input['data']['list'][i]['moment']['author']['user']['id'])
        like_count = int(json_input['data']['list'][i]['moment']['extended_entities']['reviews'][0]['ups'])
        dislike_count = int(json_input['data']['list'][i]['moment']['extended_entities']['reviews'][0]['downs'])
        reply_count = int(json_input['data']['list'][i]['moment']['extended_entities']['reviews'][0]['comments'])
        content = json_input['data']['list'][i]['moment']['extended_entities']['reviews'][0]['contents']['text']
        res.add((comment_id, created_time, star, device, author_id, like_count, dislike_count, reply_count, content,
                 int(app_id)))
    return res


def analysis_game_sub_comment_json_to_tuple(json_input, id_and_app_id):
    res = list()
    for i in range(len(json_input['data']['list'])):
        sub_comment_id = int(json_input['data']['list'][i]['id'])
        created_time = int(json_input['data']['list'][i]['created_time'])
        author_id = int(json_input['data']['list'][i]['author']['id'])
        to_author_id = '0'
        if 'reply_to_user' in json_input['data']['list'][i]:
            to_author_id = json_input['data']['list'][i]['reply_to_user']['id']
        content = json_input['data']['list'][i]['contents']['raw_text']
        like_count = json_input['data']['list'][i]['ups']
        comment_id = id_and_app_id[0]
        app_id = id_and_app_id[1]
        res.append((sub_comment_id, app_id, comment_id, created_time, author_id, to_author_id, content, like_count))
    return res
