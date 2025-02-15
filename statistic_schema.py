SCHEMA_GET_STAT_200_SUCCESS = {
    'type': 'array',
    'items': {
            'statistics': {
                'oneOf': [
                    {
                        'type': 'object',
                        'properties': {
                            'likes': {'type': 'integer'},
                            'viewCount': {'type': 'integer'},
                            'contacts': {'type': 'integer'}
                        },
                        'required': ['likes', 'viewCount', 'contacts'],
                    },
                    {'type': 'null'}]
            }
        }
    }

SCHEMA_GET_STAT_404_NOT_FOUND = {
    'type': 'object',
    'properties': {
        'result': {
            'type': 'object',
            'properties': {
                'message': {'type': 'string'},
                'messages': {'type': 'object'}
            },
            'required': ['messages'], 
        },
        'status': {'type': 'string'}
    },
}
