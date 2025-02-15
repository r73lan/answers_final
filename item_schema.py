SCHEMA_GET_ITEMS_200_SUCCESS = {
    'type': 'array',
    'items': {
        'type': 'object',
        'properties': {
            'id': {'type': 'string'},
            'sellerId': {'type': 'integer'},
            'name': {'type': 'string'},
            'price': {'type': 'integer'},
            'createdAt': {'type': 'string'},
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
                    {'type': 'null'}
                ]
            }
        },
        'required': ['id', 'sellerId', 'name', 'price', 'statistics'],
    }
}

SCHEMA_GET_ITEMS_404_NOT_FOUND = {
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

SCHEMA_POST_ITEMS_200_SUCCESS = {
    'type': 'object',
    'properties': {
        'status': { 'type': 'string' }
    }
}

SCHEMA_POST_ITEMS_400_BADREQUEST = {
        'type': 'object',
        'properties': {
            'result': {
                'type': 'object',
                'required': [ 'messages' ],
                'properties': {
                    'message':{'type': 'string'},
                    'messages':{
                        'type': 'object',    
                        'additionalProperties': {'type': 'string'}
                        }
                    },
            'status':{'type': 'string'}
            }
        }
    }
