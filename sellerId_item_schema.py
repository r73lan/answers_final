SCHEMA_GET_SELLERID_ITEM_200_SUCCESS = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'id': { 'type': 'string' },
            'sellerId': { 'type': 'integer' },
            'name': { 'type': 'string' },
            'price': { 'type': 'integer' },
            'createdAt': { 'type': 'string'},
            'statistics': {
                    'oneOf': [
                        {
                            'type': 'object',
                            'properties':{
                                'likes': { 'type': 'integer' },
                                'viewCount': { 'type': 'integer' },
                                'contacts': { 'type': 'integer' },
                            },
                            'required': [ 'likes', 'viewCount', 'contacts' ],
                        },
                        {'type': 'null'}
                    ]
            }
        },
        'required': [ 'id','sellerId','name','price','statistics']
    }
}

SCHEMA_GET_SELLERID_ITEM_400_BADREQUEST = {
    'type': 'object',
    'properties': {
            'result': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'},
                    'messages': {
                        'type': 'object',
                        'additionalProperties': {'type': 'string'}
                        },
                    },
                'required': ['messages']
                },
            'status': {'type': 'string'}         
        }
}