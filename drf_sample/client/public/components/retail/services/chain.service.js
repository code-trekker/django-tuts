retail
    .factory('Chain', function($resource) {
        return $resource(
            'http://127.0.0.1:8000/chains/:id/',
            {},
            {
                'query': {
                    method: 'GET',
                    isArray: true,
                    headers: {
                        'Content-Type':'application/json'
                    }
                }
            },
            {
                stripTrailingSlashes: false
            }
        );
    });
