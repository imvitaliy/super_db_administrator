from django.http import JsonResponse


USER_LIST = [
    {
        "username" : "pepe",
        "age" : 23,
        "role" : "Web Developer",
        "available_dbs" : [
            {
                "db" : "MySQL",
                "host" : "localhost",
                "port" : 3306,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
            {
                "db" : "MongoDB",
                "host" : "localhost",
                "port" : 27017,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
        ]
    },
    {
        "username" : "joselito",
        "age" : 24,
        "role" : "Web Developer",
        "available_dbs" : [
            {
                "db" : "MySQL",
                "host" : "localhost",
                "port" : 3306,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
            {
                "db" : "MongoDB",
                "host" : "localhost",
                "port" : 27017,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
        ]
    },
    {
        "username" : "manolito",
        "age" : 44,
        "role" : "Web Developer",
        "available_dbs" : [
            {
                "db" : "MySQL",
                "host" : "localhost",
                "port" : 3306,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
            {
                "db" : "MongoDB",
                "host" : "localhost",
                "port" : 27017,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
        ]
    },
    {
        "username" : "pedrosanchez",
        "age" : 48,
        "role" : "Web Developer",
        "available_dbs" : [
            {
                "db" : "MySQL",
                "host" : "localhost",
                "port" : 3306,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
            {
                "db" : "MongoDB",
                "host" : "localhost",
                "port" : 27017,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
        ]
    },
    {
        "username" : "josemota",
        "age" : 63,
        "role" : "Web Developer",
        "available_dbs" : [
            {
                "db" : "MySQL",
                "host" : "localhost",
                "port" : 3306,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
            {
                "db" : "MongoDB",
                "host" : "localhost",
                "port" : 27017,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
        ]
    },
    {
        "username" : "damian",
        "age" : 47,
        "role" : "Web Developer",
        "available_dbs" : [
            {
                "db" : "MySQL",
                "host" : "localhost",
                "port" : 3306,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
            {
                "db" : "MongoDB",
                "host" : "localhost",
                "port" : 27017,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
        ]
    },
    {
        "username" : "kilot",
        "age" : 87,
        "role" : "Web Developer",
        "available_dbs" : [
            {
                "db" : "MySQL",
                "host" : "localhost",
                "port" : 3306,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
            {
                "db" : "MongoDB",
                "host" : "localhost",
                "port" : 27017,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
        ]
    },
    {
        "username" : "fmanzano",
        "age" : 34,
        "role" : "Web Developer",
        "available_dbs" : [
            {
                "db" : "MySQL",
                "host" : "localhost",
                "port" : 3306,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
            {
                "db" : "MongoDB",
                "host" : "localhost",
                "port" : 27017,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
        ]
    },
    {
        "username" : "hyuya",
        "age" : 36,
        "role" : "Web Developer",
        "available_dbs" : [
            {
                "db" : "MySQL",
                "host" : "localhost",
                "port" : 3306,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
            {
                "db" : "MongoDB",
                "host" : "localhost",
                "port" : 27017,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
        ]
    },
    {
        "username" : "hinata",
        "age" : 23,
        "role" : "Web Developer",
        "available_dbs" : [
            {
                "db" : "MySQL",
                "host" : "localhost",
                "port" : 3306,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
            {
                "db" : "MongoDB",
                "host" : "localhost",
                "port" : 27017,
                "db_user" : "pepito",
                "db_pass" : "aasd_Asd3aasdA_456sc5"
            },
        ]
    },
]


def user_api_view(request):
    return JsonResponse(USER_LIST, safe=False)

def user_detail_api_view(request, user):
    try:
        return JsonResponse(USER_LIST[int(user)])
    except Exception as e:
        raise Exception
