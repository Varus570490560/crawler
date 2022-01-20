
def analysis_game_comment_json_to_tuple(json_input, app_id):
    res = set()
    for i in range(len(json_input['data']['list'])):
        created_time = int(json_input['data']['list'][i]['moment']['created_time'])
        star = int(json_input['data']['list'][i]['moment']['extended_entities']['reviews'][0]['score'])
        device = json_input['data']['list'][i]['moment']['extended_entities']['reviews'][0]['device']
        author_id = int(json_input['data']['list'][i]['moment']['author']['user']['id'])
        like_count = int(json_input['data']['list'][i]['moment']['extended_entities']['reviews'][0]['ups'])
        dislike_count = int(json_input['data']['list'][i]['moment']['extended_entities']['reviews'][0]['downs'])
        reply_count =int(json_input['data']['list'][i]['moment']['extended_entities']['reviews'][0]['comments'])
        content = json_input['data']['list'][i]['moment']['extended_entities']['reviews'][0]['contents']['text']
        res.add((created_time, star, device, author_id, like_count, dislike_count, reply_count, content, int(app_id)))
    return res
