from fastapi import Request
from fastapi import HTTPException
from time import time


request_history={}

def rate_limit(
        request:Request
):

    client_ip=request.client.host

    current_time=time()

    window=60
    max_requests=10


    if client_ip not in request_history:

        request_history[
            client_ip
        ]=[]


    request_history[
        client_ip
    ]=[

        req_time

        for req_time in
        request_history[
            client_ip
        ]

        if current_time
        -
        req_time

        < window
    ]


    if len(
        request_history[
            client_ip
        ]
    ) >= max_requests:

        raise HTTPException(
            status_code=429,
            detail=
            "Too many requests"
        )


    request_history[
        client_ip
    ].append(
        current_time
    )



